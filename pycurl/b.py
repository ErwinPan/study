import urllib
import pycurl
import StringIO

url = 'http://www.google.com/'

def run(url):
    c = pycurl.Curl()
    c.setopt( pycurl.URL , url )
    c.setopt( pycurl.FOLLOWLOCATION , True )

    c.setopt( pycurl.COOKIEFILE , './pycurl' )
    c.setopt( pycurl.COOKIEJAR , './pycurl' )

    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)

    c.perform()

    #print b.getvalue()
    r = b.getvalue()
    b.close()
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)


    check = re.findall( re.compile( '(<form(.*?)</form>)' , flags=(re.IGNORECASE|re.DOTALL) ) , r );
    if len(check) < 1 :
        print "No FORM DATA"
        return 0

    r = check[0][1]
    out = {} 
    for sub_info in re.findall( re.compile( '<input(.*?)(name=[\'"]{0,1}(.*?)[\'"]{0,1}[\s]+value=[\'"]{0,1}(.*?)[\'"]{0,1}[\s>]|value=[\'"]{0,1}(.*?)[\'"]{0,1}[\s]+name=[\'"]{0,1}(.*?)[\'"]{0,1}[\s>])' , flags=re.IGNORECASE ) , r ):
        if len(sub_info) != 6 :
                continue
        if sub_info[2] != '':
                out[ sub_info[2] ] = sub_info[3]
        elif sub_info[5] != '':
                out[ sub_info[5] ] = sub_info[4]

    for key in out :
        print "\t",key,":\t",out[key]

    url = 'target_form_action_url'
    c.setopt( pycurl.URL , url )
    c.setopt( pycurl.FOLLOWLOCATION , True )
    c.setopt( pycurl.POST , True )
    c.setopt( pycurl.POSTFIELDS , urllib.urlencode(out) )

    c.perform()

    #print b.getvalue()
    r = b.getvalue()
    b.close()

    f = open( target_file , 'wb' )
    f.write( r )
    f.close()


if __name__ == '__main__':
    print "done"

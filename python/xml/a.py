# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys
import re

# Refer to http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/processing-xml-in-python-with-element-tree.html

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
'''
<?xml version="1.0"?>
<doc>
    <branch name="testing" hash="1cdf045c">
        text,source
    </branch>
    <branch name="release01" hash="f200013e">
        <sub-branch name="subrelease01">
            xml,sgml
        </sub-branch>
    </branch>
    <branch name="invalid">
    </branch>
</doc>
'''

def xml_create(xml_file):
    
    # Create xml tree
    try:
        tree = ET.ElementTree(file=xml_file)
        root = tree.getroot()
        print "xml file %s loaded ..." % xml_file
    except:
        root = ET.Element('doc')
        tree = ET.ElementTree(root)

        # Append a single element
        a = ET.Element('branch')
        a.set('name', 'testing')
        a.set('hash', '1cdf045c')
        a.text = '\n        text,source\n'
        root.append(a)

        b = ET.Element('branch')
        b.set('name', 'release01')
        b.set('hash', 'f200013e')

        c = ET.SubElement(b, 'sub-branch')
        c.set('name', 'subrelease01')
        c.text = '\n            xml,sgml\n'

        d = ET.Element('branch')
        d.set('name', 'invalid')
    
        # Append a tuple of element by 'extend'
        root.extend((b, d))

        tree.write(xml_file)
        print "new xml file %s created ..." % xml_file


    # for subelem in root:
    for subelem in root:
        print subelem.tag, subelem.attrib

    for elem in tree.iterfind('branch/sub-branch'):
        print elem.tag, elem.attrib

    for elem in tree.iterfind('branch[@name="release01"]'):
        print elem.tag, elem.attrib


    # Dump whole tree
    #tree.write(sys.stdout)   # ET.dump can also serve this purpose

    tree.write(xml_file)

if __name__ == '__main__':
    try:
                     
        xml_create('out.xml')

        print "xml done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        print "xml failed"
        sys.exit(-1)

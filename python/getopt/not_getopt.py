import sys
import traceback
import getopt



def print_usage(cmd):
    usage = '''
        -c, --parse-category
            Parse category
        -l, --parse-list-file=FILE
            Parse a list file
        -d, --parse-list-file=DIR
            Parse list files in a directory
        -h, --help
            Print this usage
    '''

    print ('\n%s usage: ' + usage) % cmd
    return



def main(argv):

    parse_category = None
    parse_list_file = None
    parse_list_dir = None

    try:
        print "...xxx argv=%s" % str(argv)
        opts, other_args = getopt.getopt(argv[1:],"cf:d:",["parse-category=", "parse-list-file=", "parse-list-dir="])

    except getopt.GetoptError:
        print "...123"
        traceback.print_exc()
        print_usage(argv[0])
        sys.exit(-1)

    for opt, arg in opts:
        if opt in ("-c", "--parse-category"):
            parse_category = True
        elif opt in ("-f", "--parse-list-file"):
            parse_list_file = arg
        elif opt in ("-d", "--parse-list-dir"):
            parse_list_dir = arg

    if not parse_category and not parse_list_file and not parse_list_dir:
        print_usage(argv[0])
        sys.exit()

    return parse_category, parse_list_file, parse_list_dir



if __name__ == '__main__':
    try:

        parse_category, parse_list_file, parse_list_dir = main(sys.argv)


        if parse_category is not None:
            # Define Root Category Entry
            pass

        if parse_list_file is not None:
            pass

        if parse_list_dir is not None:
            pass

        print "done"
        sys.exit(0)

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)


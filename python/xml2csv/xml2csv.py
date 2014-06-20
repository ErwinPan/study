## Call libraries
import csv
from xmlutils.xml2csv import xml2csv

import sys, getopt

def print_usage(cmd):
    print 'argv[0] -i <inputfile> -o <outputfile>'


def main(argv, inputfile, outputfile):
    try:
        opts, args = getopt.getopt(argv[1:],"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print_usage(argv[0])
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if inputfile == '' or outputfile == '':
        print_usage(argv[0])
        sys.exit()
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile
    return inputfile, outputfile


def doxml2csv(inputfile, outputfile):
    converter = xml2csv(inputfile, outputfile, encoding="utf-8")
    converter.convert(tag="message")
    print 'Convert done ...'


if __name__ == "__main__":
    inputfile = ''
    outputfile = ''
    
    inputfile, outputfile = main(sys.argv, inputfile, outputfile)

    doxml2csv(inputfile, outputfile)

    #print "Using (print >> sys.stderr, 'X'): %s" %(s1)
    #print >> sys.stderr, 'X'

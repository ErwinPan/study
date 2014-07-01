# -*- coding: utf-8 -*-
import urllib
import pycurl
import StringIO
import traceback
import sys, getopt
import re
import string
import time
import random
import os
import errno
from datetime import datetime, date, time


def printf(*argv):
    try:
        print ("%s " + argv[0]) % ( (datetime.now().strftime("[%Y/%m/%d %H:%M:%S.%f]"), ) +  argv[1:])

    except Exception, e:
        traceback.print_exc()

    pass



if __name__ == '__main__':
    try:
        printf("test = %d, %d, str=%s", 1, 3, "123")

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)

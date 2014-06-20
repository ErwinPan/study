import os
from os.path import join, getsize

for root, dirs, files in os.walk('../'):
    print "===root (%s) consumes" % str(root)
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"

    for d in dirs:
        print "d: %s" % str(d)

    for f in files:
        print "f: %s" % str(f)

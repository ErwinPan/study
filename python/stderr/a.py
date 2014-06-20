import time
import sys


def run1(runs):
    x = 0
    cur = time.time()
    while x < runs:
        x += 1
        print >> sys.stderr, 'X'
    elapsed = (time.time()-cur)
    return elapsed

def run2(runs):
    x = 0
    cur = time.time()
    while x < runs:
        x += 1
        sys.stderr.write('X\n')
        sys.stderr.flush()
    elapsed = (time.time()-cur)
    return elapsed

def compare(runs):
    sum1, sum2 = 0, 0
    x = 0
    while x < runs:
        x += 1
        sum1 += run1(runs)
        sum2 += run2(runs)
    return sum1, sum2

if __name__ == '__main__':
    s1, s2 = compare(1000)
    print "Using (print >> sys.stderr, 'X'): %s" %(s1)
    print "Using (sys.stderr.write('X'),sys.stderr.flush()):%s" %(s2)
    print "Ratio: %f" %(float(s1) / float(s2))

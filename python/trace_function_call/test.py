# Ref
#       http://www.dalkescientific.com/writings/diary/archive/2005/04/20/tracing_python_code.html

import sys
import commands
import linecache
import traceback

print >> sys.stderr, "<call from='[main]'>"

def co_name_filter(co_name):
    if co_name == '<module>':
        co_name = 'main'
    co_name = co_name.replace('<', '[')
    co_name = co_name.replace('>', ']')
    return co_name

def traceit(frame, event, arg):
    global call_stack_count
    frame_caller = frame.f_back

    if event == "line" and 0:
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        line = linecache.getline(filename, lineno)
        print "%s, line %d: %s" % (filename, lineno, line.rstrip())
        print "frame code line: %s" % frame.f_code
    elif event == 'call':
        caller_co_name = co_name_filter(frame_caller.f_code.co_name)
        co_name = co_name_filter(frame.f_code.co_name)

        print >> sys.stderr, '<call from="[%s] in (%s:%d)" to="[%s]">' % (caller_co_name, frame_caller.f_globals["__file__"], frame_caller.f_lineno, co_name)
    elif event == 'return':
        print >> sys.stderr, "</call>"

    return traceit


sys.settrace(traceit)

############################ copy codes above ###############################

xmms='xmms2'

call_stack_count = 0


def hello_world():
    print "Hello World!!"
    pass


if __name__ == '__main__':
    try:
        ret = commands.getoutput("which " + xmms).find(xmms)
        hello_world()
        print 'ret = %s' % ret
        
    
    except Exception, e:
	traceback.print_exc()
        sys.exit(-1)

############################ copy codes below ###############################

print >> sys.stderr, "</call>"

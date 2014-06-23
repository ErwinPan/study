import sys
import traceback
import getopt
import sqlite3


def sqlite3_test(db_name):

    try:
        conn = sqlite3.connect(db_name)

        cur = conn.cursor()

        # Never do this -- insecure!
        #symbol = 'RHAT'
        #cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

        # Do this instead to return a row of result as 'tuple'
        t = ('RHAT',)
        cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
        ret = cur.fetchone()
        print '1st row: %s' % str(ret)

        # Fetches the next row of a query result set, returning a single sequence, or None when no more data is available.
        ret = cur.fetchone()
        print '2nd row: %s' % str(ret)

        
        # Fetches the next set of rows of a query result, returning a list. An empty list is returned when no more rows are available.
        ret = cur.fetchmany(size = 3)
        print "type of result of fetchmany is %s" % (str(type(ret)))
        for row in ret:
            print row

        ret = cur.fetchmany(size = 3)
        print "type of result of fetchmany is %s" % (str(type(ret)))
        for row in ret:
            print row


        # Fetches all (or 'remaining' if fetched) rows of a query result, returning a list.
        ret = cur.fetchall()
        print "type of result of fetchall is %s, %s" % (str(type(ret)), str(type(ret[0])))
        for row in ret:
            print row


        # Execute and return an array of tuple
        ret = cur.execute('SELECT * FROM stocks ORDER BY price')
        print "type of result of execute is %s" % str(type(ret))
        for row in ret:
            print row

        #            (u'2006-01-05', u'BUY', u'RHAT', 100, 35.14)
        #            (u'2006-03-28', u'BUY', u'IBM', 1000, 45.0)
        #            (u'2006-04-06', u'SELL', u'IBM', 500, 53.0)
        #            (u'2006-04-05', u'BUY', u'MSFT', 1000, 72.0)


        conn.close()


    except Exception, e:
        traceback.print_exc()

    pass



def sqlite3_execute_script_with_transaction(db_name):

    try:
        conn = sqlite3.connect(db_name)

        cur = conn.cursor()

        cur.executescript("""
            create table person(
                firstname,
                lastname,
                age
            );

            create table book(
                title,
                author,
                published
            );

            insert into book(title, author, published)
            values (
                'Dirk Gently''s Holistic Detective Agency',
                'Douglas Adams',
                1987
            );
            """)
    
    except sqlite3.Error, e:
        print 'Execute script failed and rollback'
        if conn:
            conn.rollback()
        pass # due to table exists

    except Exception, e:
        traceback.print_exc()

    
    conn.commit()
    conn.close()


def sqlite3_create(db_name):

    try:
        conn = sqlite3.connect(db_name)

        cur = conn.cursor()

        # Create table
        cur.execute('''CREATE TABLE stocks
                             (date text, trans text, symbol text, qty real, price real)''')

    except sqlite3.OperationalError:
        print 'sqlite3.OperationalError: insert fail due to table exist '

    except Exception, e:
        traceback.print_exc()
        return

    try:
        # Insert a row of data
        cur.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

        # Larger example that inserts many records at a time
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]
        cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

    except Exception, e:
        traceback.print_exc()

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

    pass


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

        sqlite3_create('test.db');

        sqlite3_execute_script_with_transaction('test.db');

        sqlite3_test('test.db');

        sys.exit(0)

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


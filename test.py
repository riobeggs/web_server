#!/usr/bin/python
import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(**params)
        conn_info = {
            "dbname": "test",
            "user": "postgres",
            "password": "postgres"
        }

        # use kwargs to connect to database
        conn = psycopg2.connect(**conn_info)

        query = "SELECT * FROM person WHERE last_name = 'beggs' ;"

        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute(query)

        # display the PostgreSQL database server version
        result = cur.fetchall()
        print(result)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect2():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(**params)
        conn_info = {
            "dbname": "test",
            "user": "postgres",
            "password": "postgres"
        }
        conn = psycopg2.connect(**conn_info)

        # multi part query
        query = "SELECT * FROM person"
        last_name = input("enter last name: ")

        # query limited to 1 response
        query += f' WHERE last_name = \'{last_name}\' limit 1;'

        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute(query)

        # return all results of query
        result = cur.fetchall()
        print(result)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect3():
    """ Connect to the PostgreSQL database server 
    use a with statement to control db connection"""

    conn_info = {
            "dbname": "test",
            "user": "postgres",
            "password": "postgres"
        }

        # multi part query
    query = "SELECT * FROM person"

    # query limited to 1 response
    query += ' WHERE last_name = \'beggs\';'

    try:
        with psycopg2.connect(**conn_info) as conn, \
            conn.cursor() as cur:
            cur.execute(query)
            res = cur.fetchall()
            print(res)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    connect3()

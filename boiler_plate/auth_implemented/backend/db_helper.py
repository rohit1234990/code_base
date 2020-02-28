import pymysql.cursors
import pymysql


def connect():
    connection  = pymysql.connect(host='localhost',
                    user='scott',
                    password='Admin123*',
                    db='projects',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

    return connection
    
def insert(query, arguments):
    result = None      
    try:
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(query, arguments)
        
        conn.commit()
        result = {'result': 'success'}
    except Exception:
        result = {'result': 'failure'}
    finally:
        conn.close()
        return result

def select_one(query, arguments):
    result = None      
    try:
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(query, arguments)
            result = {'result': 'success', 'data': cursor.fetchone()}
    except Exception:
        result = {'result': 'failure'}
    finally:
        conn.close()
        return result

def select_all(query, arguments):
    result = None      
    try:
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(query, arguments)
            result = {'result': 'success', 'data': cursor.fetchall()}
    except Exception:
        result = {'result': 'failure'}
    finally:
        conn.close()
        return result


def delete_helper(query_arr):
    try:
        conn = connect()
        with conn.cursor() as cursor:
            for query in query_arr:
                cursor.execute(query[0], query[1])
            result = {'result': 'success'}
            conn.commit()
    except Exception:
        result = {'result': 'failure'}
    finally:
        conn.close()
        return result

def edit_helper(query, arguments):
    try:
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(query, arguments)
            conn.commit()
            result = {'result': 'success'}            
    except Exception:
        result = {'result': 'failure'}
    finally:
        conn.close()
        return result

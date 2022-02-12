import psycopg2
import os 
import sys


conn = None
try:
    conn = psycopg2.connect(database=sys.argv[1],
                            user=os.environ.get('PGUSER'),
                            password=os.environ.get('PGPASSWORD'),
                            host=os.environ.get('PGHOST'),
                            port=os.environ.get('PGPORT'))
    with open('date.txt', 'r') as f:
        date = f.readline()
    curr = conn.cursor()    
    sql =   '''
            SELECT r.name FROM match_referees AS mr, referees AS r, matches AS m 
            WHERE mr.referee = r.referee_id 
            AND mr.match_num = m.match_num 
            AND m.match_date = '{}'
            '''.format(date)

    curr.execute(sql)
    while True:
        row = curr.fetchone()
        if not row:
            break
        name = row[0].split(' ')
        print(name[-1], end=' ')
        for i in range((len(name)-2)):
            print(f'{name[i][0]}.', end=' ')
        print(f'{name[len(name)-2][0]}.')
#         print(name)
    curr.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

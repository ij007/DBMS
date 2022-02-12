import psycopg2
import os 
import sys
import math


conn = None
try:
    conn = psycopg2.connect(database=sys.argv[1],
                            user=os.environ.get('PGUSER'),
                            password=os.environ.get('PGPASSWORD'),
                            host=os.environ.get('PGHOST'),
                            port=os.environ.get('PGPORT'))
    curr = conn.cursor()
    with open('parameter.txt', 'r') as f:
        start = f.readline()    
    sql =   '''
            SELECT sum(m.host_team_score) FROM matches m, teams t 
            WHERE host_team_score>guest_team_score 
            AND m.host_team_id = t.team_id 
            AND t.name like '{}%'
            
            '''.format(start)
    curr.execute(sql)

    result = curr.fetchone()
    result = int(result[0])
    pi = math.pi
    deg = result * 10 * (pi/180)
    v = round(math.cos(deg),2)
    print(v)
        
    curr.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()

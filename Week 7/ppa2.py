import psycopg2
import os 
import sys

def dcode(x):
    l=''
    for i in x:
        if i.isalpha():
            s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            a=s[(s.index(x[0])+7)%26]
            l+=a
        if i.isdigit():
            b=(int(i)+7)%10
            l+=str(b)

    return l
conn = None
try:
    conn = psycopg2.connect(database=sys.argv[1],user=os.environ.get('PGUSER'), password=os.environ.get('PGPASSWORD'),host=os.environ.get('PGHOST'),port=os.environ.get('PGPORT'))
    curr=conn.cursor()
    sql =   '''
            SELECT team_id FROM teams WHERE jersey_home_color != jersey_away_color ORDER BY team_id ASC;
            '''
    curr.execute(sql)
    while True:
        row = curr.fetchone()
        if not row:
            break
        print(dcode(row[0]))
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


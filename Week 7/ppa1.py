import psycopg2
import sys
import os
def isprime(x):
    if x <=1:
        return False
    for i in range(2,x):
        if x%i==0 :
            return False
    return True

conn=None
try:
    conn= psycopg2.connect(database=sys.argv[1],user=os.environ.get('PGUSER'), password=os.environ.get('PGPASSWORD'),host=os.environ.get('PGHOST'),port=os.environ.get('PGPORT'))
    curr=conn.cursor()
    curr.execute( "select t.name,p.name,p.jersey_no from teams t , players p where t.team_id=p.team_id order by p.name desc,t.name desc")
    while True:
        row=curr.fetchone()
        if not row :
            break
        if isprime(row[2]):
            print(f'{row[1]}, {row[0]}')
    curr.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
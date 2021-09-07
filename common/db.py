import json
import mysql.connector
import sqlalchemy
import sqlalchemy.pool as pool
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

config = {
    'user': 'koushik', 
    'password': 'ThisisallM!',
    'host': '192.168.29.148',
    'database': 'cherry_coster'
}

def format(rows, cols):
    arr = []
    for t in rows:        
        for i,c in enumerate(cols):                        
            arr.append({ c: json.loads(t[i]) if isinstance(t[i], str) else t[i] })
    return arr

#engine=create_engine("mysql+mysqldb://koushik:ThisisallM!@192.168.0.112[:3306]/cherry_coster")

engine = create_engine(
    "mysql+mysqldb://koushik:ThisisallM!@192.168.29.148:3306/cherry_coster",
    pool_size=50, 
    max_overflow=0,
    echo=True
)

def execute(query, read=True):
    if read:
        result=engine.execute(query)
        for row in result:
            print(row)
        return ""
        #self.cursor.execute(query)
        #return [format(self.cursor.fetchall(), self.cursor.column_names), list(self.cursor.column_names)]
    else:
        with Session(engine) as session:
            pass

class DB:
    #Variable
    #Functions
    def __init__(self):
        self.connection = engine.raw_connection()    
    
    def execute(self, query, read=True):
        if read:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)                    
            return [format(self.cursor.fetchall(), list(map((lambda d:d[0]), self.cursor.description))), list(map((lambda d:d[0]), self.cursor.description))]
        else:
            #self.cursor = self.connection.cursor()
            #self.cursor.execute(query)
            #print(self.cursor.lastrowid)
            with Session(engine) as session:
                self.cursor = session.execute(query)
                #session.flush()
                print(self.cursor.lastrowid)
                #session.rollback()
                #return [format(self.cursor.fetchall(), list(map((lambda d:d[0]), self.cursor.description))), list(map((lambda d:d[0]), self.cursor.description))]


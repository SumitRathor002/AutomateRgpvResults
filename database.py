import sqlite3 
   
class Database:   
    def __init__(self):
        self.conn = sqlite3.connect('Results.db')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(""" CREATE TABLE results(
                Name text,
                RollNumber text,
                SGPA real,
                CGPA real
            )""")
            self.conn.commit()
        except sqlite3.OperationalError as e:
            if 'table results already exists' in str(e):
                pass
            else:
                print(e)

    # def deletedup(self):
    #     self.cursor.execute("""DELETE FROM results
    #                             WHERE rowid NOT IN (SELECT MIN(rowid)
    #                             FROM results
    #                             GROUP BY RollNumber);
    #                             )""")
    #     self.conn.commit()
    

import sqlite3

db_name = "autoparkas.db"

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

query = """
    SELECT COUNT(*) 
    FROM Autoparkas
    WHERE DEGALAI = 'Dyzelinas' 
      AND strftime('%Y', 'now') - CAST(substr(PIRM_REG_DATA, 1, 4) AS INT) > 10;
"""

cursor.execute(query)
total_count = cursor.fetchone()[0]

print("Total number of diesel vehicles older than 10 years:", total_count)

conn.close()

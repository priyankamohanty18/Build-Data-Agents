from snowflake_connection import get_connection

conn = get_connection()

cursor = conn.cursor()

try:
    cursor.execute("SELECT * from EMPLOYEE LIMIT 5")
    print("Connected successfully")
    print(cursor.fetchone())
finally:
    cursor.close()
    conn.close()
        
    
    
    
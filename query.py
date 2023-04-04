import cx_Oracle
import pandas as pd

# Set up connection details
dsn_tns = cx_Oracle.makedsn('your_host', 'your_port', service_name='your_service_name')
conn = cx_Oracle.connect(user='your_username', password='your_password', dsn=dsn_tns)

# Read SQL query from file
with open('query.sql', 'r') as f:
    sql_query = f.read()

# Execute query and load result into dataframe
df = pd.read_sql(sql_query, conn)

# Close the connection
conn.close()

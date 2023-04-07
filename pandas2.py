import cx_Oracle
from config_params import username, password, hostname, port, database_name

# Create the connection string
dsn = cx_Oracle.makedsn(hostname, port, service_name=database_name)
conn_str = '{}/{}@{}'.format(username, password, dsn)

# Connect to the Oracle database
conn = cx_Oracle.connect(conn_str)

# Create a cursor object
cur = conn.cursor()

# SQL query to extract data from the database
sql_query = 'SELECT * FROM my_table'

# Execute the query and load the data into the cursor
cur.execute(sql_query)

# Load the data from the cursor into a Pandas DataFrame
df = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])

# Close the cursor and database connection
cur.close()
conn.close()

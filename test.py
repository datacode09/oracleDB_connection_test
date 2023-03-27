'''
Replace username, password, hostname, port, and service_name with your Oracle database connection details. 
The cx_Oracle.connect() function will raise an exception if it fails to connect to the database, so we catch that and log the error message. 
We also catch any other exceptions that might occur during the database operations and log those as well.

The logging module is used to create a log file called db_connectivity.log in the same directory as the script. 
The log file will contain entries for successful database connections, database errors, and any other errors that occur during script execution.
The level parameter is set to logging.INFO, which means that log messages with a severity level of INFO or higher will be recorded in the log file. 
You can change this to logging.DEBUG if you want more detailed logging.


'''

import cx_Oracle
import logging

# Set up logging
logging.basicConfig(filename='db_connectivity.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Connect to Oracle database
try:
    conn = cx_Oracle.connect('username/password@hostname:port/service_name')
    logging.info('Successfully connected to Oracle database')
    # Do some database operations here
    ...
except cx_Oracle.Error as e:
    logging.error('Database error: {}'.format(str(e)))
except Exception as e:
    logging.error('Error: {}'.format(str(e)))
finally:
    # Close database connection
    try:
        conn.close()
        logging.info('Database connection closed')
    except Exception as e:
        logging.error('Error closing database connection: {}'.format(str(e)))

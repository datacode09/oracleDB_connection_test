'''
In this script, we first set up logging configuration using the logging module, with a filename for the log file and a logging level of DEBUG. We then define a list of dictionaries, with each dictionary containing the details for a different database to be tested.

We define a function test_database_connection that takes a database dictionary as input, attempts to connect to the database using cx_Oracle, logs the result, and returns a boolean indicating success or failure.

Finally, we loop over the list of databases and call the test_database_connection function for each one, logging the result and printing a message indicating success or failure.

This script logs everything including timestamps and detailed error-logging in the specified log file database_connectivity_test.log. You can modify the code to suit your needs such as changing database connection details or the log filename.





Regenerate response

'''

import cx_Oracle
import logging
import datetime

# Set up logging configuration
log_filename = 'database_connectivity_test.log'
logging.basicConfig(filename=log_filename, level=logging.DEBUG)

# Define database connection details
database_list = [
    {
        'name': 'database1',
        'username': 'username1',
        'password': 'password1',
        'dsn': 'database1_dsn'
    },
    {
        'name': 'database2',
        'username': 'username2',
        'password': 'password2',
        'dsn': 'database2_dsn'
    }
]

# Define function to test database connection
def test_database_connection(database):
    try:
        connection = cx_Oracle.connect(database['username'], database['password'], database['dsn'])
        logging.info(f"{datetime.datetime.now()} {__file__} Connected to {database['name']}.")
        connection.close()
        return True
    except cx_Oracle.Error as error:
        logging.error(f"{datetime.datetime.now()} {__file__} {database['name']}: {error}")
        return False

# Test database connections
for database in database_list:
    result = test_database_connection(database)
    if result:
        print(f"{database['name']} connection test passed.")
    else:
        print(f"{database['name']} connection test failed. See log file for details.")


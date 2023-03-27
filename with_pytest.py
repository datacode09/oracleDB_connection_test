import cx_Oracle
import logging
import os
import pytest

# Set up logging
LOG_DIRECTORY = './logs'
LOG_FILENAME = 'database-connection-test.log'

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

logging.basicConfig(filename=os.path.join(LOG_DIRECTORY, LOG_FILENAME), level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define connection details for each database
DATABASES = [
    {
        'name': 'database1',
        'username': 'user1',
        'password': 'password1',
        'dsn': 'dsn1'
    },
    {
        'name': 'database2',
        'username': 'user2',
        'password': 'password2',
        'dsn': 'dsn2'
    }
]

@pytest.mark.parametrize('database', DATABASES)
def test_database_connection(database):
    try:
        # Set up connection
        connection = cx_Oracle.connect(database['username'], database['password'], database['dsn'])

        # Log successful connection
        logging.info(f"Connected to {database['name']}")

        # Close connection
        connection.close()

    except cx_Oracle.DatabaseError as error:
        # Log detailed error
        error, = error.args
        logging.error(f"Failed to connect to {database['name']}. Error message: {error.message}, error code: {error.code}")
        pytest.fail(f"Failed to connect to {database['name']}. Error message: {error.message}, error code: {error.code}")


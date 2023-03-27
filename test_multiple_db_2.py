import cx_Oracle
import datetime

# List of Oracle database connection details
db_connections = [
    {'username': 'user1', 'password': 'password1', 'dsn': 'database1'},
    {'username': 'user2', 'password': 'password2', 'dsn': 'database2'},
    {'username': 'user3', 'password': 'password3', 'dsn': 'database3'}
]

# Set up logging
LOG_FILE = 'database_connectivity.log'
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Test database connectivity
for connection in db_connections:
    try:
        # Establish database connection
        conn = cx_Oracle.connect(connection['username'], connection['password'], connection['dsn'])
        logger.info(f"Successfully connected to {connection['dsn']}")
        conn.close()
    except cx_Oracle.Error as error:
        logger.error(f"Failed to connect to {connection['dsn']}. {error}")

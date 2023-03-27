import cx_Oracle
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime

# List of Oracle database connection details
db_connections = [
    {'username': 'user1', 'password': 'password1', 'dsn': 'database1'},
    {'username': 'user2', 'password': 'password2', 'dsn': 'database2'},
    {'username': 'user3', 'password': 'password3', 'dsn': 'database3'}
]

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set up a rotating log file handler
log_file = 'database_connectivity.log'
handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)  # Set the logging level on the handler
handler.setFormatter(formatter)
logger.addHandler(handler)

# Test database connectivity
for connection in db_connections:
    try:
        # Establish database connection
        conn = cx_Oracle.connect(connection['username'], connection['password'], connection['dsn'])
        logger.info(f"Successfully connected to {connection['dsn']}")
        conn.close()
    except cx_Oracle.Error as error:
        logger.error(f"Failed to connect to {connection['dsn']}. {error}")

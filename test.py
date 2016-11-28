"""
Description: Call mongodb connection class and use that
"""

# Application imports
from apis import MongoConn

# Initialise tinydb wrapper class and use db instance for db operations
db_obj = MongoConn(connection_obj={"DATABASE": "test", "HOST": "localhost", "PORT": 27017})
print db_obj.list_document()
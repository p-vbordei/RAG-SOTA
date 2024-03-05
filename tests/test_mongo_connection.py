# RAG-SOTA/tests/test_mongo_connection.py

import unittest
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

class TestMongoDBConnection(unittest.TestCase):
    def test_connection(self):
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')
        except ServerSelectionTimeoutError:
            self.fail("MongoDB connection failed or timed out.")

if __name__ == '__main__':
    unittest.main()

# in project root
# python -m unittest discover -s tests

### end ###
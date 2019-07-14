import unittest
from database.connection.mysql_connection import get_connection

class TestConnection(unittest.TestCase):
    def test_connection(self):
        connection = get_connection()
        self.assertIsNotNone(connection)


if __name__ == '__main__':
    unittest.main()

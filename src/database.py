import aiosqlite 

class Database:
    def __init__(self):
        self.connection = None


    async def get_connection(self):
        """
        Returns:
            Database connection
        """
        if self.connection is None:
            self.connection = await aiosqlite.connect("../databases/exp.db")
            return self.connection


    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

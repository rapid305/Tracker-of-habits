from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConfig:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", 5432))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASS")
        self.database = os.getenv("DB_NAME")

        if not all([self.user, self.password, self.database]):
            raise ValueError("Database credentials are not fully set in .env file.")

    def get_async_connection_string(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    def get_sync_connection_string(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

database_config = DatabaseConfig()


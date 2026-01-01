# PATH: db/config.py

# 🔴 ONLY THIS FILE CHANGES PER ENV (local / aws / prod)

DB_TYPE = "sqlite"   # sqlite | postgres | mysql

SQLITE_DB_PATH = "agentic_ai.db"

# Example for later (DO NOT USE NOW)
POSTGRES = {
    "host": "localhost",
    "port": 5432,
    "db": "agentic_ai",
    "user": "postgres",
    "password": "password"
}

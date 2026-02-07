import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # Project1/
DB_PATH = BASE_DIR / "backend" / "app.db"

SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"
SEED_PATH = BASE_DIR / "database" / "seed.sql"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Create tables
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    cur.executescript(f.read())

# Seed data
with open(SEED_PATH, "r", encoding="utf-8") as f:
    cur.executescript(f.read())

conn.commit()
conn.close()

print("✅ Database created and seeded successfully")

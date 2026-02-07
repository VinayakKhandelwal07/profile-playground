import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "app.db"

print("Using DB:", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

tables = ["profile", "skills", "projects", "project_skills"]

for t in tables:
    try:
        rows = cur.execute(f"SELECT * FROM {t}").fetchall()
        print(f"\nTABLE: {t}")
        print(rows)
    except Exception as e:
        print(f"\nTABLE: {t} ERROR:", e)

conn.close()

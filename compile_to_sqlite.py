import os
import json
import sqlite3

cve_directory = "cvelistV5-main/cves"
db_file = "cve_data.db"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cve_data (
        cve_id TEXT PRIMARY KEY,
        json_data TEXT
    )
''')

for root, dirs, files in os.walk(cve_directory):
    for file in files:
        if file.startswith("CVE-") and file.endswith(".json"):
            file_path = os.path.join(root, file)
            cve_id = os.path.splitext(file)[0]
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                json_data = json.dumps(data)
                cursor.execute('''
                    INSERT OR REPLACE INTO cve_data (cve_id, json_data)
                    VALUES (?, ?)
                ''', (cve_id, json_data))

conn.commit()
conn.close()

print(f"Database Created{db_file}")

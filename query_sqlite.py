import sqlite3
import json

conn = sqlite3.connect("cve_data.db")
cursor = conn.cursor()
cve_id = "CVE-2022-47966"

cursor.execute("SELECT json_data FROM cve_data WHERE cve_id = ?", (cve_id,))
result = cursor.fetchone()

if result:
    json_data = json.loads(result[0])
    print(json.dumps(json_data, indent=4))
else:
    print(f"{cve_id} not found")

conn.close()

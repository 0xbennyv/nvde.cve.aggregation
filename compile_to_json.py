import os
import json

cve_directory = "cvelistV5-main/cves"

cve_data = {}
for root, dirs, files in os.walk(cve_directory):
    for file in files:
        if file.startswith("CVE-") and file.endswith(".json"):
            file_path = os.path.join(root, file)
            cve_id = os.path.splitext(file)[0]
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                cve_data[cve_id] = data

output_file = "compiled_cve_data.json"
with open(output_file, 'w', encoding='utf-8') as out_file:
    json.dump(cve_data, out_file, indent=4)

print(f"Compiled data written to {output_file}")

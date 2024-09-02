import os
import json

# Path to the cve directory
cve_directory = "cvelistV5-main/cves"  # Update this path if needed

# Initialize an empty dictionary to hold all the CVEs
cve_data = {}

# Traverse through the cve directory recursively
for root, dirs, files in os.walk(cve_directory):
    for file in files:
        if file.endswith(".json"):
            # Construct the full path to the json file
            file_path = os.path.join(root, file)
            # Get the file name without the extension (e.g., "CVE-1999-0001")
            cve_id = os.path.splitext(file)[0]
            # Open and read the json file
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                # Add the data to the dictionary with the CVE ID as the key
                cve_data[cve_id] = data

# Output file
output_file = "compiled_cve_data.json"

# Write the compiled data to a single JSON file
with open(output_file, 'w', encoding='utf-8') as out_file:
    json.dump(cve_data, out_file, indent=4)

print(f"Compiled data written to {output_file}")

import requests
from datetime import datetime, timedelta
import os
import json

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

data = []
pages=[0,1]
for p in pages:
    response = requests.get(f"https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page={p}&size=1000")
    response.raise_for_status()
    data.extend(response.json())

tw_time = datetime.now() + timedelta(hours=8)
output_file = os.path.join(output_dir, f"{tw_time.strftime('%Y_%m_%d_%H_%M_%S')}.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"已下載並存到 {output_file}")

files = os.listdir("data")
print(files)
files.sort(reverse=True)

with open(f"index.json", "w", encoding="utf-8") as f:
    json.dump(files[:576], f, ensure_ascii=False, indent=4)
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
files.sort(reverse=True)
"""
# 最近一小時的所有資料
recent_hour = []
# 每30分鐘一筆資料
sampled_files = []

now = datetime.now() + timedelta(hours=8)
one_hour_ago = now - timedelta(hours=1)
two_days_ago = now - timedelta(hours=48)

for file in files:
    try:
        file_time = datetime.strptime(file.split(".")[0], "%Y_%m_%d_%H_%M_%S")
        
        # 最近一小時的資料全部保留
        if file_time > one_hour_ago:
            recent_hour.append(file)
            continue
            
        # 超過一小時但在48小時內的資料每30分鐘取樣一次
        if file_time > two_days_ago:
            if file_time.minute in [0, 30]:
                sampled_files.append(file)
    except:
        continue

result_files = recent_hour + sampled_files

print(f"result_files: {result_files}")
"""

result_files = files
with open(f"index.json", "w", encoding="utf-8") as f:
    json.dump(result_files, f, ensure_ascii=False, indent=4)

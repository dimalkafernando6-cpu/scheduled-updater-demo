from datetime import datetime
from zoneinfo import ZoneInfo

# Fetch current time using Python's built-in zoneinfo
tz = ZoneInfo("Asia/Colombo")
current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')

# Update timestamp in a log file
with open("last_updated.txt", "w") as f:
    f.write(f"Last Pipeline Execution: {current_time}\n")

print(f"Successfully updated timestamp: {current_time}")

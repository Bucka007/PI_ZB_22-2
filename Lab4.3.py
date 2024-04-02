import time
from datetime import datetime

for i in range(5):
    current_time = datetime.now()
    print(f"Текущее время: {current_time.strftime('%H:%M:%S')}")
    time.sleep(1)
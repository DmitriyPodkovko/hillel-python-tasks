import requests

import time

time1 = requests.get('https://api.github.com/').elapsed.total_seconds()

time2 = requests.get("http://google.com").elapsed.total_seconds()


print(time1)

print(time2)


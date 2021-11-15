# from urllib.parse import urlencode
# from urllib.request import urlopen, Request
# from urllib.error import HTTPError
# from json import loads

# api_key = "jmgkkDkFTiMp55iRcVGCRiTU5OUg7FqaQfKYDOECUXI.LPVbfXhH9bqcJfzqsyZ-4" # APIアクセストークン

# url = "https://api.nature.global/1/devices/"

# headers = {
#     "accept" :"application/json",
#     "Authorization" :"Bearer " + api_key,
# }

# request = Request(url, headers=headers)

# try:
#   with urlopen(request) as response:
#     data_byte = response.read()
#     data= loads(data_byte)
# except HTTPError as e:
#     print(e)

# device_info = data[0]["newest_events"]

# print("温度 : "   + str(device_info["te"]["val"]) + "度")
# print("湿度 : "   + str(device_info["hu"]["val"]) + "%")
# print("明るさは : " + str(device_info["il"]["val"]) + "度")
# print("最後に検知したのは" + str(device_info["mo"]["created_at"]) + "です。")


from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import loads
import datetime

api_key = "jmgkkDkFTiMp55iRcVGCRiTU5OUg7FqaQfKYDOECUXI.LPVbfXhH9bqcJfzqsyZ-4" # APIアクセストークン

url = "https://api.nature.global/1/devices/"

headers = {
    "accept" :"application/json",
    "Authorization" :"Bearer " + api_key,
}

request = Request(url, headers=headers)

try:
  with urlopen(request) as response:
    data_byte = response.read()
    data= loads(data_byte)
except HTTPError as e:
    print(e)

device_info = data[0]["newest_events"]

print("温度 : "   + str(device_info["te"]["val"]) + "度")
print("湿度 : "   + str(device_info["hu"]["val"]) + "%")
print("明るさは : " + str(device_info["il"]["val"]) + "度")

detect_date_str = str(device_info["mo"]["created_at"]).split("T")[0].split("-")
detect_time_str = str(device_info["mo"]["created_at"]).split("T")[1].split("Z")[0].split(":")

detect_date = [int(n) for n in detect_date_str]
detect_time = [int(n) for n in detect_time_str]

date = datetime.datetime(year=detect_date[0], month=detect_date[1], day=detect_date[2], hour=detect_time[0], minute=detect_time[1], second=detect_time[2])
now = datetime.datetime.now()
difference_time = now - date

if difference_time.days > 0:
  print("人感センサー :{}日前".format(difference_time.days))
elif difference_time.total_seconds > 3600:
  print("人感センサー : {}時間前".format(difference_time.total_seconds/3600))
else:
  print("人感センサー :{}分前".format(int(difference_time.total_seconds()/60)))

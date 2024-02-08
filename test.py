import requests

BASE = "http://127.0.0.1:5000/"

# Just to Test Patch
# data = [{"likes": 78, "name": "Joe", "views": 100000}, 
#         {"likes": 1000, "name": "Roger", "views": 200000},
#         {"likes": 35, "name": "Tim", "views": 80}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()
# response = requests.get(BASE + "video/2")
# print(response.json())

response = requests.patch(BASE + "video/2", {"views":99, "likes":101})
print(response.json())

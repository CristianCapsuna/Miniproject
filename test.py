import json

# with open('Orders.txt') as f:
#     for x in f.readlines():
#         print(x)
#         test = json.loads(x)
# print('HI')

json1 = json.loads('{"customer_name": "John","customer_address": "London","customer_phone": "0789887334","courier": 2,"status": "preparing"}')
json2 = json.loads('{"customer_name": "John","customer_address": "London","customer_phone": "0789887334","courier": 2,"status": "preparing"}')
print(json1 == json2)
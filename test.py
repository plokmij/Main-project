import json
from pprint import pprint
follower_data = []
with open('data.json') as data_file:       
	for line in data_file:
		follower_data.append(json.loads(line))

print(follower_data)

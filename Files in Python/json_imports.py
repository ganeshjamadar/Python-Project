import json

with open('friends_json.txt','r') as json_file:
    json_file_content = json.load(json_file)

print(json_file_content['friends'][0])


cars = [
    {'make': 'Ford','model': 'Fiesta'},
    {'make': 'Ford','model': 'Focus'},
]

with open('cars_json.txt', 'w') as json_output_file:
     json.dump(cars,json_output_file)

my_json_stirng = '[{"firstName": "Ganesh","lastName": "Jamadar"}]'

fullName = json.loads(my_json_stirng)

print(fullName[0]['firstName'] + ' ' + fullName[0]['lastName'])
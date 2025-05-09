import json


data={123:{"name":"John Doe",
            "age":30,
            "address":"123 Main St",
            "phone":"555-1234",
            "email":"ewfe"},
            124:{"name":"Jane Smith",
                 "age":28,
                 "address":"456 Elm St",
                 "phone":"555-5678",
                 "email":"ddsvsd"}}


with open('mydatae.json', 'w') as json_file:
    obj=json.dump(data, json_file, indent=4)

"""with open('mydatae.json', 'r') as json_file:
    data=json.load(json_file)
    print(data)
print(data["123"]["name"])"""

dataFile=open('mydatae.json', 'r')

dataInfo=json.load(dataFile)

print(dataInfo)

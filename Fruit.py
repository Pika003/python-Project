# Fruit Nutritions details using API
import requests
import json
a = input("Enter a fruit name: ")
response_API = requests.get('https://www.fruityvice.com/api/fruit/'+a)
data = response_API.text
parse_json = json.loads(data)
fruit_name = parse_json['name']
fruit_details = parse_json['nutritions']
print("\nDetails of ",fruit_name)
print("\ncalories :",fruit_details["calories"])
print("fat :",fruit_details["fat"])
print("sugar :",fruit_details["sugar"])
print("carbohydrates :",fruit_details["carbohydrates"])
print("protein :",fruit_details["protein"])
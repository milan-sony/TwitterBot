import requests
import keys

categories = {'age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beautybest', 'birthday', 'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success'}

# In Python, list(s) is a built-in function that converts an iterable (e.g. a set, tuple, or string) to a list
categorylist = list(categories)
category = categorylist[0]

api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
response = requests.get(api_url, headers={'X-Api-Key': f'{keys.API_Ninjas}'})

if response.status_code != 200:
  print("Error: ", response.status_code, response.text)
else:
  quote_json = response.json()
  quote = quote_json[0]['quote']
  author = quote_json[0]['author']
  category_data = quote_json[0]['category']
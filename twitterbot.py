import requests
import tweepy
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
import os

def configure():
  load_dotenv()

# function to get quotes from API Ninjas
def getquotes():
  configure()
  categories = {'age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beautybest', 'birthday', 'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success'}
  # In Python, list(s) is a built-in function that converts an iterable (e.g. a set, tuple, or string) to a list
  categorylist = list(categories)
  category = categorylist[0]

  QuoteAPI_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
  response = requests.get(QuoteAPI_url, headers={'X-Api-Key':os.getenv('API_Ninjas')})

  if response.status_code != 200:
    error_status = response.status_code, response.text
    print("QuoteAPI authentication Failed")
    print("Error: ",error_status)
    error_message = "Something went wrong with the authentication of QuoteAPI. Error: "+str(error_status)
    sendemail(error_message)
  else:
    print("QuoteAPI authentication is OK")
    quote_json = response.json()
    quote = quote_json[0]['quote']
    author = quote_json[0]['author']
    category_data = quote_json[0]['category']
    print("Quote is fetched from JSON response")
    return(category_data, quote, author)

# function to tweet posts on twitter
def posttweet():
  configure()
  category_data, quote, author = getquotes()
  # Authenticate to Twitter
  authenticator = tweepy.OAuthHandler(os.getenv('API_Key'), os.getenv('API_Key_Secret'))
  authenticator.set_access_token(os.getenv('Access_Token'), os.getenv('Access_Token_Secret'))
  #  credentials are tested using verify_credentials().
  twitter_api_authenticate = tweepy.API(authenticator)
  try:
    twitter_api_authenticate.verify_credentials()
    print("Twitter API authentication is OK")
    tweet = "#dailyquotes"+" "+"#"+category_data+" "+quote+" - "+author
    print("Quote is added to the tweet")
    print(tweet)
    # Create Twitter API object
    api = tweepy.API(authenticator, wait_on_rate_limit=True)
    try:
      api.update_status(tweet)
      print("Tweet posted")
    except tweepy.Forbidden as e:
      print(e)
      error_msg = str(e)
      sendemail(error_msg)
  except:
    print("Error: Twitter API Authentication Failed")
    error_message = "Error: Twitter API Authentication Failed"
    sendemail(error_message)

# function to send Email
def sendemail(errormessage):
  configure()
  email_sender = os.getenv('email_sender')
  email_password = os.getenv('email_password')
  email_receiver = os.getenv('email_receiver')
  subject = '🚨 Alert from TwitterQuoteBot🤖'
  email_content = str(errormessage)

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = subject
  em.set_content(email_content)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', '465', context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print('Email Sent')
    exit()

getquotes()
posttweet()
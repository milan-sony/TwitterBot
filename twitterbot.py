import requests
import tweepy
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
import os

def configure():
  load_dotenv()

# function to send Email
def send_email(errormessage):
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


def getquotes():
  configure()
  # Getting quote from the URL
  quote_url = 'https://api.quotable.io/random'
  response = requests.get(quote_url)

  if response.status_code != 200 or response.status_code == 429:
    error_status = response.status_code, response.text
    print("Quote not found")
    print("Error: ", error_status)
    quote_error_message = "Quote not found "+str(error_status)
    send_email(quote_error_message)
  else:
    print("Quote found")
    quote_json = response.json()
    quote = quote_json['content']
    author = quote_json['author']
    return(quote, author)

# function to tweet posts on twitter
def posttweet():
  configure()
  quote, author = getquotes()
  # Authenticate to Twitter
  authenticator = tweepy.OAuthHandler(os.getenv('API_Key'), os.getenv('API_Key_Secret'))
  authenticator.set_access_token(os.getenv('Access_Token'), os.getenv('Access_Token_Secret'))
  #  credentials are tested using verify_credentials().
  twitter_api_authenticate = tweepy.API(authenticator)
  try:
    twitter_api_authenticate.verify_credentials()
    print("Twitter API authentication is OK")
    tweet = "#dailyquotes"+" "+quote+" - "+author
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
      send_email(error_msg)
  except:
    print("Error: Twitter API Authentication Failed")
    error_message = "Error: Twitter API Authentication Failed"
    send_email(error_message)

posttweet()

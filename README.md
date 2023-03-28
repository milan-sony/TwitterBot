<p align="center">
    <img width="100" src="icon/icon.png" alt="Icon">
</p>

# TwitterBot

A bot🤖 that tweet quotes daily on Twitter <a href = "https://twitter.com/tweetwithquotes">tweetwithquotes</a>

## Prerequisites

<a href = "https://github.com/lukePeavey/quotable">Quote API</a>

<a href = "https://developer.twitter.com/en/docs/platform-overview">Twitter API</a>

For sending an Email, you have to make necessary changes in your gmail account (refer youtube, Keyword: How to send a mail in python)

## Read documentation about

- <a href = "https://developer.twitter.com/en/docs/twitter-api">Twitter API</a>
- <a href = "https://docs.tweepy.org/en/latest/">Tweepy</a>

## Libraries used

- `requests`
- `tweepy`
- `dotenv`

## Run locally

You will need to install Python on you system, head over to https://www.python.org/downloads/ to download python.
(Dont Forget to tick `Add Python to PATH` while installing Python)

Once you have downloaded Python on your system, 
run the following command inside your terminal (only if your system is git enabled, otherwise download the zip file and extract it)

```bash
  git clone https://github.com/milan-sony/twitterbot.git
```

Then go to the project folder

```bash
  cd twitterbot
```

(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```

Activate the virtual environment

```bash
  venv/Scripts/activate
```

If error occurs when activating virtual environment, run the following command

```bash
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Then Install the dependencies needed for this project

```bash
  pip install -r requirements.txt
```

Now run the script

```bash
  python twitterbot.py
```

## Working

This bot works in such a way that

1st it will send a request to the Quote API from <a href = "https://api-ninjas.com/api/quotes">API Ninjas</a> and it will get the JSON response back, then the quote is fetched from the JSON response and this response is posted on twitter. If any error messages occured or if the authentication from Quote API and twitter API failed, it will send an Email to the given Email Id.

## Points to be noted

You can use different API's for this project

Actually it's not 100% accurate, there are some faults while running the program (If any bug occurs or not running properly, exit the code by clicking `ctrl + c` in the terminal and run again `python twitterbot.py`)

## Future updates

- Try to add more features to the bot

#! python3.7
# bonprix.py - Imports comments from products into Excel spreadsheet"
import requests, sys, bs4



url = "https://www.bonprix.ro/style/fusta-creion-121730795/?catalogueNumber=942227&type=image&return=ref"
response = requests.get(url)

try:
    response.raise_for_status()
    text = response.text
    print(text[:3000])
    soup = bs4.Beautifulsoup(text, 'html.parser')
    tags = soup.select(print
except Exception as exc:
    print('There was a problem: ', exc)


'''for tweet in public_tweets:
    print (tweet.text)
    u=tweet.text
    u=u.encode('unicode-escape').decode('utf-8')'''

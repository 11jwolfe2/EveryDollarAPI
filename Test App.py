import requests as requests
from bs4 import BeautifulSoup
import urllib as urllib
import http as http
import pickle as pickle
import json as json

site = "https://everydollar.id.ramseysolutions.net/sign-in?scope=openid%20profile%20email&response_type=code&client_id=everydollar&redirect_uri=https%3A%2F%2Fwww.everydollar.com%2Fapp%2Fauth&state=eyJmcm9tIjp7InBhdGhuYW1lIjoiL2J1ZGdldCJ9fQ&code_challenge=OTMnsDl29IHFOdd4MzyR93iAslsKO_O0Ea5fnBFRWlk&code_challenge_method=S256"
signin = "https://everydollar.id.ramseysolutions.net/sign-in?scope=openid%20profile%20email&response_type=code&client_id=everydollar&redirect_uri=https%3A%2F%2Fwww.everydollar.com%2Fapp%2Fauth&state=eyJmcm9tIjp7InBhdGhuYW1lIjoiL2J1ZGdldCJ9fQ&code_challenge=OTMnsDl29IHFOdd4MzyR93iAslsKO_O0Ea5fnBFRWlk&code_challenge_method=S256"

headerM = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-length': '217',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://everydollar.id.ramseysolutions.net',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

with requests.Session() as session:
    r = session.get(signin)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
    tokenEncode = urllib.parse.quote(token, safe='')
    strategy = 'name_password'
    service = 'user_sso_mfa'
    email = 'jwolfe72@gmail.com'
    #email = urllib.parse.quote(email, safe='')
    password = '4ehO5$ShCan3*L8X'
    #password = urllib.parse.quote(password, safe='*')

    payload = {
        'authenticity_token': token,
        'strategy': strategy,
        'service': service,
        'email': email,
        'password': password
    }

    #payload = 'authenticity_token=' + token + '&' + 'strategy=' + strategy + '&' + 'service=' + service + '&' + 'email=' + email + '&' + 'password=' + password
    r = session.post(signin, data=payload)
    r = session.get("https://www.everydollar.com/app/auth?client_id=everydollar&code=FskE0gqTxdIbx8aXIVICrSuriR4&scope=openid%20profile%20email&state=eyJmcm9tIjp7InBhdGhuYW1lIjoiL2J1ZGdldCJ9fQ", headers=headerM)
    print(r.content)
    r = session.get("https://api.everydollar.com/user/")
    print(r.content)
    r = session.get("https://www.everydollar.com/app/budget")
    print(r.content)
    r = session.get("https://api.everydollar.com/budget/budgets/d6dbe17c-8481-4269-b157-37256804995b")
    print(r.content)
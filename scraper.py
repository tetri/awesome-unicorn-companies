import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.cbinsights.com/research-unicorn-companies')

soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    if (len(tds) == 0):
        continue

    company = tds[0].text
    valuation = tds[1].text
    date_joined = tds[2].text
    country = tds[3].text
    city = tds[4].text
    industry = tds[5].text
    select_investors = tds[6].text
    
    print(f'* {company} {valuation}B {date_joined} {city} @ {country} {industry} {select_investors}')

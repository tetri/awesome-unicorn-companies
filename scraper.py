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

    link = tds[0].find('a').get('href')

    page2 = requests.get(link)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    header_link = soup2.select('a[class*="Header_link_"]')
    
    sitelink = ''
    if (len(header_link) > 0):
        real_link = header_link[0]
        url = real_link.get('href')
        site = real_link.text

        sitelink = f'[{site}]({url}) - ' 

    description = soup2.select('p[data-test="description"]')
    if (len(description) > 0):
        description = description[0].text
    else:
        description = ''

    valuation = tds[1].text
    date_joined = tds[2].text
    country = tds[3].text
    city = tds[4].text
    industry = tds[5].text
    select_investors = tds[6].text
    
    print(f'* **{company}** - {sitelink}{description}')
    print(f'  * Valuation: **{valuation}B**')
    print(f'  * Date joined: **{date_joined}**')
    print(f'  * Location: **{city} @ {country}**')
    print(f'  * Industry: **{industry}**')
    print(f'  * Select investors: **{select_investors}**')

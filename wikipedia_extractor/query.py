import urllib.request as u
import wikipedia as w
from bs4 import BeautifulSoup as b

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita'
req = u.urlopen(url)
article = req.read().decode()

with open('GDP_PPP_Ranking.html', 'w') as fo:
    fo.write(article)

data_in = open('GDP_PPP_Ranking.html', 'r')
soup = b(article, 'html.parser')
tables = soup.find_all('table', class_='sortable')
count = 0
for table in tables:
    ths = table.find_all('th')
    headings = [th.text.strip() for th in ths]
    if headings[:3] == ['Rank', 'Country/Territory', 'Int$']:
        break

table = tables[0]
rank_dic = {}

for row in table.find_all('tr'):
    data = row.find_all('td')
    if data:
        if len(data) == 3:
            rank, c_t, ppp = [datum.text.strip() for datum in data[:3]]
            rank_dic[(rank, c_t)] = ppp
        else: 
            break
print('--------------------------------------------------------------------------------')
for key in rank_dic:
    pr_str = '|'
    rank_start_pos = 6/2 - int(len(key[0])/2)
    ptr = 0
    while ptr <= rank_start_pos:
        pr_str += ' '
        ptr += 1
    pr_str += key[0]
    ptr += len(key[0])
    while ptr <= 7:
        pr_str += ' '
        ptr += 1
    pr_str += '|'
    print(pr_str)

print('--------------------------------------------------------------------------------')
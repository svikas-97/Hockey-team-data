import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

l_url = []
l_dct = []
for num in range(1,25):
    l_url.append(f'https://www.scrapethissite.com/pages/forms/?page_num={num}')
for url in l_url:
    print(url)
    r = requests.get(url)
    soup = bs(r.content, 'html5lib')

    table_soup = soup.find('table', class_='table')
    
    rows = table_soup.find_all('tr', class_='team')
    for row in rows:
        team_name = row.find('td', class_='name').text.strip()
        match_year = row.find('td', class_='year').text.strip()
        wins = row.find('td', class_='wins').text.strip()
        losses = row.find('td', class_='losses').text.strip()
        ot_losses = row.find('td', class_='ot-losses').text.strip()
        win_percentage = row.find('td', class_='pct').text.strip()
        goals_for = row.find('td', class_='gf').text.strip()
        goals_against = row.find('td', class_='ga').text.strip()
        diff = row.find('td', class_='diff').text.strip()

        dct = {
            'Team Name':team_name,
            'Year':match_year,
            'Wins':wins,
            'Losses':losses,
            'OT Losses':ot_losses,
            'Win %':win_percentage,
            'Goals For':goals_for,
            "goals Against":goals_against,
            '+/-':diff
        }
        l_dct.append(dct)

df = pd.DataFrame(l_dct)
print(df)
df.to_csv('hockey team scraped data.csv', index=False)
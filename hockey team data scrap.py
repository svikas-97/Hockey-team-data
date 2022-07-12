import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


team_name_list = []
year_list = []
wins_list = []
losses_list = []
ot_loss_list = []
win_percentage_list = []
goals_for_list = []
goals_against_list = []
diff_list = []


url_list = []
D = {}
for i in range(1,25):
    full_url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}'
    url_list.append(full_url)
for idx, val in enumerate(url_list):
    r1 = requests.get(val)
    soup1 = bs(r1.content)

    tag_team1 = soup1.find_all('td', class_='name')
    team_name1 = [tag1.get_text().strip() for tag1 in tag_team1]
    team_name_list.append(team_name1)
    
    tag_year1 = soup1.find_all('td', class_='year')
    year1 = [tag1.get_text().strip() for tag1 in tag_year1]
    year_list.append(year1)
    
    tag_wins1 = soup1.find_all('td', class_='wins')
    wins1 = [tag1.get_text().strip() for tag1 in tag_wins1]
    wins_list.append(wins1)
    
    tag_losses1 = soup1.find_all('td', class_='losses')
    losses1 = [tag1.get_text().strip() for tag1 in tag_losses1]
    losses_list.append(losses1)
    
    tag_win_percentage1 = soup1.find_all('td', class_=['pct text-success', 'pct text-danger'])
    win_percentage1 = [tag1.get_text().strip() for tag1 in tag_win_percentage1]
    win_percentage_list.append(win_percentage1)
    
    tag_goalsfor1 = soup1.find_all('td', class_='gf')
    goals_for1 = [tag1.get_text().strip() for tag1 in tag_goalsfor1]
    goals_for_list.append(goals_for1)
    
    tag_goalsagainst1 = soup1.find_all('td', class_='ga')
    goals_against1 = [tag1.get_text().strip() for tag1 in tag_goalsagainst1]
    goals_against_list.append(goals_against1)
    
    tag_diff1 = soup1.find_all('td', class_=['diff text-success', 'diff text-danger'])
    difference1 = [tag1.get_text().strip() for tag1 in tag_diff1]
    diff_list.append(difference1)
    
    tag_ot_loss1 = soup1.find_all('td', class_='ot-losses')
    ot_loss1 = [tag1.get_text().strip().replace('', '0') for tag1 in tag_ot_loss1]
    ot_loss_list.append(ot_loss1)
    
    
team_name_list = team_name_list[0]+team_name_list[1]+team_name_list[2]+team_name_list[3]+team_name_list[4]+team_name_list[5]+team_name_list[6]+team_name_list[7]+team_name_list[8]+team_name_list[9]+team_name_list[10]+team_name_list[11]+team_name_list[12]+team_name_list[13]+team_name_list[14]+team_name_list[15]+team_name_list[16]+team_name_list[17]+team_name_list[18]+team_name_list[19]+team_name_list[20]+team_name_list[21]+team_name_list[22]+team_name_list[23]

year_list = year_list[0]+year_list[1]+year_list[2]+year_list[3]+year_list[4]+year_list[5]+year_list[6]+year_list[7]+year_list[8]+year_list[9]+year_list[10]+year_list[11]+year_list[12]+year_list[13]+year_list[14]+year_list[15]+year_list[16]+year_list[17]+year_list[18]+year_list[19]+year_list[20]+year_list[21]+year_list[22]+year_list[23]

wins_list = wins_list[0]+wins_list[1]+wins_list[2]+wins_list[3]+wins_list[4]+wins_list[5]+wins_list[6]+wins_list[7]+wins_list[8]+wins_list[9]+wins_list[10]+wins_list[11]+wins_list[12]+wins_list[13]+wins_list[14]+wins_list[15]+wins_list[16]+wins_list[17]+wins_list[18]+wins_list[19]+wins_list[20]+wins_list[21]+wins_list[22]+wins_list[23]

losses_list = losses_list[0]+losses_list[1]+losses_list[2]+losses_list[3]+losses_list[4]+losses_list[5]+losses_list[6]+losses_list[7]+losses_list[8]+losses_list[9]+losses_list[10]+losses_list[11]+losses_list[12]+losses_list[13]+losses_list[14]+losses_list[15]+losses_list[16]+losses_list[17]+losses_list[18]+losses_list[19]+losses_list[20]+losses_list[21]+losses_list[22]+losses_list[23]

ot_loss_list = ot_loss_list[0]+ot_loss_list[1]+ot_loss_list[2]+ot_loss_list[3]+ot_loss_list[4]+ot_loss_list[5]+ot_loss_list[6]+ot_loss_list[7]+ot_loss_list[8]+ot_loss_list[9]+ot_loss_list[10]+ot_loss_list[11]+ot_loss_list[12]+ot_loss_list[13]+ot_loss_list[14]+ot_loss_list[15]+ot_loss_list[16]+ot_loss_list[17]+ot_loss_list[18]+ot_loss_list[19]+ot_loss_list[20]+ot_loss_list[21]+ot_loss_list[22]+ot_loss_list[23]

win_percentage_list = win_percentage_list[0]+win_percentage_list[1]+win_percentage_list[2]+win_percentage_list[3]+win_percentage_list[4]+win_percentage_list[5]+win_percentage_list[6]+win_percentage_list[7]+win_percentage_list[8]+win_percentage_list[9]+win_percentage_list[10]+win_percentage_list[11]+win_percentage_list[12]+win_percentage_list[13]+win_percentage_list[14]+win_percentage_list[15]+win_percentage_list[16]+win_percentage_list[17]+win_percentage_list[18]+win_percentage_list[19]+win_percentage_list[20]+win_percentage_list[21]+win_percentage_list[22]+win_percentage_list[23]

goals_for_list = goals_for_list[0]+goals_for_list[1]+goals_for_list[2]+goals_for_list[3]+goals_for_list[4]+goals_for_list[5]+goals_for_list[6]+goals_for_list[7]+goals_for_list[8]+goals_for_list[9]+goals_for_list[10]+goals_for_list[11]+goals_for_list[12]+goals_for_list[13]+goals_for_list[14]+goals_for_list[15]+goals_for_list[16]+goals_for_list[17]+goals_for_list[18]+goals_for_list[19]+goals_for_list[20]+goals_for_list[21]+goals_for_list[22]+goals_for_list[23]

goals_against_list = goals_against_list[0]+goals_against_list[1]+goals_against_list[2]+goals_against_list[3]+goals_against_list[4]+goals_against_list[5]+goals_against_list[6]+goals_against_list[7]+goals_against_list[8]+goals_against_list[9]+goals_against_list[10]+goals_against_list[11]+goals_against_list[12]+goals_against_list[13]+goals_against_list[14]+goals_against_list[15]+goals_against_list[16]+goals_against_list[17]+goals_against_list[18]+goals_against_list[19]+goals_against_list[20]+goals_against_list[21]+goals_against_list[22]+goals_against_list[23]

diff_list = diff_list[0]+diff_list[1]+diff_list[2]+diff_list[3]+diff_list[4]+diff_list[5]+diff_list[6]+diff_list[7]+diff_list[8]+diff_list[9]+diff_list[10]+diff_list[11]+diff_list[12]+diff_list[13]+diff_list[14]+diff_list[15]+diff_list[16]+diff_list[17]+diff_list[18]+diff_list[19]+diff_list[20]+diff_list[21]+diff_list[22]+diff_list[23]


D['Team Name'] = team_name_list
D['Year'] = year_list
D['Wins'] = wins_list
D['Losses'] = losses_list
D['OT Losses'] = ot_loss_list
D['Win %'] = win_percentage_list
D['Goals For'] = goals_for_list
D['Goals Against'] = goals_against_list
D['+/-'] = diff_list


data_frame = pd.DataFrame(D)
data_frame.index = data_frame.index+1


data_frame['Year'] = pd.to_numeric(data_frame['Year'])
data_frame['Wins'] = pd.to_numeric(data_frame['Wins'])
data_frame['Losses'] = pd.to_numeric(data_frame['Losses'])
data_frame['OT Losses'] = pd.to_numeric(data_frame['OT Losses'])
data_frame['Win %'] = pd.to_numeric(data_frame['Win %'])
data_frame['Goals For'] = pd.to_numeric(data_frame['Goals For'])
data_frame['Goals Against'] = pd.to_numeric(data_frame['Goals Against'])
data_frame['+/-'] = pd.to_numeric(data_frame['+/-'])


data_frame.to_csv('Hockey teams data.csv')


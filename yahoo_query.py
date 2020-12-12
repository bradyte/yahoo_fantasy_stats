import json
import pandas as pd
from yahoo_oauth import OAuth2

BASE_URI = 'https://fantasysports.yahooapis.com/fantasy/v2/'


file_path = 'json/oauth2.json'  # location of oauth2 json file


oauth2_token = OAuth2(None, None, from_file = file_path)
if not oauth2_token.token_is_valid():
    oauth2_token.refresh_access_token()

"""
function - json_query
desc -
input - query url
output - result from query in raw JSON format
"""
def json_query(oauth2_token, url):
    url = url + '?format=json'
    response = oauth2_token.session.get(url)
    json_data = json.loads(str(response.content, 'utf-8'))
    return json_data

url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/399.l.228404/teams'

data = json_query(oauth2_token, url)
league_settings = data["fantasy_content"]["league"][0]

league_overview = data["fantasy_content"]["league"][1]["teams"]

team_overview = league_overview["0"]["team"][0]

tmp = team_overview
d = {}

for i in range(len(tmp)):
    if type(tmp[i]) is dict:
        d.update(tmp[i])

        
# df = pd.DataFrame(data=d)

# count = league_overview["count"]

# items = league_overview["0"]["team"]
# for item in items:
#     print("{} \n".format(item))

# for i in range(count):
#     idx = str(i)
#     items = league_overview["0"]["team"][0]
#     print(len(items))
    

print(json.dumps(d, indent=4))

with open('data.json', 'w') as outfile:
    json.dump(d, outfile, indent=4)


    
# def getLeagueSettings():
#     url         = BASE_URI + 'leagues;league_keys=' \
#                 + str(game_key) + '.l.' + str(228404) + '/settings?format=json'

#     jsondata = jsonQuery(url)
    
    

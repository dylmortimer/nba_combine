from flask import Flask, jsonify, request
import pandas as pd
import requests

API_BASE = 'https://stats.nba.com/stats/'

url = 'draftcombinestats'

def doit(start_season):

  df = pd.DataFrame()
  print('hello')

  for i in range(start_season, 2024):
    print(i)
    parameters = {'LeagueID': '00', 'SeasonYear': i}
    proxies = {"https":"<same postman proxy>"}
    stats_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
        'Referer': 'https://stats.nba.com/',
        'Host': 'stats.nba.com'
    }
    nba_response = requests.get(url=API_BASE+url, params=parameters, headers = stats_headers)

    data = nba_response.json()

    headers = data['resultSets'][0]['headers']

    rows = data['resultSets'][0]['rowSet']

    df = pd.concat([df,pd.DataFrame(rows, columns=headers)])

  return (df)

if __name__ == '__main__':
    df_csv = doit(2021)
    df_csv.to_csv('nba_combine.csv')
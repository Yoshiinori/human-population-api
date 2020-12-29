from bs4 import BeautifulSoup
import requests
from flask import Flask

app = Flask(__name__)

url ='https://www.worldometers.info/world-population/world-population-by-year/'


year = []
population = []

@app.route('/')
def main():
  r = requests.get(url).text
  soup = BeautifulSoup(r, 'html.parser')
  for data in soup.find('tbody'):
    '''
    Get every year then append every data on the year list
    '''
    year.append(data.td.get_text())
    '''
    Get every data, split the whitespaces get the second one which is the year then replace , with a blank string
    '''
    population.append(data.text.split()[1].replace(',', ''))
  '''
  Reverse the lists then put it on a dict and return it to the user
  '''
  year.reverse()
  population.reverse()
  json = {'info': f'this api is scraping {url} all of these are in order, it is optimized for a javascript library called Chart.js | Made by Yoshiinri | License: MIT | Repo: https://github.com/Yoshiinori/human-population-api','year': year, 'population': population}
  return json



if '__main__' == __name__:
  app.run(debug=True)
from bs4 import BeautifulSoup as bs
from requests import get 
from contextlib import closing
from requests.exceptions import ConnectionError
import pandas as pd

def get_exchange_rate_data(date):
  # print('url: {}'.format('https://www.xe.com/currencytables/?from=THB&date='+date))
  res=get('https://www.xe.com/currencytables/?from=THB&date='+date)
  soup = bs(res.content,'lxml')
  table = soup.find_all('table')[0] 
  listData = pd.read_html(str(table))
  df = listData[0]
  df.columns = ['a','b','c','d']
  return df

def find_exchange_rate_for_currence(curr, df):
  df = df.loc[df['a']==curr]
  
  return df['d'].item()

def get_exchange_rate_for_date_and_currency(date, currency):
  tabledf = get_exchange_rate_data(date)
  res= find_exchange_rate_for_currence(currency.upper(), tabledf)
  return res

def main():
  print(get_exchange_rate_for_date_and_currency('2013-11-07', 'inr'))

# main()
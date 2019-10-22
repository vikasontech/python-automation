import pandas as pd
from practice import read

def main():
  df = read('/Users/vikas/Downloads/2017-06-10_Yes Bank.csv')
  # df = df.loc[:,['category']]
  df = df['Category']
  df = df.drop_duplicates(keep='first')
  print(df)
  df.to_csv('/Users/vikas/Downloads/test2.csv')
main()
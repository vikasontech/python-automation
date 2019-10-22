import pandas as pd

import exchange as ex
import common


def read(fileName):
  return pd.DataFrame(pd.read_csv(fileName))


def checkCategory(value):
  if value == 'Income':
    return 'Income'
  return 'expense'


def main():
  df = read('/Users/vikas/Downloads/2017-06-10_Yes Bank.csv')
  # df = df.head(2)
  df['new-col'] = df['Payment Method'].map(str) + \
                  '~' + \
                  df['Description'].map(str)

  # df['Date'] = df['Date'].map(str)+ ' 00:00:00'
  # df = df.drop(columns=['Payment Method', 'Description'])

  # print(df.head(2))
  newDf = pd.DataFrame()

  newDf['Date'] = df['Date'].map(str) + ' 00:00:00'
  newDf['Wallet'] = 'Wallet'
  newDf['Category Type'] = df['Amount'].apply(lambda x: 'income' if x > 0 else 'expense')
  newDf['Category Name'] = df['Subcategory']
  newDf['Rate'] = round(df['Date'].apply(lambda x: ex.get_exchange_rate_for_date_and_currency(x, 'INR')), 4)
  newDf['Amount'] = newDf['Rate'] * df['Amount']
  newDf['Amount'] = round(newDf['Amount'], 2)
  newDf['Currency'] = 'THB'
  newDf['Note'] = df['Payment Method'].apply(lambda x: '#' + x.replace(' ', '-'))
  newDf['Note'] = newDf['Note'] \
                  + ', ' \
                  + df['Description'] \
                  + ', ' \
                  + ',RATE: ' \
                  + newDf['Rate'].map(str) \
                  + ', ' \
                  + df['Tag'].apply(lambda x: '#' + str(x))

  newDf = common.calclate_tag_and_category(newDf)
  newDf = newDf.drop(columns=['Rate'])
  # print(newDf.head(5))

  newDf.to_csv('/Users/vikas/Downloads/test2.csv')
main()

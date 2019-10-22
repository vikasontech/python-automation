def test():
  print('hello')

def sample():
  d = {'Interest': ('Extra Income', '#interest'), \
       'Account Transfer': ('do not process', ''), \
       'Pocket Money': ('Family & Personal', '#pocketmoney'), \
       'Aeroplane': ('Travel', '#ticket'), \
       'Other': ('Other', ''), \
       'Mobile': ('Utilities', '#mobile'), \
       'Rupesh Bhaiya': ('Home', '#rupeshbhaiya'), \
       'Lent': ('Utilities', '#lent'), \
       'Equities': ('Other', ''), \
       'Fee': ('Utilities', ''), \
       'Gift': ('Utilities', '#gift'), \
       'Train': ('Travels', '#ticket'), \
       'Insurance': ('Utilities', '#insurance')}

  return d

def calclate_tag_and_category(df):
  d = sample()
  df['Category Name'] = df['Category Name'].apply(lambda x: d[x][0] if x in d else x)
  return df


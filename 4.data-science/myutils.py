from dataclasses import dataclass
from practice import read


def test():
  print('test')


def sample():
  d = {'Interest': ('Extra Income','#interest') , \
      'Account Transfer': ('do not process','') ,\
      'Pocket Money': ('Family & Personal','#pocketmoney') ,\
      'Aeroplane': ('Travel','#ticket') ,\
      'Other': ('Other','') ,\
      'Mobile': ('Utilities','#mobile') ,\
      'Rupesh Bhaiya': ('Home','#rupeshbhaiya') ,\
      'Lent': ('Utilities','#lent') ,\
      'Equities': ('Other','') ,\
      'Fee': ('Utilities','') ,\
      'Gift': ('Utilities','#gift') ,\
      'Train': ('Travels','#ticket') ,\
      'Insurance': ('Utilities','#insurance')}

  return d


def calclate_tag_and_category(df):
  d = sample()
  df['Category Name2'] = df['Category Name'].apply(lambda x: d[x][0] if x in d else x )
  return df


# def calclate_tag_and_category2():
#   df = read('/Users/vikas/Downloads/test.csv')
#   d = sample()

#   df['Category Name2'] = df['Category Name'].apply(lambda x: d[x][0] if x in d else x )

#   df.to_csv('/Users/vikas/Downloads/test2.csv')
#   return df

print(calclate_tag_and_category())

from vocabulary import main as voc
from currency import main as cur

print("Welcome to the automation tools v.01")

def option():
  print("1. Vocabulary")
  print("2. Currency Calculator")
  print("q. Quit")
  choice = input("What's your choice: ")
  return choice

def process():
  choice = 'none'
  while (choice != 'q'):
    choice = option()
    choice = choice.lower()
    if( choice == "1"):
      print("vocabulary")
      voc()
    elif ( choice == "2"):
      print("currancy")
      cur()
    elif (choice != 'q'):
      print("Choose correct option!!!")
  
process()

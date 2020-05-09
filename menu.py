from vocabulary import main as voc
from currency import main as cur
#from gistutils import main as gist_convertor
import gistutils as g

print("Welcome to the automation tools v.02")

def option():
  print("1. Vocabulary")
  print("2. Currency Calculator")
  print("3. Gist url format")
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
    elif ( choice == "3"):
      print("Gist url convertor")
      g.main()
    elif (choice != 'q'):
      print("Choose correct option!!!")

try:
    process()
except KeyboardInterrupt as e:
    print("\nsee you soon ...")

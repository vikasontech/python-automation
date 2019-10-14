from bs4 import BeautifulSoup as bs
from requests import get 
from contextlib import closing

def tester(soup):
    #find the css class
    #soup = soup.find_all('p', class_='short')
    soup = soup.find_all('p')
    return soup[0].contents

def tester2(soup):
    soup = soup.find_all('p')
    return soup[1].contents



def stringFormatter(arrayString):
    str1 = ''
    for s in arrayString:
        str1 = str1 + str(s)

    str1 = str1.replace('<i>','`')
    str1 = str1.replace('</i>','`')
    return str1


def main():
    inp = input("Input word you want to search: ")
    print("Searching for ",inp,"...")
    url = 'https://www.vocabulary.com/dictionary/' + inp
    print('----'*30)
    with closing(get(url, stream=True)) as resp:
        html_doc = resp.content
        soup = bs(html_doc, 'html.parser')
        print("\n", stringFormatter(tester(soup)))
        print('----'*30)
        inp = input("\nDo you want more(y/N):")
        if inp == 'y':
            print('----'*30)
            print("Printing more ...\n")
            print(stringFormatter(tester2(soup)), "\n")
            print('----'*30)
            input("Press any key to exit...")

        


#todo
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
main()

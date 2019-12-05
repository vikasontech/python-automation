from bs4 import BeautifulSoup as bs
from requests import get 
from contextlib import closing
from requests.exceptions import ConnectionError

def tester(soup):

    checkWordFound = soup.find_all('h1', class_='dynamictext')
    if(len(checkWordFound) == 0):
        return;

    soup = soup.find_all('p')
    return soup[0].contents


def tester2(soup):
    soup = soup.find_all('p')
    return soup[1].contents


def stringFormatter(arrayString):
    str1 = ''
    if arrayString is None:
        return ;

    for s in arrayString:
        str1 = str1 + str(s)

    str1 = str1.replace('<i>','`')
    str1 = str1.replace('</i>','`')
    return str1


def main():
    while True:
        inp = input('Input word you want to search or input (q/Q) for quit: ')
        if (inp.lower() == 'q'):
            print('value of inp {}'.format(inp))
            break;

        print("\nSearching for ",inp,"...")
        url = 'https://www.vocabulary.com/dictionary/' + inp
#        print('url: ', url)
        print('----'*30)
        try:
            with closing(get(url, stream=True)) as resp:
                html_doc = resp.content
                soup = bs(html_doc, 'html.parser')
                result = stringFormatter(tester(soup))

                if result is None:
                    print("word not found")
                    print('----'*30)
                    continue 
                    return 
                print("\n>>>>", result)
                print('----'*30)
                print("Printing more ...\n")
                print(stringFormatter(tester2(soup)), "\n")
                print('----'*30)
        except ConnectionError as e:
            print("ERROR! unable to connect pls check your internet connection")
            # print('----'*30)




def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
# main()

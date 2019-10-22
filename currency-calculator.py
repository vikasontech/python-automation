from bs4 import BeautifulSoup as bs
import requests

transaction_fee = 300
def get_current_exchange_rate(): 
    res=requests.get('https://www.kasikornbank.com/en/Rate/Pages/Foreign-Exchange.aspx')
    soup=bs(res.content, 'html.parser')
    for tab in soup.find_all('div', class_='itemsRate'):
        if tab['data-sname'].strip() == 'INR':
            return float(tab['data-sellchq'].strip())
            break

def details():
    print('kBank Fee per transaction: {}'.format(transaction_fee))

def calculate_inr_by_thb_at_current_exchange_rate(thb_want_to_send):
    actual_thb_after_tax = thb_want_to_send-transaction_fee
    rate = get_current_exchange_rate()
    expecte_inr=round(actual_thb_after_tax*(1/rate), 2)
    print('Rate: {}, Expected inr: {}'.format(rate, expecte_inr))

def main():
    while (True):
        res= input("How much money you want to send (THB) or Q/q to quit:")
        if res.lower() == 'q':
            break;
        thb_want_to_send=float(res.strip())
        calculate_inr_by_thb_at_current_exchange_rate(thb_want_to_send)



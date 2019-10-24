from bs4 import BeautifulSoup as bs4
import requests
import re
from PyPDF2 import PdfFileWriter

url = "https://th.jobsdb.com/TH/EN/Search/FindJobs?KeyOpt=COMPLEX&JSRV=1&RLRSF=1&JobCat=1&SearchFields=Positions,Companies&Key=software%20development%20team%20lead&Locations=2&SalaryF=130000&SalaryType=1&JSSRC=JSRSB"


class HtmlContent():

    def get_html(url2):
        res = requests.get(url2)
        soup = bs4(res.content, 'html.parser')
        return soup

def find_all_jobs(soup):
    list_of_jobs = soup.find_all('a', class_='posLink')
    return list_of_jobs

def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', str(text)).strip()

class JobDesciption():
    def get_job_title(s):
        h1s = s.find_all('h1', class_="general-pos ad-y-auto-txt2")
        for title in h1s: 
            return title.contents[0].strip()

    def get_company_name(s):
        h2s = s.find_all('h2', class_="jobad-header-company ad-y-auto-txt1")
        for name in h2s:
            return name.contents[0].strip()

    def get_salary_details(s):
        s1 = s.find_all('p', class_='meta-item primary-meta-salary col-xs-9')
        for e in s1:
            salary_detail = remove_tags(e)
        return salary_detail
        
    def get_job_description(s):
        cls = 'jobad-primary-details'
        s1 = s.find_all('div', class_=cls)
        for e in s1:
            #print(e.contents)
            for x in e.contents:
                print (remove_tags(x))
            #print(e)
        return ''
class PDFwritter():
        def writePDF(text):
            output = PdfFileWriter()
            os = open("sample.pdf", "wb")
            output.write(os)
            

def main():
    htmlcontent = HtmlContent()
    soup = HtmlContent.get_html(url)
    list_of_jobs = find_all_jobs(soup)

    for jobs in list_of_jobs:
        link = jobs['href']
        s = HtmlContent.get_html(link)
        print(f"title: {JobDesciption.get_job_title(s)}") 
        print(f"company: {JobDesciption.get_company_name(s)}")
        print(f"salary: {JobDesciption.get_salary_details(s)}")
        print(JobDesciption.get_job_description(s));
#main()
def sampe():
    PDFwritter.writePDF("jai shri ram")

sampe()




from bs4 import BeautifulSoup as bs4
import requests

url = "https://th.jobsdb.com/TH/EN/Search/FindJobs?KeyOpt=COMPLEX&JSRV=1&RLRSF=1&JobCat=1&SearchFields=Positions,Companies&Key=software%20development%20team%20lead&Locations=2&SalaryF=130000&SalaryType=1&JSSRC=JSRSB"


class HtmlContent():

    def get_html(url2):
        res = requests.get(url2)
        soup = bs4(res.content, 'html.parser')
        return soup


def find_all_jobs(soup):
    list_of_jobs = soup.find_all('a', class_='posLink')
    return list_of_jobs


class JobDesciption():
    def get_job_title(s):
        h1s = s.find_all('h1', class_="general-pos ad-y-auto-txt2")
        for title in h1s: 
            return title.contents[0].strip()

    def get_company_name(s):
        h2s = s.find_all('h2', class_="jobad-header-company ad-y-auto-txt1")
        for name in h2s:
            return name.contents[0].strip()

        
    def get_job_description(s):
        print(s.find_all('section', class_='jobad-body'))
        #print(s.html.body.main.div.article.section.contents)
#        des = s.find_all('span')
#/html/body/main/div/article[1]/section[2]/div/div[1]/div[2]/span/ul[1]/li[1]/span/text()
#        for uls in des:
#            print(uls.attrs)
#            print(uls.contents)
#            break
        return "demo"

htmlcontent = HtmlContent()
soup = HtmlContent.get_html(url)
list_of_jobs = find_all_jobs(soup)

for jobs in list_of_jobs:
    link = jobs['href']
    s = HtmlContent.get_html(link)
    print(f"title: {JobDesciption.get_job_title(s)}") 
    print(f"company: {JobDesciption.get_company_name(s)}")
    print(JobDesciption.get_job_description(s));


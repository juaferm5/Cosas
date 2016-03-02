import requests
from bs4 import BeautifulSoup

s = requests.Session()
#print("dime tu mierda: ")
url=raw_input("Dime tu caca: ")
r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text)
viewstate_element = soup.find (id="__VIEWSTATE")
viewstate = viewstate_element["value"]
eventvalidation_element = soup.find (id="__EVENTVALIDATION")
eventvalidation = eventvalidation_element["value"]

r = s.post(url,
                 data = {'AirportList': "BOS",
                         'CarrierList':"VX",
                         'Submit': "Submit",
                         '__EVENTTARGET':"",
                         '__EVENTARGUMENT':"",
                         '__EVENTVALIDATION': eventvalidation,
                         '__VIEWSTATE':viewstate})

f = open ("caca.html","w")
f.write(r.text)

import requests
from bs4 import BeautifulSoup
import webbrowser
import urllib

text = input("Search :")

url = "https://nigeriaphonebook.com/search-result?contactPhone" + "=" + text

result = requests.get(url)
with open('outpu.html', 'wb') as f:
    f.write(result.content)
webbrowser.open('outpu.html')
soup = BeautifulSoup(result.text, "lxml")
final = soup.find_all('main')
finalist = final[0].find('section', class_="search-sec-contact1 search-filter-sec mt-2")
fin = finalist.find('div', class_="container custom-max-wid")
fi = fin.find('div', class_="row")
f = fi.find('div', class_="w-100 col-md-12")
for r in f:
    print(r.text)








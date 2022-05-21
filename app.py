import phonenumbers
from urllib import request
from flask import Flask, flash, render_template, request
from  phonenumbers import geocoder, timezone, carrier
from forms import Search
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    form = Search(request.form)
    num = request.form.get('num')
    if request.method == "POST":

        
     
        numb = phonenumbers.parse(num, 'NG')
        
        x = geocoder.description_for_number(numb, 'en')

        n = timezone.time_zones_for_number(numb)
        c = carrier.name_for_number(numb, 'en')
        url = "https://nigeriaphonebook.com/search-result?contactPhone=" + num

        result = requests.get(url)
        
        soup = BeautifulSoup(result.text, "lxml")
        final = soup.find_all('main')
        finalist = final[0].find('section', class_="search-sec-contact1 search-filter-sec mt-2")
        fin = finalist.find('div', class_="container custom-max-wid")
        fi = fin.find('div', class_="row")
        f = fi.find('div', class_="w-100 col-md-12")
       
        
        

        return render_template('result.html', x=x, n=n, c=c, f=f)
        
   

    return render_template('phone.html', num=num, form=form)



if __name__ == "__main__":
    app.run()
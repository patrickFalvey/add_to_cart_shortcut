from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView
from django.http import HttpResponse

import mechanize
from time import sleep

def home(request):
    return render(request, 'demo/index.html')

import datetime

def AddToCartDavidson(request):

##    #Aquire Davidson's username
##    user = UserProfile.objects.get(user=request.user.id)
##    username = user.davidson_login
##
##    #Decrypt Davidson's password
##    fernet = Fernet(FERNET_KEY)
##    password = fernet.decrypt(user.davidson_password)
##
##    #Product upc will be used to navigate to proper page once logged in
##    product = Product.objects.get(id=request.GET.get('product_id'))
##    upc = product.upc
    upc = '098289019349'

    

    #Instantiate mechanize browser and login to Davidson's
    br = mechanize.Browser()
    cj = mechanize.CookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    br.addheaders = [
        ('User-agent',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
        ]
    site = "http://www11.davidsonsinc.com/Login/Login.aspx"
    br.open(site)
    br.select_form(nr=0)
##    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$UserName'] = username
##    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$Password'] = password
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$UserName'] = 'scott@gsadirect.com'
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$Password'] = 'gsadirect1'
    br.submit()
        
    product_page = 'http://www11.davidsonsinc.com/Dealers/ItemDetail.aspx?sid=%s&scode=upcID' % (upc,)
    br.open(product_page)

    c_expires = datetime.datetime.now() + datetime.timedelta(days=1)
    print c_expires
    
    response = redirect(product_page)

    Inject cookies into response object
    for cookie in cj:
        name = cookie.name
        if name != 'ASP.NET_SessionId' and name != '.ASPXAUTH':
            response.set_cookie(cookie.name, cookie.value, expires=c_expires, domain='.www.davidsonsinc.com')
            print cookie.name, cookie.value, cookie.domain
        else:
            response.set_cookie(cookie.name, cookie.value, expires=c_expires,domain='www.davidsonsinc.com', httponly=True)
        


    return response


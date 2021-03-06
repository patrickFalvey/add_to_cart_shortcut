from django.views.generic.base import RedirectView
from braces.views import LoginRequiredMixin

import mechanize
from cryptography.fernet import Fernet

from saasapp.models import Product, UserProfile
from saas.fernet import FERNET_KEY



class AddToCartDavidson(LoginRequiredMixin, RedirectView):

    #Aquire Davidson's username
    user = UserProfile.objects.get(user=request.user.id)
    username = user.davidson_login

    #Decrypt Davidson's password
    fernet = Fernet(FERNET_KEY)
    password = fernet.decrypt(user.davidson_password)

    #Product upc will be used to navigate to proper page once logged in
    product = Product.objects.get(id=request.GET.get('product_id'))
    upc = product.upc 

    

    #Instantiate mechanize browser and login to Davidson's
    br=mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [
        ('User-agent',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
        ]
    site = "http://www11.davidsonsinc.com/Login/Login.aspx"
    br.open(site)
    br.select_form(name="aspnetForm")
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$UserName'] = username
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$Password'] = password
    br.submit()
    
    permanent = False

    #Redirect to specific Davidson's product page using upc
    def get_redirect_url(self, *args, **kwargs):
        self.url = 'http://www11.davidsonsinc.com/Dealers/ItemDetail.aspx?sid=%s' % upc
        return super(AddToCartDavidson,
                     self).get_redirect_url(*args, **kwargs)



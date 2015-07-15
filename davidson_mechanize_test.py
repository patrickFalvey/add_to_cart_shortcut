import mechanize


upc = '723364202001'

def add_to_cart_davidson(upc):


    username = 'scott@gsadirect.com'
    password = 'gsadirect1'
    
    br=mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
        ]
    url = "http://www11.davidsonsinc.com/Login/Login.aspx"
    br.open(url)

    br.select_form(nr=0)
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$UserName'] = username
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$Password'] = password
    br.submit()
        
    product_page = 'http://www11.davidsonsinc.com/Dealers/ItemDetail.aspx?sid=%s&scode=upcID' % (upc,)
    br.open(product_page)

add_to_cart_davidson(upc)







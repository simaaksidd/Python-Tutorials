from random import betavariate
import requests
from bs4 import BeautifulSoup

# using the requests module, we use 'get' to provide bs4 access to the website 
result = requests.get("https://www.google.com/")

# This does not show if it actually got to the site
# To ensure that this works a-ok we should print an http status code
# 200 OK indicates that the page is there!
# print(result.status_code)

# if not 200 OK, use https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# This wiki is for unkown codes

# for xtra info use: 
# print(result.headers)

# to print the source of the website:
src = result.content


# Now that we have a src var with all of the info that we need
# We will pass this info to bs4, which will make this data in the lxml format
soup = BeautifulSoup(src, 'lxml')

# find all finds all data with tags.  
links = soup.find_all("a")
# This would find all the anchor tags, so they'll find all the links
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
# this is a simple loop which looks for a link in the links list for an "About" in the text
# then we print the actual variable 'link'
# we also print the attribute 'href'
# the link var output is: <a href="/intl/en/about.html">About Google</a>
# the href attr output is: /intl/en/about.html

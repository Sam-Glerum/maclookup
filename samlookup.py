#Sam Glerum
'''
- Post mac_address to http://coffer.com/mac_find/?string=
- Return mac_address + vendor
'''

'''
Functions to be created:
- Get user input
- Append user input to http://coffer.com/mac_find/?string=
- Open the URL + user input
- Read (scrape) the mac_address + right vendor
- Print result to console
'''

import urllib2


class UserInput(object):
    def __init__(self):
        pass

    def user_input(self):
        #get a mac address from the user
        self.user_mac_input = str(raw_input("\nEnter a valid MAC-Address: ")).lower()

    def search_site(self):
        #set url to search and append the mac address to the url
        #this url can then be searched
        search_url = "http://coffer.com/mac_find/?string="
        mac_url = search_url + self.user_mac_input
        search_coffer = urllib2.urlopen(mac_url)
        return search_coffer

    def scrape_site(self):
        #scrape the html-elements containing the mac_address + Vendor
        #return the scraped data
        print "nothing here yet mate"


runprogram = UserInput()
runprogram.user_input()
runprogram.search_site()

# import libraries
# -*- coding: utf-8 -*-
import sqlite3

from requests import get
url = 'https://www.keepinspiring.me/famous-quotes/' # the webpage to be scraped for quotes
response = get(url)

#python scraping module
from bs4 import BeautifulSoup

#parsing and storing the webpage
soup = BeautifulSoup(response.text, 'html.parser')

#connecting the database using sqlite3
conn = sqlite3.connect('/home/nimba/Documents/quotes.db')
cur=conn.cursor()

#scanning for the relevant tags in the HTML file
for my_tag in soup.find_all('div',class_='author-quotes'):
	dquote=my_tag.text.strip()

	#writing the data 
	cur.execute("insert into quotes2(quote)values(?)",(dquote,))

#commit
conn.commit();
conn.close();

       

		
			
    		













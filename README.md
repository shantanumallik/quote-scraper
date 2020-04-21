# quote-scraper
A Python based scraper that fetches quotes from a website, converts them to images and posts them to a social media platform of your choice

# Setup
	-Install Python ( any version )
	-setup sqlite3
	-install the font 'AmaticsSC-Regular.ttf'. This step is crucial.
	-create a database with primary key being 'id'. Set it to auto increment. The other column in the table will store the quote
	-name of the database must be 'quotes.db'

# Execution

	-run the file 'scrape.py' to scrape a website and store the quotes in the database file 'quotes.db'
	-run the file 'app.py'
	-go to localhost:5000
	-the quote displayed on the page will be saved as an image in the api root directory.
	-refresh the page to get a different quote everytime.
	
# Known issues
	- No API has been added to post the generated image to any social media.
	- The tweet.py file is just a template

# search for tabs script
# Ben Watson - 24/11/17

# workflow:
# 1. user input, search terms    2. send query to UG
# 3. scrape & show links of search results
# 4. select desired url for input into scraper module
# it ain't pretty but it works!

import bs4 as bs
from lxml import html
import requests
import docx

# user input search term - be as specific as possible for best results
search_term = input('tab search - be specific')

# format search term string for passing into UG search (format = 'term'+'term'+...)
# split search string on whitespace, add '+'
str = '+'.join(search_term.split())

# UG query url, stored as string
query = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value='
# concatenate string to pass to http request
UG = query + str

# pass str to UG search query
results = requests.get(UG)

# scrape data from search results page
soup = bs.BeautifulSoup(results.content, 'lxml')

#  select 'tresults' table from soup
table = soup.find('table', class_='tresults')

# create empty list to store results links for later access
list = []

#  scrape links from table, add to list, print links for user to see
for link in table.find_all('a'):
    list.append(link.get('href'))
    print(link.get('href'))

# user views printed links, selects from list, convert input to int
choice = int(input('enter # to choose link from list'))

# user input passed to http request
tab_url = requests.get(list[choice])

# soup made from selected url
tab_page = bs.BeautifulSoup(tab_url.content, 'lxml')

# select & print desired TABs text from 'pre' tag
for tab in tab_page.find_all('pre'):
    print(tab.text)


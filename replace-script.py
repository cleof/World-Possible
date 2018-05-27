from bs4 import BeautifulSoup
from urllib.request import urlopen

# read html file and create soup object
response = urlopen('https://learningenglish.voanews.com/a/lets-learn-english-lesson-26-this-game-is-fun/3457248.html')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# initially commenting out
# for item in soup.find_all("li", class_="block-socials"):
# 	item.replace_with('<!- ' + item.text + '>')

# find and remove the social blocks at the bottom of the page
for item in soup.find_all("li", {'class':'block-socials'}): 
    item.decompose()

# update html
file = open("https://learningenglish.voanews.com/a/lets-learn-english-lesson-26-this-game-is-fun/3457248.html","w+")
file.write(soup.text)
file.close()
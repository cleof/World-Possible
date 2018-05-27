from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://learningenglish.voanews.com/a/lets-learn-english-lesson-26-this-game-is-fun/3457248.html')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.find_all("li", class_="block-socials"):
	item.replace_with('<!- ' + item.text + '>')

print(soup)
file = open("new.html","w+") # this is writing the file weirdly...
file.write(soup.text)
file.close()
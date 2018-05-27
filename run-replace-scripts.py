from bs4 import BeautifulSoup
from shutil import copyfile

# example script
def remove_social(soup):
	for item in soup.find_all("li", class_="block-socials"):
		item.replace_with('')

# suffix appended to backup file
BACKUP_SUFFIX = 'original'

# function that copies original file and then transforms html with a list of replace scripts
# arg1: name of file to be transformed
# arg2: files that have already been transformed <-- this should be included in this function
# arg3: transformations to be performed on file
def transform(file_name, already_visited = [], tranformations = []):
	# copy the file iff we haven't seen this file before
	original_file_name = file_name[:-4] + BACKUP_SUFFIX + '.html'

	if file_name not in already_visited:
		copyfile(file_name, original_file_name)

	# read the originally scraped version
	source = None
	with open(original_file_name, 'r') as data:
		source = BeautifulSoup(data.read(), 'html.parser')

	# run transformations
	for fn in tranformations:
		fn(source)

	# overwrite original
	with open(file_name, "w") as out_file:
		out_file.write(str(source))

if __name__ == '__main__':
	print("running!")
	transform("/Users/rwoll/Desktop/tech/learningenglish.voanews.com/a/lets-learn-english-lesson-26-this-game-is-fun/3457248.html", ["/Users/rwoll/Desktop/tech/learningenglish.voanews.com/a/lets-learn-english-lesson-26-this-game-is-fun/3457248.html"], [remove_social])
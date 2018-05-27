# Writing a replace script

### Install python

Now that we have `wget` isntalled, let's get Python 3 installed!

If you're using `brew`, simply type:

```
$ brew install python3
```

(To check what version you have installed, type `python --version` in your shell.)

### Create working environment

Let's create a new folder on the Desktop:

```
$ cd ~/Desktop # which whill get you to your desktop
$ mkdir tech # to create a folder to work in
$ cd tech # to move into the folder we just created
```

> If you're ever unsure of where you are, type `pwd` to find
> __p__rint __w__orking __d__irectory

```
$ python3 -m venv techenv
```

Let's activate the environment:

```
$ source techenv/bin/activate
```
### Install beautiful soup (with pip)

Now that we are in are in our environment, let's install Beautiful Soup. 
Beautiful soup is a python package that allows for the search and manipulation of html sites.

```
$ pip install beautifulsoup4
```

Here's the documentation for using Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/.

### Create a replace script

Create a file to work with:

```
$ touch replace_script.py
```

Open the file in your favorite text editor,
then add the following contents to the file:

```python
print('Hello, World!')
```

Save the file!

### Running the script

Run the file:

```
$ python3 replace_script.py
```

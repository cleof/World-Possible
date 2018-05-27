# Scraping the site

## Wget

Use wget to scrape one site. This site will be used to assess what features must be changed or removed for offline access. It crawls just enough to get linked media.

[Wget 1.18 Manual](https://www.gnu.org/software/wget/manual/wget.html#HTTP-Options)

#### The script we used to scrape learningenglish.voanews.com:

```
$ wget --reject b --span-hosts --domains learningenglish.voanews.com,av.voanews.com --no-clobber --page-requisites --adjust-extension --convert-links https://learningenglish.voanews.com/a/lets-learn-english-lesson-26-this-game-is-fun/3457248.html
``` 
* --reject b: Used to prevent the download of files ending in \*\.b.
* --span-hosts: Enables spanning across hosts when doing recursive retrieving.
* --domains: Set domains to be followed. domain-list is a comma-separated list of domains.
* --no-clobber: Prevents multiple versions of site being downloaded upon re-download.
* --page-requisites: This option causes Wget to download all the files that are necessary to properly display a given HTML page. This includes such things as inlined images, sounds, and referenced stylesheets.
* --adjust-extension: requires suffix ‘.html’ to be appended to the local filename.
* --convert-links: convert the links in the document to make them suitable for local viewing

#### Initiate local server via terminal to view and navigate the scraped site:

```
$ python3 -m http.server --bind 127.0.0.1
```


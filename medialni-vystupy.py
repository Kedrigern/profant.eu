#!/usr/bin/env python3

import os
import re
import sys
import csv
import glob
import markdown
from sh import git

"""
Download pirates press releases with given keywords. Default is "profant".
Use git repos of jekylls websites from Config.
"""

class Config:
    repos = {
        "pirati.cz": {
            "url": "git@github.com:pirati-web/pirati.cz.git",
            "prefix": "/tiskove-zpravy/"
        },
        "praha.pirati.cz": {
            "url": "git@github.com:pirati-web/praha.pirati.cz.git",
            "prefix": "/"
        }
    }
    verbose = True
    keyword = "profant"
    resultPath = "./_data/media.csv"

class Result:
    articles = []
    totalCount = 0

def article_condition(article):
    keyword = Config.keyword
    if keyword in article['text'].lower():
        return True
    if keyword in article['author'][0]:
        return True
    return False

def article_clean(article):
    title = article['title']
    try:
        article['title'] = title[0].strip('"')
        article['date'] = article['date'][0]
        article['tags'] = article['tags'][0]
        article['author'] = article['author'][0]
    except KeyError:
        article['tags'] = ""
        print("Error: " + title[0])

def create_url(path, prefix):
    """
    TODO BUG:
    Okusuje o znak víc
    https://praha.pirati.cz/hrib-proti-kamera.html => https://praha.pirati.cz/hrib-proti-kameraM.html
    https://praha.pirati.cz/kamerovy-syste.html => https://praha.pirati.cz/kamerovy-systeM.html
    Funguje:
    https://praha.pirati.cz/dopis-white-media.html
    """
    spath = path.rstrip(".md")[25:] # example: ./_post/2016/2016-03-16-
    return prefix + spath + ".html"

def take_key(elem):
    return elem['date']

def result_output():
    Result.articles.sort(key=take_key)
    if not Config.verbose:
        print("Match: ", len(Result.articles), "/", Result.totalCount)
        for a in Result.articles:
            print(a['date'], a['title'], a['tags'])
    with open(Config.resultPath, 'w', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["date", "title", 'author', 'tags', 'url'])
        for a in Result.articles:
            try:
                spamwriter.writerow([a['date'], a['title'], a['author'], a['tags'], a['url']])
            except KeyError as e:
                print("KeyError: ", a, e)
                sys.exit()

def process_article(filepath, prefix):
    """Process one file with article.
    File is formated as markdown with yaml header"""
    text = ""
    md = markdown.Markdown(extensions=['meta'])
    with open(filepath, 'r') as fp:
        text = fp.read()
    html = md.convert(text)
    record = md.Meta
    record['text'] = text
    record['filepath'] = filepath
    record['url'] = create_url(filepath, prefix)
    try:
        if article_condition(record):
            article_clean(record)
            Result.articles.append(record)
        if not Config.verbose:
            print(".", end="")
    except KeyError:
        print("KeyError: ", filepath)

def process_repo(dirname, repo):
    """Process one git repository"""
    if not Config.verbose:
        print("Process " + dirname)
    if not os.path.isdir(dirname):
        print("Clone " + repo["url"])
        git.clone("--depth", "2", repo['url'])
    os.chdir(dirname)
    git.pull()
    mds = glob.glob("./_posts/*/*.md")
    Result.totalCount += len(mds)
    prefix = "https://" + dirname + repo['prefix']
    for path in mds:
        process_article(path, prefix)
    if not Config.verbose:
        print()
    os.chdir("..")

originalDir = os.getcwd()
os.chdir("..")
for name, repo in Config.repos.items():
    process_repo(name, repo)

os.chdir(originalDir)
result_output()

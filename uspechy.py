#!/usr/bin/env python3

import io
import yaml
import pandas
import requests
from pprint import pprint   # DEBUG
from redminelib import Redmine, exceptions

"""
Download "výsledky" from source data of pirati.cz/vysledky
Source data are in Redmine

Redmine priority:
7: Okamžitá
6: Urgentní
5: Vysoká
4: Normální
3: Nízká
"""

class Config:
    verbose = True
    resultPath = "./_data/uspechy.yaml"
    urls = {
      "rm": "https://redmine.pirati.cz",
      "issue": "https://redmine.pirati.cz/issues/",
      "issues": "https://redmine.pirati.cz/projects/snemovna/issues.json",
      "issues_tags": "https://redmine.pirati.cz/issues.csv?utf8=✓&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=28&f%5B%5D=project_id&op%5Bproject_id%5D=%3D&v%5Bproject_id%5D%5B%5D=185&v%5Bproject_id%5D%5B%5D=186&v%5Bproject_id%5D%5B%5D=187&v%5Bproject_id%5D%5B%5D=188&v%5Bproject_id%5D%5B%5D=189&v%5Bproject_id%5D%5B%5D=190&v%5Bproject_id%5D%5B%5D=191&v%5Bproject_id%5D%5B%5D=192&v%5Bproject_id%5D%5B%5D=193&v%5Bproject_id%5D%5B%5D=125&v%5Bproject_id%5D%5B%5D=194&v%5Bproject_id%5D%5B%5D=195&v%5Bproject_id%5D%5B%5D=196&v%5Bproject_id%5D%5B%5D=197&f%5B%5D=&c%5B%5D=tags_relations&group_by=project&t%5B%5D="
    }
    tag = "profant"
    default_icon = "thumbs-up"
    default_img = ""

def get_relevant_issues_id(tag=None):
  """
  Get data from Redmine into pandas dataframe
  Data are csv (redmine json api cannot provide tags from plugin)

  Return pandas.DataFrame
  """
  url = Config.urls['issues_tags']

  content = requests.get(url).content
  raw_string = io.StringIO(content.decode('utf-8'))

  df = pandas.read_csv(
      raw_string,
      header=0,
      names=['id','tag'] )

  if tag:
    # TODO: case sensitive
    df = df[df['tag'].str.contains(tag)]

  if Config.verbose:
    print("DEBUG: get_relevant_issues_id with tag %s return %s issues" % (tag, df.id.count()))

  return df

def get_relevant_issues():
  """
  https://python-redmine.com/resources/issue.html

  Return array of redminelib.resources.Issue.
  
  Interesting fields:
   - issue.id
   - issue.subject
   - issue.created_on
   - issue.start_date -- used
   - issue.due_date
   - issue.tags -- specialy added
   - issue.custom_fields.get(48).value -- img
   - issue.custom_fields.get(50).value -- video
   - issue.description
  """
  df = get_relevant_issues_id(Config.tag)
  redmine = Redmine(Config.urls['rm'])
  issues = []
  for i in df.id:
    try:
      issue = redmine.issue.get(int(i))
      # Add tags:
      issue.tags = df[df.id==i].tag.values[0].split(', ')
      # Shortcuts:
      issue.img = issue.custom_fields.get(48).value
      issue.video = issue.custom_fields.get(50).value
      issue.date = issue.start_date
      issues.append(issue)
    except exceptions.ResourceNotFoundError:
      if Config.verbose:
        print("ERROR: Resource %s does not exists:" % (i))

  if Config.verbose:
    print("DEBUG: get_relevant_issues found %s issues" % len(issues))

  return issues

def reduce_issues(issues):
    new_issues = []
    for i in issues:
      item = {
        'id': i.id,
        'date': i.date,
        'icon': Config.default_icon,
        'subject': i.subject,
        'img': i.img,
        'video': i.video,
        'priority': i.priority.id,
        'tags': i.tags,
        'description': i.description
      }
      new_issues.append(item)
    return new_issues

def add_local_uspechy(issues):
  file = "_data/uspechy-add.yaml"
  data = []
  with open(file, encoding="utf-8") as fp:
    data = yaml.load(fp, Loader=yaml.FullLoader)
  prepend = data['prepend']
  # append = data['append']
  # for moditem in data['modify']:
  #  for k, v in enumerate(issues):
  #    if v['id'] == moditem['id']:
  #      print(moditem)
  #      print(v)
  return prepend + issues
  
def generate_uspechy():
  issues = add_local_uspechy(reduce_issues(get_relevant_issues()))
  with open(Config.resultPath, 'w+', encoding='utf-8') as fp:
      fp.write('#\n# Nepřepisujte! Soubor je generován automaticky skriptem uspechy.py\n#\n')
      yaml.dump(issues, fp, allow_unicode=True)

generate_uspechy()  

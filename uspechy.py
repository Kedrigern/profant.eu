#!/usr/bin/env python3

import csv
import json
import requests

class Config:
    urls = {
      "issue": "https://redmine.pirati.cz/issues/",
      "issues": "https://redmine.pirati.cz/projects/snemovna/issues.json",
      "issues_tags": "https://redmine.pirati.cz/issues.csv?utf8=✓&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=28&f%5B%5D=project_id&op%5Bproject_id%5D=%3D&v%5Bproject_id%5D%5B%5D=185&v%5Bproject_id%5D%5B%5D=186&v%5Bproject_id%5D%5B%5D=187&v%5Bproject_id%5D%5B%5D=188&v%5Bproject_id%5D%5B%5D=189&v%5Bproject_id%5D%5B%5D=190&v%5Bproject_id%5D%5B%5D=191&v%5Bproject_id%5D%5B%5D=192&v%5Bproject_id%5D%5B%5D=193&v%5Bproject_id%5D%5B%5D=125&v%5Bproject_id%5D%5B%5D=194&v%5Bproject_id%5D%5B%5D=195&v%5Bproject_id%5D%5B%5D=196&v%5Bproject_id%5D%5B%5D=197&f%5B%5D=&c%5B%5D=tags_relations&group_by=project&t%5B%5D="      
    }
    file = "issues.csv"
    verbose = True
    resultPath = "./_data/media.csv"


def get_issues_by_tags(tags):
  TODO: Download from url
  """
  """
  url = Config.urls['issues_tags']
  issues = []

  with open(Config.file) as f:
    reader = csv.reader(f)
    for row in reader:
        if tags[0] in row[1]:
          issues.append(row)

  return issues



print(get_issues_by_tags(['ondrej-profant'])[2])
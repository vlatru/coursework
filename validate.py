# encoding=utf-8

import os
import sys
import json
import urllib2

repo = os.environ['TRAVIS_REPO_SLUG']
pull_number = os.environ['TRAVIS_PULL_REQUEST']
api_head = "https://api.github.com/repos/"
api_request_url = "{}{}/pulls/{}".format(api_head, repo, pull_number)

try:
    response = urllib2.urlopen(api_request_url).read()
except urllib2.HTTPError:
    pass
else:
    pull_data = json.loads(response)
    username = pull_data['user']['login']

    dirs = ['1_poll', '2_quiz', '3_gallery']

    workdir = dirs[ord(username[0]) % 3]

    for dirname in dirs:
        if dirname == workdir:
            break
        if len(os.listdir(dirname)) > 1:
            print("Ошибка: \"{}\"	 не ваше задание".format(dirname))
            sys.exit(1)

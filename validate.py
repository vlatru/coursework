# encoding utf-8

import os

curr_dir = os.environ['TRAVIS_BUILD_DIR']
username = os.path.dirname(curr_dir)

print username

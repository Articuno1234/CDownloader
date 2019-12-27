# CDownloader by Articuno1234
import subprocess
import sys, os
import json

def get():
    user = sys.argv[1]
    repo = sys.argv[2]
    down(user, repo)
	
def down(user, repo):
    code = subprocess.call(("git", "clone", "https://github.com/{}/{}.git".format(user, repo)))
    if code == 0:
        if os.path.isfile('{}/cconfig.json'.format(repo)):
            with open('{}/cconfig.json'.format(repo), 'w+') as json_file:
                data = json.load(json_file)
                for p in data['Config']:
                    print("Author: {}\n{}\nDescription:\n{}".format(p['Author'], p['Version'], p['Description']))
        else:
            print("Looks like this repo does not have a config file!")
    else:
        print("\n>>> Unable to Download!")
	
get()
import requests
import json

def gitHubAPI(ID):
    repoURL = 'https://api.github.com/users/' + ID + '/repos'
    # print(repoURL)
    r = requests.get(repoURL)
    reposJSON = json.loads(r.text)
    names = []
    for obj in reposJSON:
        names.append(obj["name"])
        # print(obj["name"])
    # print(names)
    commitCount = 0
    for repoName in names:
        commitURL = 'https://api.github.com/repos/' + ID + '/' + repoName + '/commits'
        # print(commitURL)
        r = requests.get(commitURL)
        commitsJSON = json.loads(r.text)
        print('Repo: ' + repoName + ' - Number of commits: ' + str(len(commitsJSON)))
        commitCount = commitCount + len(commitsJSON)

    return len(names) + commitCount
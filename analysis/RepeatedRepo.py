import json


def runAnalysis(fileName):
    eventID = "PushEvent"

    res = dict()

    nonEvents = 0
    events = 0

    for line in open(fileName):
        data = json.loads(line)
        if data['type'] == eventID:
            repo = data['repo']['name'].partition("/")
            #name = repoPath.partition("/")[0]
            #repo = repoPath.partition("/")[2]
            if repo[0] in res:
                res[repo[0]].add(repo[2])
            else:
                res[repo[0]] = {repo[2]}

    count = 0
    for key in res:
        for repo in res[key]:
            count += 1
    print(fileName, ", ", count)

    return res

if __name__ == "__main__":
    fileBase = "data/2021-01-01-"
    res = dict()
    for i in range(10):
        #newRes = runAnalysis((fileBase + str(i) + '.json'), res)
        res.update(runAnalysis((fileBase + str(i) + '.json')))
        #res.update(newRes)

    count = 0
    for key in res:
        for repo in res[key]:
            count += 1
    print(count)

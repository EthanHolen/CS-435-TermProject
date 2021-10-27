import os
import json

def getJsonFiles(dataDir):
    return [jsonFile for jsonFile in os.listdir(dataDir) if os.path.isfile(os.path.join(dataDir, jsonFile))]

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
    dataDir = 'data2/decompressed/'
    jsonFiles = getJsonFiles(dataDir)
    res = dict()
    for jsonFile in jsonFiles:
        res.update(runAnalysis(dataDir + jsonFile))

    count = 0
    for key in res:
        for repo in res[key]:
            count += 1
    print(count)

import os
import json

def getJsonFiles(dataDir):
    return [jsonFile for jsonFile in os.listdir(dataDir) if os.path.isfile(os.path.join(dataDir, jsonFile))]

def runAnalysis(filePath):
    eventID = "PushEvent"

    res = dict()

    nonEvents = 0
    events = 0

    for line in open(filePath):
        data = json.loads(line)
        if data['type'] == eventID:
            repo = data['repo']['name'].partition("/")
            if repo[2] in res:
                res[repo[2]].add(repo[0])
            else:
                res[repo[2]] = {repo[0]}

    print(filePath.split("/")[-1], ", ", len(res))

    return res

if __name__ == "__main__":
    dataDir = 'data2/decompressed/'
    jsonFiles = getJsonFiles(dataDir)
    repoDict = dict()

    print("Listing number of unique repos per file")
    for jsonFile in jsonFiles:
        repoDict.update(runAnalysis(dataDir + jsonFile))

    # count = Number of API requests required with only partial optimization
    count = 0
    for key in repoDict:
        for user in repoDict[key]:
            count += 1

    print("\nRequests needed with partial optimization: ", count)
    print("Requests needed with full optimization: ", len(repoDict))

from sys import argv, exit
import requests, json, os


def get_toxicity(text):

    localhost = 'http://localhost:5000/model/predict'
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(localhost, headers=headers, data=text)
    return response.json()






def read_json(data):

    json_file = open(data)

    json_dict = json.load(json_file)

    filename = data.split(".")
    outputfilename = filename[0] + "-toxicity.json"
    outfile = open(outputfilename, "w")
    outfile.write("[\n")

    print("Writing to", outputfilename, "...")

    index = 0


    for i in json_dict:
        response = get_toxicity(json.dumps(i))
        wrapped_response = {'repo': i['repo'], 'response' : response}
        json.dump(wrapped_response, outfile)
        if index != len(json_dict) - 1:
            outfile.write(",\n")
        index += 1

    outfile.write("\n]")
    outfile.close()
    print("Toxicity Classification written to ", outputfilename)




def main(argv):
    if len(argv) != 2:
        exit("usage: python3 "+argv[0]+" datafile")


    read_json(argv[1])

if __name__ == "__main__":
    main(argv)
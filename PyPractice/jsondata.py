import requests

# process JSON data feed
def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    response = requests.get(urlData)
    print("result code: " + str(response.status_code))
    if(response.ok):
        data = response.json()
        printResults(data)
    else:
        print("ERR: Unable to process the url, pls retry")

def printResults(data):
    print("Printing results from the data..")
    if "title" in data["metadata"]:
        print(data["metadata"]["title"])
    if "count" in data["metadata"]:
        print(str(data["metadata"]["count"]) + " events recorded")

    for i in data["features"]:
        printPerFeature = "\n"
        if(("properties" in i) and "place" in i["properties"]):
            printPerFeature = i["properties"]["place"] + printPerFeature
        if("mag" in i["properties"]):
            printPerFeature = str(i["properties"]["mag"]) + ", " + printPerFeature
        print(printPerFeature)
if __name__ == '__main__':
    main()

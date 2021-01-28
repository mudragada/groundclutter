import requests
import json
import csv

def main():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    header = {'content-type' : 'application/json' }
    response = requests.get(url, headers=header, timeout = 5)
    respDict = response.json()
    fileName = './population.csv'
    try:
        if(response.status_code == 200):
            print(respDict)
            with open(fileName, 'w') as csvfile:
                csv_columns = ["ID Nation", "Nation", "ID Year", "Year", "Population", "Slug Nation"]
                csv_writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
                csv_writer.writeheader()
                listOfDicts = respDict['data']
                # print(listOfDicts)
                for dicto in listOfDicts:
                    csv_writer.writerow(dicto)

    except IOError:
        print("IO error")





if __name__ == '__main__':
    main()

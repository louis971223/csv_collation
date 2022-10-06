import json
import csv


# Function to convert a CSV to JSON
def csv_to_json(csvFilePath, jsonFilePath):
    # create a dictionary
    jsonArray = []

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            jsonArray.append(rows)

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonArray, indent=4))


csvFilePath = r'k1.csv'
jsonFilePath = r'k1.json'

# Call the make_json function

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_to_json(csvFilePath, jsonFilePath)
    test = open('k1.json', encoding="utf8")
    data = json.load(test)

    # query
    query = '金門縣烈嶼鄉上岐國民小學附設幼兒園'
    for i in data:
        if query == i.get('學校名稱'):
            print(f"{query}的電話是{i.get('電話')}")

    area = []
    for k in data:
        char1 = '['
        char2 = ']'
        addressStr = k.get('地址')
        numberStr = addressStr[addressStr.find(char1) + 1: addressStr.find(char2)]
        area.append(numberStr)
    # print(area)

    areaList = list(enumerate(area, 0))
    areaList_sorted = sorted(areaList, key=lambda s: s[1], reverse=True)
    # print(areaList_sorted)

    for i in areaList_sorted:
        j = i[0] - 1
        print(f"{data[j].get('學校名稱')}是{data[j].get('公/私立')}學校，地址是{data[j].get('地址')}，電話:{data[j].get('電話')}")

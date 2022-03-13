import json 
import csv 
import xml.etree.ElementTree as ET

def changeFormat(fileName, formatType): 
    if (formatType == '-c'): 
        with open(fileName, newline='') as file:
            fileReader = csv.reader(file, delimiter='\t')
            newFile = open("Information.csv", "x")
            csvWriter = csv.writer(newFile)
            for x in fileReader: 
                csvWriter.writerow(x)
            newFile.close()
    if (formatType == '-j'): 
        array = {}
        with open(fileName) as file:
            for line in file: 
                description1 = list(line.strip().split(None, 39))
                break
            l = 1
            for line in file: 
                description = list(line.strip().split(None, 38))
                block ='Player'+str(l)
                
                i = 0
                information = {}
                while i<len(description):
                    information[description1[i]]= description[i]
                    i = i + 1
                
                array[block] = information
                l = l + 1
        newFile = open("Information.json", "x")
        json.dump(array, newFile, indent=4)
        newFile.close()

    if (formatType == '-x'): 
        with open(fileName, newline='') as file:
            fileReader = csv.reader(file, delimiter='\t')
            newFile = open("Information.xml", "x")
            csvWriter = csv.writer(newFile)
            for x in fileReader: 
                csvWriter.writerow(x)
            newFile.close()



print("What format do you want it in? ")
print("XML: -x")
print("JSON: -j")
print("CSV: -c")
formatKey = input("Enter the appropriate format choice here: ")
changeFormat("Information.txt", formatKey)
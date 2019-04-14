import os
import pandas as pd
import numpy as np
import csv

rootLocation = "/home/rijesh/Documents/machine-learning/project/data"
targetLocation = "/home/rijesh/Documents/machine-learning/project/ust-machine-learning-project/merged_data_09_to_18.csv"

def getFilesInFolder():
    fileNames = []
    for x in os.listdir(rootLocation):
      fileLoc = os.path.join(rootLocation, x)
      if os.path.isfile(fileLoc):
        fileNames.append(fileLoc)
    fileNames.sort(key=lambda s: int(s[6+ s.find("season"):-4]))
    return fileNames


def iterate():
  fileNames = getFilesInFolder()
  for curfile in fileNames:
    print("Starting file cat: ", curfile)
    f = pd.read_csv(curfile)
    for index ,row in f.iterrows():
      if index % 1000 == 0:
        print("completed 1000 rows")
      writeToCsv(row)


def writeToCsv(row):
  with open(targetLocation, "a+") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(row)


iterate()



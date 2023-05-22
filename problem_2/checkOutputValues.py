import os

#Check a file for missing 
def checkOutputs(fileName):
    #Open the file
    f = open(fileName,"r")
    #Get the data values from the file
    dataValues = f.readline().split("\t")
    #Loop through the data values and check that each one contains a valid entry
    for i in range(len(dataValues)):
        if not dataValues[i]: print "File {0} is missing entry value {1}".format(fileName,i)
    #If there are less than 100 entries in dataValues, report as an issue
    if len(dataValues) < 100: print "{0} has fewer than 100 data entries!".format(fileName)
    f.close()

#Get a list of the valuex files in this directory
files = [f for f in os.listdir(".") if f.startswith("value")]

#Now check each file
for fileInDir in files:
    checkOutputs(fileInDir)


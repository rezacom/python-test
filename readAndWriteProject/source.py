import csv
# For the average
from statistics import mean 
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    averagesDict = OrderedDict()
    averagesList = list()

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for i in reader:
            numberList = list()
            for ii in i[1:]:
                numberList.append(int(ii))
            averagesDict[i[0]] = mean(numberList)
            # averagesDict[i[0]] = sum / (len(i) - 1)
    for key, value in averagesDict.items():
        averagesList.append([key, value])

    with open(output_file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for person in averagesList:
            spamwriter.writerow([person[0], person[1]])

calculate_averages('numbers.csv', 'output.csv')

def calculate_sorted_averages(input_file_name, output_file_name):
    averagesDict = OrderedDict()
    averagesList = list()

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for i in reader:
            numberList = list()
            for ii in i[1:]:
                numberList.append(int(ii))
            averagesDict[i[0]] = mean(numberList)
            # averagesDict[i[0]] = sum / (len(i) - 1)
    for key, value in averagesDict.items():
        averagesList.append([key, value])
    
    # convert tuple to dict and sort list max to min
    dictionary = OrderedDict(sorted(averagesDict.items(), key = lambda kv:(kv[1], kv[0])))

    # write data in file
    with open(output_file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for key, value in dictionary.items():
            spamwriter.writerow([key, value])

calculate_sorted_averages('numbers.csv', 'output.csv')

def calculate_three_best(input_file_name, output_file_name):
    averagesDict = OrderedDict()

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for i in reader:
            numberList = list()
            for ii in i[1:]:
                numberList.append(int(ii))
            averagesDict[i[0]] = mean(numberList)
            
    # convert tuple to dict and sort list max to min
    dictionary = OrderedDict(sorted(averagesDict.items(), key = lambda kv:(kv[1], kv[0])))

    # write data in file
    with open(output_file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(3):
            spamwriter.writerow(dictionary.popitem())

calculate_three_best('numbers.csv', 'output.csv')


def calculate_three_worst(input_file_name, output_file_name):
    averagesDict = OrderedDict()
    averagesList = list()

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for i in reader:
            numberList = list()
            for ii in i[1:]:
                numberList.append(int(ii))
            averagesDict[i[0]] = mean(numberList)
            # averagesDict[i[0]] = sum / (len(i) - 1)
    for key, value in averagesDict.items():
        averagesList.append(value)
    
    averagesList = sorted(averagesList)

    # write data in file
    with open(output_file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for ava in averagesList[:3]:
            spamwriter.writerow([ava])

calculate_three_worst('numbers.csv', 'output.csv')

def calculate_average_of_averages(input_file_name, output_file_name):
    averagesDict = OrderedDict()
    averagesList = list()

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for i in reader:
            numberList = list()
            for ii in i[1:]:
                numberList.append(int(ii))
            averagesDict[i[0]] = mean(numberList)
            # averagesDict[i[0]] = sum / (len(i) - 1)
    for key, value in averagesDict.items():
        averagesList.append(float(value))
    
    meanTotal = mean(averagesList)

    # write data in file
    with open(output_file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([meanTotal])

calculate_average_of_averages('numbers.csv', 'output.csv')
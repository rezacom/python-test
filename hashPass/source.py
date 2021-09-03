import hashlib
import csv
from typing import OrderedDict


def hash_password_hack(input_file_name, output_file_name):

    endResult = OrderedDict()
    with open(input_file_name) as f:
        reader = csv.reader(f)
        userPasswords = dict()
        hashListDic = OrderedDict()

        for i in reader:
            userPasswords[i[1]] = i[0]

        for i in range(1000, 10000):
            encoded = str(i).encode()
            result = hashlib.sha256(encoded).hexdigest()
            hashListDic[result] = i

        for key, value in userPasswords.items():
            endResult[value] = hashListDic.get(key)

    with open(output_file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for key, value in endResult.items():
            spamwriter.writerow([key, value])

hash_password_hack('inputFile.csv', 'output.csv')

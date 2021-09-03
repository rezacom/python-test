from collections import OrderedDict
from statistics import mean


class School:
    count = 0

    ages = list()
    heights = list()
    weights = list()

    def __init__(self, name):
        self.schollName = name
        studentCount = int(input())
        School.count += 1
        School.setStudentAge(self, studentCount)
        School.setStudentHeight(self, studentCount)
        School.setStudentWeight(self, studentCount)

    def setStudentAge(self, studentCount):
        for i in range(studentCount):
            age = int(input("age: "))
            School.ages.append(age)

    def setStudentHeight(self, studentCount):
        for i in range(studentCount):
            height = int(input("height: "))
            School.heights.append(height)

    def setStudentWeight(self, studentCount):
        for i in range(studentCount):
            weight = int(input("weight: "))
            School.weights.append(weight)

        # age, height, weight

# school = School("A")


class Salamat(School):

    def __init__(self):
        schoolA = School("A")
        schoolB = School("B")

        print(mean(schoolA.ages))
        print(mean(schoolA.heights))
        print(mean(schoolA.weights))

        print(mean(schoolB.ages))
        print(mean(schoolB.heights))
        print(mean(schoolB.weights))

        if float(mean(schoolA.heights)) > float(mean(schoolB.heights)):
            print("A")
        elif float(mean(schoolA.heights)) == float(mean(schoolB.heights)):
            if float(mean(schoolA.weights)) > float(mean(schoolB.weights)):
                print("A")
            else:
                print("B")
        else:
            print("B")


salamat = Salamat()

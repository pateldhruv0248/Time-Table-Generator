from pprint import pprint

classes = {'C1', 'C2', 'C3'}

class Faculty:
    def __init__(self, facultyName, numberOfClass) -> None:
        self.facultyName = facultyName
        self.numberOfClass = numberOfClass
        self.timeTable = [[[cls for cls in classes] for i in range(6)] for j in range(5)]

def showFreeSlots(faculty):
    for day in range(5):
        for slot in range(6):
            if len(faculty.timeTable[day][slot]) > 1:
                faculty.timeTable[day][slot] = ['--']

def removeClassFromOtherFaculties(asssignedFaculty, classroom, day, slot):
    for faculty in allFaculties:
        if faculty != asssignedFaculty:
            try:
                faculty.timeTable[day][slot].remove(classroom)
            except:
                pass

def getFacultyTimeTable(faculty):
    for day in range(5):
        for slot in range(6):
            currentSLotArray = faculty.timeTable[day][slot]
            for classroom in range(len(currentSLotArray)):
                assignClass = faculty.timeTable[day][slot][classroom]
                if faculty.numberOfClass[assignClass] > 0:
                    faculty.timeTable[day][slot] = [assignClass]
                    faculty.numberOfClass[assignClass] = faculty.numberOfClass[assignClass] - 1
                    removeClassFromOtherFaculties(faculty, assignClass, day, slot)
                    break
    showFreeSlots(faculty)

def printTimeTable(faculty):
    print('Faculty Name :- ', faculty.facultyName)
    for day in range(5):
        pprint(faculty.timeTable[day])
    print()
F1 = Faculty('F1', {'C1': 3, 'C2': 4,  'C3': 4})
F2 = Faculty('F2', {'C1': 5, 'C2': 7,  'C3': 3})

allFaculties = [F1, F2]
getFacultyTimeTable(F2)
getFacultyTimeTable(F1)
printTimeTable(F2)
printTimeTable(F1)

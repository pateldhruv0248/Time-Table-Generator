from pprint import pprint

classes = {'C1', 'C2', 'C3', 'C4', 'C5', 'C6'}
weekdays = [' Mon  ', ' Tue  ', ' Wed  ', ' Thu  ', ' Fri  ']
Days = 5
Slots = 6

class Faculty:
    def __init__(self, facultyName, numberOfClass) -> None:
        self.facultyName = facultyName
        self.numberOfClass = numberOfClass
        self.timeTable = [[[cls for cls in classes] for i in range(Days)] for j in range(Slots)]

def showFreeSlots(faculty):
    for slot in range(Slots):
        for day in range(Days):
            if len(faculty.timeTable[slot][day]) > 1:
                faculty.timeTable[slot][day] = ['--']

def removeClassFromOtherFaculties(asssignedFaculty, classroom, day, slot):
    for faculty in allFaculties:
        if faculty != asssignedFaculty:
            try:
                faculty.timeTable[day][slot].remove(classroom)
            except:
                pass

def getFacultyTimeTable(faculty):
    for slot in range(Slots):
        for day in range(Days):
            currentSLotArray = faculty.timeTable[slot][day]
            for classroom in range(len(currentSLotArray)):
                assignClass = faculty.timeTable[slot][day][classroom]
                if faculty.numberOfClass[assignClass] > 0:
                    faculty.timeTable[slot][day] = [assignClass]
                    faculty.numberOfClass[assignClass] = faculty.numberOfClass[assignClass] - 1
                    removeClassFromOtherFaculties(faculty, assignClass, slot, day)
                    break
    showFreeSlots(faculty)

def printTimeTable(faculty):
    print('Faculty Name :- ', faculty.facultyName)
    print(*weekdays)
    for slot in range(Slots):
        print(*faculty.timeTable[slot])
    print()

#input of every faculty member, showing total number of lectures to be taught every week.
F1 = Faculty('Faculty 1', {'C1': 3, 'C2': 4,  'C3': 4, 'C4':3, 'C5':2, 'C6':4})
F2 = Faculty('Faculty 2', {'C1': 5, 'C2': 7,  'C3': 6, 'C4':2, 'C5':3, 'C6':3})
F3 = Faculty('Faculty 3', {'C1': 2, 'C2': 7,  'C3': 5, 'C4':5, 'C5':0, 'C6':1})
F4 = Faculty('Faculty 4', {'C1': 2, 'C2': 2,  'C3': 5, 'C4':7, 'C5':6, 'C6':4})

allFaculties = [F1, F2, F3, F4]

for faculty in allFaculties:
    getFacultyTimeTable(faculty)
    printTimeTable(faculty)

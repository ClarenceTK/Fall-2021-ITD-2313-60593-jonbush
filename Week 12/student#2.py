import random
class Student(object):



    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
            return self.name

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self._scores)

    

    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "Name: " + self.name     + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
         return self.name >= other.name

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

def main():



    names = {'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen', 'John ', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph ', 'Thomas', 'Charles', 'Christopher', 'Daniel'}
    lyst = []

    for _ in range(8):
        name = random.choice(list(names))
        names.remove(name)
        s = Student(name, 3)
        lyst.append(s)

    print('Unsorted list:')
    for s in lyst:
        print(s)
    
    lyst.sort()
    
    print('\nSorted list:')
    for s in lyst:
        print(s)

if __name__ == "__main__":

    main()
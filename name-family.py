class Student:
    courseMarks={}
    def __init__(self, name, family):
        self._name = name
        self._family = family

    def addCourseMark(self,course,mark):
        self.courseMarks[course] = mark

    def average(self):
        ave = sum(self.courseMarks[x] for x in self.courseMarks)
        ave = ave/len(self.courseMarks)
        return ave

def main():
    new_s = Student("susan", "what does this mean? surname?")
    new_s.addCourseMark("math", 90)
    new_s.addCourseMark("Java", 45)
    avg = new_s.average()
    print "new student:", new_s._name, "has average:", new_s.average()


if __name__ == "__main__":
    main()

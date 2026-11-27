from nguyenngocanhthu_2380602193.lab_01.ex04.Student import Student

class StudentManagement:
    
    studentList = []
    
    def generateID(self):
        maxId = 1
        if (self.amountOfStudent() > 0):
            maxId = self.studentList[0]._id
            for st in self.studentList:
                if (maxId < st._id):
                    maxId = st._id
            maxId += 1
        return maxId
    
    def amountOfStudent(self):
        return self.studentList.__len__()
    
    def inputStudent(self):
        studentId = self.generateID()
        name = input("Input name: ")
        sex = input("Input sex: ")
        major = input("Input major: ")
        average_Score = float(input("Input average score: "))
        st = Student(studentId, name, sex, major, average_Score)
        self.rankStudent(st)
        self.studentList.append(st)
        
    def updateStudent(self, studentId):
        st:Student = self.findbyID(studentId)
        if (st != None):
            name = input("Input name: ")
            sex = input("Input sex: ")
            major = input("Input major: ")
            average_Score = float(input("Input average score: "))
            st._name = name
            st._sex = sex
            st._major = major
            st._average_Score = average_Score
            self.rankStudent(st)
        else:
            print("Student with id = ", studentId, " not found!")
            
    def sortByID(self):
            self.studentList.sort(key=lambda st: st._id, reverse=False)
            
    def sortByName(self):
            self.studentList.sort(key=lambda st: st._name, reverse=False)
        
    def sortByAverageScore(self):
            self.studentList.sort(key=lambda st: st._average_Score, reverse=False)
            
    def sortByMajor(self):
            self.studentList.sort(key=lambda st: st._major, reverse=False)
            
    def findByID(self, studentId):
            searchResult = None
            if(self.amountOfStudent() > 0):
                for st in self.studentList:
                    if (st._id == studentId):
                        searchResult = st
            return searchResult
        
    def findByName(self, keyword):
            studentList = []
            if(self.amountOfStudent() > 0):
                for st in self.studentList:
                    if (keyword.upper() in st._name.upper()):
                        studentList.append(st)
            return studentList
        
    def deleteByID(self, studentId):
            isDeleted = False
            st = self.findByID(studentId)
            if (st != None):
                self.studentList.remove(st)
                isDeleted = True
            return isDeleted
        
    def rankStudent(self, st:Student):
            if (st._average_Score >= 8):
                st._rank = "Excellent"
            elif (st._average_Score >= 6.5):
                st._rank = "Good"
            elif (st._average_Score >= 5):
                st._rank = "Average"
            else:
                st._rank = "Weak"
    
    def displayStudent(self, studentList):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Average Score", "Rank"))
        if(studentList.__len__() > 0):
            for st in studentList:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(st._id, st._name, st._sex, st._major, st._average_Score, st._rank))
        print("\n")
        
    def getListStudent(self):
        return self.studentList
            
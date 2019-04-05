import abc


class PersonalInformationInterface():
    def setPhoneNumber(self, p):
        pass

    def getPhoneNumber(cls):
        pass

    def setName(self, p):
        pass

    def getName(cls):
        pass

    def setAge(self, p):
        pass

    def getAge(cls):
        pass

    def setBirthday(self, p):
        pass

    def getBirthday(cls):
        pass

    def setProfession(self, p):
        pass

    def getProfession(cls):
        pass

    def setSex(self, p):
        pass

    def getSex(cls):
        pass

    def setHeight(cls, p):
        pass

    def getHeight(cls):
        pass

    def setWeight(cls, p):
        pass

    def getWeight(cls):
        pass

    def setBust(cls, p):
        pass

    def getBust(cls):
        pass

    def setWaistline(cls, p):
        pass

    def getWaistline(cls):
        pass

    def setHipline(cls, p):
        pass

    def getHipline(cls):
        pass

    def setShoulderwidth(cls, p):
        pass

    def getShoulderwidth(cls):
        pass

    class Meta:
        abstract = True


class CustomerInterface():
    def isAdministrator(self):
        pass

    def checkAuthority(self, password):
        pass

    def setPassword(self, password):
        pass

    class Meta:
        abstract = True

class SecurityQAInterface():
    def getRandomSecurityQuestionNumber(self):
        pass
    def checkSecurityQA(self,Qnum,Ans):
        pass
    class Meta:
        abstract=True


class CourseInterface():
    def setCourseName(self, p):
        pass

    def getCourseName(cls):
        pass

    def setCourseIntroduction(self, p):
        pass

    def getCourseIntroduction(cls):
        pass

    def setCoursePrice(self, p):
        pass

    def getCoursePrice(cls):
        pass

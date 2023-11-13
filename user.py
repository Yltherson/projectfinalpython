class User:
    fullName = ""
    age = ""
    numero = ""
    email = ""
    fact = ""

    def __init__(self, fullname, age, num, mail, fact) -> None:
        super().__init__()
        self.fullName = fullname
        self.age = age
        self.numero = num
        self.email = mail
        self.fact = fact

    def setFullName(self, name):
        self.fullName = name

    def getFullName(self):
        return self.fullName

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setNumero(self, num):
        self.numero = num

    def getNumero(self):
        return self.numero

    def setEmail(self, mail):
        self.email = mail

    def getEmail(self):
        return self.email

    def setFact(self, fact):
        self.fact = fact

    def getFact(self):
        return self.fact

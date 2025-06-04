class idk:
    def __init__(self,name,section,language=""):
        self.name = name
        self.section = section
        self.language = language
        print("I am creating an object")


obj2 = idk("Kalpit", 8)
print(obj2.name, obj2.section)

obj3 = idk("Heee", 8, "Java")
print(obj3.name, obj3.section, obj3.language)

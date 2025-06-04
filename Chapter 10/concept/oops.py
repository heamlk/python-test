class idk:
    name="Heehee"
    section=7
    def info(self):
        print(f"The name is {self.name} and section is {self.section}")
    @staticmethod
    def heehee():
        print("Heehee as i said")

obj = idk()
obj.salary=120000
print(obj.name, obj.section, obj.salary)
# salary is a instance(object) attribute, name/section is a class attribute

obj2 = idk()
obj2.section=9
print(obj2.name, obj2.section)
# instance attribute takes over class attribute

obj3 = idk()
print(obj3.name, obj3.section)
obj3.info() # this is equal to - idk().info(obj3)
idk.info(obj3) # this is equal to - obj3.info()
obj3.heehee()


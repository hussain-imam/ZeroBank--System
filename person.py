class Person:
    def __init__(self,name,age,cnic):
        self.name=name.strip()
        self.age=age
        self.cnic=cnic

    def __str__(self):

        return f"Name: {self.name} | Age: {self.age} | CNIC: {self.cnic}"
    def to_dict(self):
        return {
            "name":self.name,
            "age":self.age,
            "CNIC":self.cnic
        }
    @staticmethod
    def from_dict(data):
        return Person(data['name'], data['age'], data['CNIC'])
    

 



    
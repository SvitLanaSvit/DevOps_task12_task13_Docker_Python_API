class Student:
    def __init__(self, id, first_name, last_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

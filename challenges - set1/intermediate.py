"""
Intermediate challenge: Write a class for a car, the class should have the following as arguments:
-> Weight
-> Wheels
-> Passengers
-> Model number
-> Car manufacturor
Challenge 2: Introduce type hinting; weight is int, wheels is int, passengers is int, model number is int, car manufacturor is str
Challenge 3: when a user runs `print(car_object)` respond with `Car weight : <weight> ¦ Car wheels : <wheels> ¦ Passengers : <passengers> ¦ Model Number : <model_number>`
"""

class car:
    def __init__(self,weight:int, wheels:int, passengers:int,model_number:int,car_manufacturor:str):
        self.weight = weight
        self.wheels = wheels
        self.passengers = passengers
        self.model_number=model_number
        self.car_manufacturor = car_manufacturor

    def __repr__(self):
        return f"Car weight : {self.weight} ¦ Car wheels : {self.wheels} ¦ Passengers :{self.passengers} ¦ Model Number : {self.model_number}"

car_obj = car(weight=20, wheels=4, passengers=4,model_number=32789,car_manufacturor='nissan')
print(car_obj)
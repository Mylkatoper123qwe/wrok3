import random
#Class People
class People:
    def __init__(self,name ="People", job=None , home=None , car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
#Def
    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def get_eat(self):
        pass

    def get_work(self):
        pass

    def shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass
#Class Auto
class Auto:
    def __init__(self,brand_list):

        self.brand=random.choice(list(brand_list))

        self.fuel=brand_list[self.brand]["fuel"]

        self.strengh = brand_list[self.brand]["Strenght"]

        self.consumption=brand_list[self.brand]["Consumption"]

#Brands_Car
    brands_of_car = {
 "BMW":{"fuel":100, "strength":100,"consumption": 6},

 "Lada" :{"fuel":50, "strength":40,"consumption": 10},

 "Volvo" :{"fuel":70, "strength":150,"consumption": 8},

 "Ferrari" :{"fuel":80, "strength":120,"consumption": 14}, }


#Drive
    def drive(self):
        if self.strengh>0 and
            self.fuel>=self.consumption:
            self.fuel-=self.consumption
            self.strengh-=1
            return  True
        else:
            print("The car cannot move")
            return False

#Class House
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
#Class Job
class Job:
    def __init__(self,job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list












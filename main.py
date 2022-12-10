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
        if self.strengh>0 and self.fuel>=self.consumption:
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
        self.salary=job_list[self.job]["salary"]
        self.gladnees_less=job_list[self.job]["Gladness_less"]

#Job_list
job_list = {
    "Java developer":
    {"Salary":50, "gladness_less": 10 },
    "Python developer":
    {"salary":40,"gladness_less": 3 },
    "C++ developer":
    {"salary":45,"gladness_less": 25},
    "Rust Developer":
    {"salary":70,"gladness_less": 1}
}

#Metod pull house
def get_home(self):
    self.home = House()
def get_car(self):
    self.car = Auto(brands_of_car)
def get_job(self):
    if self.car.drive():
        pass
    else:
        self.to_repair()
        return
    self.job = Job(job_list)

#Eat
def eat(self):
    if self.home.food <=0:
        self.shopping("food")
    else:
        if self.satiety >=100:
            self.satiety = 100
            return
        self.satiety+=5
        self.home.food-=5

#Def work
def work(self):
    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            self.shopping("fuel")
            return
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladnees_less
        self.satiety -=4

#Metod Byu
def shopping(self, manage):
    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            manage = "fuel"
        else:
            self.to.repair()
            return
        if manage == "fuel":
            print("I bought fuel")
            self.money -=100
            self.car.fuel +=100
        elif manage == "food":
            print("Bought food")
            self.money -=50
            self.home.food +=50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness+=10
            self.satiety+=2
            self.money-=15
#Metod Chill
def chill(self):
    self.gladness+=10
    self.home.mess+=5

def clean_home(self):
    self.gladness-=5
    self.home.mess = 0

def to_repair(self):
    self.car.strenght+=100
    self.money-=50
#Parametr vivod
def days_indexes(self,day):
    day = f"Today the {day} of {self.name}'s life"
    print(f"{day:=50}","\n")
    human_indexes = self.name + "'s indexes"
    print(f"{human_indexes:50}","\n")
    print(f"Money - {self.money}")
    print(f"Satiety - {self.satiety}")
    print(f"Gladness - {self.gladness}")
    home_indexes = "Home indexes"
    print(f"{home_indexes:50}","\n")
    print(f"Food - {self.home.food}")

#Workout Classes
print(f"Mess - {self.home.mess}")
car_indexes = f"{self.car.brand} car indexes"
print(f"{car_indexes:50}", "\n")
print(f"Fuel - {self.car.fuel}")
print(f"Strenght - {self.car.strenght}")

#Def alive
def is_alive(self):
    if self.gladness<0:
        print("Depression...")
        return False
    if self.satiety<0:
        print("Dead...")
        return False
    if self.money<-500:
        print("Bankrupt...")
        return False

#Simyliation
def live (self,day):
    if self.is_alive() == False:
        return False
    if self.home is None:
        print("Settled in the house")
        self.get_home()
    if self.car is None:
        self.get_car()
        print(f"I bought a car {self.car.brand}")
    if self.job is None:
        self.get_job()
        print(f"I don't have a job,I'm going to get  a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)

#Zanatia day
dice = random.randint(1,4)
if self.satiety<20:
    print("I'll go eat")
    self.eat()
elif self.gladness < 20:
    if self.home.mess>15:
        print("I want to chill , but there is  so much mess..\nSo I will clean to the house")
        self.clean_home()
    else:
        print("Let's chill!")
        self.chill()
elif self.money<0:
    print("Start working ")
    self.work()
elif self.car.strenght<15:
    print("I need to repair my car")
    self.to_repair()

#Don dice
elif dice == 1:
    print("Let's chill")
    self.chill()
elif dice == 2:
    print("Start working")
    self.work()
elif dice == 3:
    print("Cleaning time!")
    self.clean_home()
elif dice == 4:
    print("Time for treats!")
    self.shopping(manage="delicacies")

#Object men
















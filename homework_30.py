import time
import math
class Car:
    ID = 0
    def __init__(self):
        Car.ID += 1
        self.id = Car.ID


class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.cars = {}
        self.summa = 0

    def park(self, car: Car):
        start_time = time.time()
        self.cars[car.ID] = start_time

    def release(self, car):
        if car.ID in self.cars:
            self.summa += math.ceil(time.time() - self.cars[car.ID]) * 500
            self.cars.pop(car.ID)
        else:
            return "Car not found"
    def spots_left(self):
        return self.total_spots - len(self.cars)

    def cash_register(self):
        return self.summa
    

car1 = Car()
car2 = Car()
car3 = Car()
p = ParkingLot(5)
p.park(car1)
time.sleep(1)
print(p.spots_left())
print(p.cash_register())
p.park(car2)
time.sleep(1)
print(p.spots_left())
p.release(car2)
print(p.cash_register())
p.release(car3)



#2
# class MyShow:
#     def __init__(self, name, channel, year, casts, episode = 1, rate = None):
#         if not(isinstance(name, str)):
#             raise Exception("Wrong name")
#         if not(isinstance(channel, str)):
#             raise Exception("Wrong channel")
#         if not(isinstance(year, int) and 1990 < year < 2024):
#             raise Exception("Wrong year")
#         if not(isinstance(episode, int)):
#             raise Exception("Wrong episode number")
#         if not(isinstance(rate, int) and 1 <= rate<= 10):
#             raise Exception("Wrong rate")
#         if not(isinstance(casts, list)):
#             raise Exception("Wrong casts")
#         self.__name = name
#         self.__channel = channel
#         self.__year = year
#         self.__episode = episode
#         self.__rate = rate
#         self.__casts = casts

#     @property
#     def name(self):
#         return f"name: {self.__name}"
    
#     @property
#     def channel(self):
#         return f"channel: {self.__channel}"
    
#     @property
#     def year(self):
#         return f"year: {self.__year}"
    
#     @property
#     def episode(self):
#         return f"episode: {self.__episode}"
    
#     @episode.setter
#     def episode(self, ep):
#         if not(isinstance(ep, int)):
#             return "Wrong episode number"
#         self.__episode = ep 
    
#     @property
#     def rate(self):
#         return f"rate: {self.__rate}"
    
#     @rate.setter
#     def rate(self, rt):
#         if not(isinstance(rt, int) and 1 <= rt <= 10):
#             self.__rate = "Wrong rate"
#         else:
#             self.__rate = rt
    
#     @rate.deleter
#     def rate(self):
#         self.__rate = None
    
#     @property
#     def casts(self):
#         return f"casts: {self.__casts}"
    

#     def add_casts(self, cast):
#         self.__casts.append(cast)
    
#     def casts_remove(self, cast):
#         self.__casts.pop(self.__casts.index(cast))



# show1 = MyShow("Kassandra", "ArmeniaTV", 1992, ["Coraima Torres", "Osvaldo Rios", "Henry Soto"], 100, 10)

# print(show1.name)
# print(show1.channel)
# print(show1.year)
# print(show1.casts)
# print(show1.episode)
# show1.episode = 1
# print(show1.episode)
# print(show1.rate)
# del show1.rate
# print(show1.rate)
# show1.rate = 9
# print(show1.rate)
# show1.add_casts("Alexander Milic")
# print(show1.casts)
# show1.casts_remove("Alexander Milic")
# print(show1.casts)



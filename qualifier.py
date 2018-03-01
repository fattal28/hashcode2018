import random, re, math
a = "a_example.in"
b = "b_should_be_easy.in"
c = "c_no_hurry.in"
d = "d_metropolis.in"
e = "e_high_bonus.in"
fileName = d
inputFile = open(fileName, mode='r')
rawData = [] 
def printArray(array):
    for subarray in array:
        print(subarray)
def getTime(data): # minimum finish time
    return data[4]+abs(data[2]-data[0])+abs(data[3]-data[1])

for line in inputFile:
    rawData.append([int(s) for s in line[:-1].split(' ')])

map = []
mapData = rawData.pop(0)
VEHICLES = mapData[2]
RIDE_NUMBER = mapData[3]
BONUS = mapData[4]

for i in range(mapData[0]):
    map.append([])
    for j in range(mapData[1]):
        map[i].append([])



class Car:
    def __init__(self, ride):
        self.rides = [ride]
        self.ride_ids = [ride.ride_id]
        
    def addRide(self, ride):
        self.rides.append(ride)

    def returnList(self):
        res = list(self.ride_ids)
        return res

class Ride:
    def __init__(self, data, ride_id):
        self.ride_id = ride_id
        self.ride_length = abs(data[2]-data[0])+abs(data[3]-data[1])
        self.earliest_time = data[4]
        self.latest_time = data[5]

    def show(self):
        return self.ride_length, self.earliest_time, self.latest_time


#printArray(map)
#printArray(rawData)

    


rides = [Ride(rawData[i], i) for i in range(len(rawData))]
cars = [Car(ride) for ride in rides]

outputFile = open("output" + fileName + ".out", mode="w")
for car in cars:
    res = str(len(car.ride_ids)) + ' ' + ' '.join(str(x) for x in car.ride_ids) + "\n"
    outputFile.write(res)
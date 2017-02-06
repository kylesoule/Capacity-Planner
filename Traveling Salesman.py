#http://www.theprojectspot.com/tutorial-post/applying-a-genetic-algorithm-to-the-travelling-salesman-problem/5

import random, math
from datetime import datetime

startTime = datetime.now()


class Tour:
    cities = {}
    
    def __init__(self):
        for i in xrange(0, len(city_list)):
            self.cities["C{city}".format(city=len(self.cities))] = [None, None]
    
    def parseCities(self, city_list):
        for city in city_list.split(" "):
            x, y = city_list[city]
            self.addCityByName(city, x, y)
    
    def encodeTour(self):
        encoded = []
        for city in self.cities.keys():
            encoded.append(city)
        return " ".join(encoded)
    
    def addCityByName(self, name, x, y):
        self.cities[name] = [x, y]
    
    def addCity(self, x, y):
        for i in xrange(0, self.getSize()):
            if self.cities["C{city}".format(city=i)] == [None, None]:
                self.cities["C{city}".format(city=i)] = [x, y]
    
    def getCityByPlace(self, place):
        return self.cities.get(place)

    def getCityByName(self, city):
        if city[:1] != "C":
            city = "C{city}".format(city=city)
        return self.cities[city]

    def getSize(self):
        return len(self.cities)
    
    def getFitness(self):
        return 1.0 / self.measure()

    def measure(self):
        cities = self.cities
        x, y = [0, 0]
        distance = 0
    
        for city, point in cities.items():
            distance += math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            x, y = point
        return distance
        
def fitness_proportionate_selection():
    max = sum(choices.values())
    pick = random.uniform(0, max)
    current = 0
    for key, value in choices.items():
        current += value
        if current > pick:
            return key

def begin_touring():
    parent1 = fitness_proportionate_selection()
    parent2 = fitness_proportionate_selection()
    
    child = crossover(parent1, parent2)

def crossover(parent1, parent2):
    child = Tour()

def new_seed(size):
    seed = [None]*size
    for i in xrange(0, size):
        seed[i] = str(random.randint(0, 1))
    return seed

def random_seed(size):
    while True:
        seed = new_seed(size)
        if is_form_valid(seed):
            break
    
    return "".join(seed)

def is_form_valid(seed_list):
    zero = 0
    for seed in seed_list:
        if seed == "0":
            zero += 1
    
    if zero > 1 and zero < 9:
        return True
    else:
        return False

def evaluate(member):
    # 0 = deck 1 = sum to 36
    # 1 = deck 2 = product to 360
    members = list(member)
    stack_a = 0
    stack_b = 1
    
    for i in xrange(0, len(members)):
        if members[i] == "0":
            stack_a += (i + 1)
        else:
            stack_b *= (i + 1)
    
    error = (solution_a - stack_a) + (solution_b - stack_b)
    
    #print "{stack}:\tE:{e}\tA:{a}\tB:{b}".format(stack=member, e=error, a=stack_a, b=stack_b)
    return error, stack_a, stack_b

def breed(member):
    rand_xover = random.uniform(0, 1)
    member_list = list(member)
    
    if rand_xover <= crossover_rate:
        xover_start = random.randint(0, len(member_list))
        for i in xrange(0, len(member_list)):
            rand_mutate = random.uniform(0, 1)
            
            if i >= xover_start or rand_mutate <= mutation_rate:
                if member_list[i] == "0":
                    member_list[i] = "1"
                else:
                    member_list[i] = "0"
        
        member = "".join(member_list)

        if is_form_valid(member):
            ev = evaluate(member)[0]
            if ev != 0:
                choices[member] = 1.0 / abs(ev)
            else:
                choices[member] = 1.0
    else:
        for i in xrange(0, len(member_list)):
            rand_mutate = random.uniform(0, 1)
            
            if rand_mutate <= mutation_rate:
                if member_list[i] == "0":
                    member_list[i] = "1"
                else:
                    member_list[i] = "0"
        
        member = "".join(member_list)
        
        if is_form_valid(member):
            ev = evaluate(member)[0]
            if ev != 0:
                choices[member] = 1.0 / abs(ev)
            else:
                choices[member] = 1.0

    return fitness_proportionate_selection()


crossover_rate = 0.7
mutation_rate = 0.1

city_list = { "C0": [20  , 20]  ,
              "C1": [60  , 20]  ,
              "C2": [20  , 40]  ,
              "C3": [40  , 120] ,
              "C4": [60  , 80]  ,
              "C5": [60  , 200] ,
              "C6": [100 , 120] ,
              "C7": [80  , 180] ,
              "C8": [140 , 140] ,
              "C9": [20  , 160] ,
             "C10": [100 , 160] ,
             "C11": [120 , 80]  ,
             "C12": [140 , 180] ,
             "C13": [180 , 60]  ,
             "C14": [180 , 200] ,
             "C15": [160 , 20]  ,
             "C16": [180 , 100] ,
             "C17": [100 , 40]  ,
             "C18": [200 , 160] ,
             "C19": [200 , 40]  }

tour = Tour()

for key, val in city_list.items():
    x, y = val
    tour.addCity(x, y)

best = ["START", 0]
choices = {tour.encodeTour(): tour.getFitness()}

test = 0

while True:
    if test == 1000:
        print best
        break
    else:
        begin_touring()
    test += 1

'''
# Genetic algorithm
stack_a = random_seed(10)

solution_a = 36
solution_b = 360

crossover_rate = 0.2
mutation_rate = 0.7

choices = {stack_a: 1.0 / evaluate(stack_a)[0]}

runs = 0

while True:
    if evaluate(stack_a)[0] == 0:
        print stack_a
        #for i in xrange(0, len(stack_a)):
        #    sys.stdout.write("{p} ".format(p=(i + 1)))
        #sys.stdout.write("= {s}\n".format(s=0))
        
        startTime = datetime.now()
        break
    else:
        stack_a = breed(stack_a)
    #runs += 1
    #if runs == 1000:
    #    for key, val in choices.items():
    #        print "{k}\t{v}".format(k=key, v=val)
    #    break

print "Execution time: {t}".format(t = datetime.now() - startTime)
'''
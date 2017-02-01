# https://www.codeproject.com/Articles/16286/AI-Simple-Genetic-Algorithm-GA-to-solve-a-card-pro

import random, sys
from datetime import datetime

startTime = datetime.now()


int_pop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pop = [ "0001", # 1
        "0010", # 2
        "0011", # 3
        "0100", # 4
        "0101", # 5
        "0110", # 6
        "0111", # 7
        "1000", # 8
        "1001", # 9
        "1010"] # 10

lup = { "0001": 1,
        "0010": 2,
        "0011": 3,
        "0100": 4,
        "0101": 5,
        "0110": 6,
        "0111": 7,
        "1000": 8,
        "1001": 9,
        "1010": 10 }

def fitness_proportionate_selection():
    max = sum(choices.values())
    pick = random.uniform(0, max)
    current = 0
    for key, value in choices.items():
        current += value
        if current > pick:
            return key

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
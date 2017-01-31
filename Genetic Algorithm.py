import random, sys
from datetime import datetime

startTime = datetime.now()


pop = [ "0001", # 1
        "0010", # 2
        "0011", # 3
        "0100", # 4
        "0101", # 5
        "0110", # 6
        "0111", # 7
        "1000", # 8
        "1001", # 9
        "1010", # +
        "1011", # -
        "1100", # *
        "1101"] # /

lup = { "0001": 1,
        "0010": 2,
        "0011": 3,
        "0100": 4,
        "0101": 5,
        "0110": 6,
        "0111": 7,
        "1000": 8,
        "1001": 9,
        "1010": "+",
        "1011": "-",
        "1100": "*",
        "1101": "/"}

def fitness_proportionate_selection(choices):
    max = sum(choices.values())
    pick = random.uniform(0, max)
    current = 0
    for key, value in choices.items():
        current += value
        if current > pick:
            return key

def random_seed(size):
    # Only returns valid form seeds
    seed = ""
    for i in xrange(0, size):
        if i == 0:
            seed = pop[random.randint(0, len(pop) - 1)]
        else:
            seed = seed + " " + pop[random.randint(0, len(pop) - 1)]
    
    if is_form_valid(seed):
        return seed
    else:
        random_seed(size)

def is_form_valid(member):
    # Expected form is value, operator, ...
    valid = True
    parts = member.split(" ")
    for i in xrange(0, len(parts)):
        if i % 2 == 1:
            if int(parts[i], 2) < 10:
                valid = False
        else:
            if int(parts[i], 2) > 9:
                valid = False
    return valid

def evaluate(member):
    parts = member.split(" ")
    p_val = int(parts[0], 2)
    val = 0.0 + p_val
    op = 0

    for i in xrange(0, len(parts)):
        if i % 2 == 1:
            op = int(parts[i], 2)
        else:
            p = int(parts[i], 2)
            if op == 10:
                val += p
            elif op == 11:
                val -= p
            elif op == 12:
                val *= p
            elif op == 13:
                val /= p
    return val

def breed(member):
    rand_xover = random.uniform(0, 1)
    rand_mutate = random.uniform(0, 1)
    
    if rand_xover <= crossover_rate:
        xover_start = random.randint(0, len(member))
        
        for i in xrange(0, len(member) - 1):
            if member[i] != " ":
                if i >= xover_start or rand_mutate <= mutation_rate:
                    if member[i] == "0":
                        member[i] = "1"
                    else:
                        member[i] = "0"
    return member
            

# Genetic algorithm
member_a = random_seed(9)
criteria = 23
crossover_rate = 0.7
mutation_rate = 0.001

while True:
    if evaluate(member_a) == criteria:
        print member_a
        for pc in member_a.split(" "):
            sys.stdout.write("{p} ".format(p=lup[pc]))
        sys.stdout.write("= {s}\n".format(s=criteria))
    else:
        member = breed(member_a)
        
# Brute force
'''
while True:
    member_a = random_seed(9)

    if is_form_valid(member_a):
        result = evaluate(member_a)
        
        if result == 23:
            print member_a
            for pc in member_a.split(" "):
                sys.stdout.write("{p} ".format(p=lup[pc]))
            sys.stdout.write("= {s}\n".format(s=result))
            break
# Benchmarks: 0.9s, 5.1s, 1.5s, 4.9s
'''

print "Execution time: {t}".format(t = datetime.now() - startTime)
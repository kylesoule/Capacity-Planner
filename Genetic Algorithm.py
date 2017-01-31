import random

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

def fitness_proportionate_selection(choices):
    max = sum(choices.values())
    pick = random.uniform(0, max)
    current = 0
    for key, value in choices.items():
        current += value
        if current > pick:
            return key

def random_seed(size):
    seed = ""
    for i in xrange(0, size):
        seed = seed + " " + pop[random.randint(0, len(pop) - 1)]
    return seed.strip()

member_a = random_seed(9)
member_b = random_seed(9)

print member_a
print member_b
'''
choices = {"Test 1": 0.1,
           "Test 2": 0.2,
           "Test 3": 0.3,
           "Test 4": 0.4,
           "Test 5": 14,
           "Test 6": 8,
           "Test 7": 0.7,
           "Test 8": 0.8,
           "Test 9": 0.9,
           "Test 10": 0.5}

selection = [0,0,0,0,0,0,0,0,0,0]
for i in xrange(0, 1000000):
    selected = weighted_random_choice(choices)
    selection[int(selected.replace("Test ", "")) - 1] += 1

c = 0
for select in selection:
    print "{c}\t{select}".format(c=c, select=select)
    c += 1
'''
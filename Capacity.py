
# Available runtime in a day (hours)
hours = 24

# {Part: Demand}
demand = {'1300031': 1628,
          '2202251': 1686,
          '2222561': 272,
          '3580498': 404,
          '3802704': 310,
          '3802788': 265}

# TODO: Write a Class
# {Part: [Runtime, Setup Time, Min Plan Days, Max Plan Days]}
parts = {'1300031': [0.02463, 1.0, 3, 20],
         '2202251': [0.02009, 1.0, 3, 20],
         '2222561': [0.02171, 1.0, 3, 20],
         '3580498': [0.01653, 1.0, 3, 20],
         '3802704': [0.02657, 1.0, 3, 20],
         '3802788': [0.02657, 1.0, 3, 20]}

# {Machine: [Part List,...]}
machines = {'M 004277': ['1300031', '3802704', '3802788'],
            'M 004183': ['1300031', '3802704', '3802788'],
            'M 004234': ['1300031', '2202251', '3802704', '3802788'],
            'M 004262': ['2202251', '2222561', '3580498', '3802704', '3802788'],
            'M 004233': ['1300031', '2202251', '2222561', '3580498', '3802704', '3802788']}

for machine in list(machines.keys()):
    for part in machines[machine]:
        print("{machine}\t{part}\t\t{rt}\t\t{demand}".format(machine=machine,
                                                           part=part,
                                                           rt=parts[part][0],
                                                           demand=demand[part]))


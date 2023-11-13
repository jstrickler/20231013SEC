
d1 = dict()

airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

d2 = {}
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)

pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
         ('Oregon', 'Salem'), ('California', 'Sacramento')]

state_caps = dict(pairs)

print(d3['red'])
print(airports['LAX'])

airports['SLC'] = 'Salt Lake City'
airports['LAX'] = 'Lost Angels'
print(airports['SLC'])  # print value where key is 'SLC'

code = 'PSP'

if code in airports:   # is key in dictionary?
    print(airports[code])  # print key if key is in dictionary
else:
    print(f"{code} not in airports")

print(airports.get(code))  # get value if key in dict, otherwise get None
print(airports.get(code, 'NO SUCH AIRPORT'))  # get value if key in dict, otherwise get 'NO SUCH AIRPORT'

print(airports.setdefault(code, 'Palm Springs'))  # get value if key in dict, otherwise get 'Palm Springs' AND set key
print(code in airports)  # check for key in dict

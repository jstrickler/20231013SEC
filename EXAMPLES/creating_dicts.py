
d1 = dict()  # create new empty dict

airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',  # initialize dict with literal key/value pairs (keys can be any string, number or tuple)
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

d2 = {}
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)  # initialize dict with named parameters; keys must be valid identifier names

pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
         ('Oregon', 'Salem'), ('California', 'Sacramento')]

state_caps = dict(pairs)  # initialize dict with an iterable of pairs

print(d3['red'])  # print value for given key
print(airports['LAX'])

airports['SLC'] = 'Salt Lake City'  # assign to new key
airports['LAX'] = 'Lost Angels'  # overwrite existing key
print(airports['SLC'])

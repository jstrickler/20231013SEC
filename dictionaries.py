d1 = dict()  # empty dictionary

d2 = {'a': 35, 'm': 99, 'c': 14}

d3 = {}

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

airports['DCA'] = "Washington, DC"
airports['IAD'] = "Washington, DC"

print(airports['YCC'])
print(airports.get('BWI', "NOT FOUND"))
print(airports.get('BWI'))
print(airports.get('YCC'))


for code, city in airports.items():
    print(code, city)
print()

print(f"airports.keys(): {airports.keys()}")





class Person():

    def __init__(self, firstname=None, lastname=None):
        self.first_name = firstname  # calls property for validation
        self.last_name = lastname    # calls property

    @property
    def first_name(self):  # getter property
        return self._first_name

    @first_name.setter  # decorator comes from getter property
    def first_name(self, value):  # setter property
        if value is None or value.isalpha():
            self._first_name = value
        else:
            raise ValueError("ERROR: First name may only contain letters")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is None or value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last name may only contain letters")

if __name__ == '__main__':
    person1 = Person('Ferneater', 'Eulalia')
    person2 = Person()
    person2.last_name = 'Pepperpot'  # assign to property
    person2.first_name = 'Hortense'

    print(f"{person1.first_name} {person1.last_name}")
    print(f"{person2.first_name} {person2.last_name}")

    try:
        person3 = Person("R2D2")
    except ValueError as err:
        print(err)
    else:
        print(f"{person3.first_name} {person3.last_name}")

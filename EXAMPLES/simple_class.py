
class Simple:  # default base class is object
    def __init__(self, message_text):  # constructor
        self._message_text = message_text  # message text stored in instance object

    def text(self):  # instance method
        return self._message_text


if __name__ == "__main__":
    msg1 = Simple('hello')  # instantiate an instance of Simple
    print(msg1.text())  # call instance method

    msg2 = Simple('hi there')  # create 2nd instance of Simple
    print(msg2.text())

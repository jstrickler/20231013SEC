import sys
import logging

logging.basicConfig(filename='c2f_batch.log', level=logging.WARNING)

try:
    celsius = float(sys.argv[1])
except ValueError as err:
    logging.exception(err)
    print("Invalid temperature")
except IndexError as err:
    logging.exception(err)
    print("Please specify a temperature to convert on the command line")
else:
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

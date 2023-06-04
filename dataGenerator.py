import csv
import random
from random import seed
from random import randint

total_rows = 200000

training_rows = int(total_rows / 100 * 80)
testing_rows = total_rows - training_rows

def calculate_durability(number_of_tooth,heat_dissipation,viscosity_of_lubricant,temperature):
    return number_of_tooth * heat_dissipation * viscosity_of_lubricant / temperature

with open('training.csv', mode = 'w',) as training_file:
    training_writer = csv.writer(training_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    training_writer.writerow(['number_of_tooth', 'heat_dissipation', 'viscosity_of_lubricant', 'temperature', 'durability'])

    for i in range(0, training_rows,1):
        number_of_tooth = randint(10,50)
        heat_dissipation = random.uniform(0.2,0.8)
        viscosity_of_lubricant = randint(1,5)
        temperature = round(random.uniform(18,120),1)
        durability = calculate_durability(number_of_tooth,heat_dissipation,viscosity_of_lubricant,temperature)
        training_writer.writerow([number_of_tooth,heat_dissipation,viscosity_of_lubricant,temperature,durability])

with open('testing.csv', mode = 'w',) as testing_file:
    testing_writer = csv.writer(testing_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    testing_writer.writerow(['number_of_tooth', 'heat_dissipation', 'viscosity_of_lubricant', 'temperature', 'durability'])

    for i in range(0, testing_rows,1):
        number_of_tooth = randint(10,50)
        heat_dissipation = random.uniform(0.2,0.8)
        viscosity_of_lubricant = randint(1,5)
        temperature = round(random.uniform(18,120),1)
        durability = calculate_durability(number_of_tooth,heat_dissipation,viscosity_of_lubricant,temperature)
        testing_writer.writerow([number_of_tooth,heat_dissipation,viscosity_of_lubricant,temperature,durability])

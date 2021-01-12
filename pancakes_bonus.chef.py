from kitchen import Rosemary
# Fetching the required utensils and ingredients
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Milk, Salt, Butter

# How many pancakes do you want to make?
# ATTENTION: Rosemary doesn't like to do a lot of work for little outcome.
# If you tell her to make less than 3 pancakes, she will blow up the kitchen with a non-positive egg!
pancakes = 3

# Getting all utensils ready
bowl = Bowl.use(name = "Perfect batter")
pan = Pan.use('Great pancake')
plate = Plate.use('Serving of amazing pancakes')

# Mixing two cracked eggs per four pancakes into the bowl (rounding)
for egg in Egg.take(round(pancakes*0.25)):
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Adding salt, flour, and milk to the batter
bowl.add(Salt.take(str(round(pancakes/8)) + ' dash(es) of salt'))
# Flour in batches of 31.25 grams (one batch per pancake)
for i in range(pancakes):
    bowl.add(Flour.take(grams = 31.25))
    bowl.mix()
# Milk in two batches of 125 ml (one batch per two pancakes, rounding down)
for milk in range(int(pancakes/2)):
    bowl.add(Milk.take(ml = 125))
    bowl.mix()

# The chosen amount of pancakes are baked from the batter and a little butter
for i in range(pancakes):
    pan.add(Butter.take('a little bit'))
    pan.add(bowl.take('1/' + str(pancakes))) # Fraction of batter to be added is calculated
    # Each pancake is baked for one minute on each side in intervals of 30 seconds
    pan.cook(0.5)
    for ii in range(3):
        pan.flip()
        pan.cook(0.5)
    # Each pancake is added to the stack on the plate
    plate.add(pan.take())

# Our chef serves amazingly delicious pancakes just for you
Rosemary.serve(plate)
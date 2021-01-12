from kitchen import Rosemary
# Fetching the required utensils and ingredients
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Milk, Salt, Butter

# Getting all utensils ready
bowl = Bowl.use(name = "Perfect batter")
pan = Pan.use('Great pancake')
plate = Plate.use('Serving of eight amazing pancakes')

# Mixing two cracked eggs into the bowl
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Adding salt, flour, and milk to the batter
bowl.add(Salt.take('a dash'))
# Flour in five batches of 50 grams
for i in range(5):
    bowl.add(Flour.take(grams = 50))
    bowl.mix()
# Milk in two batches of 125 ml
for milk in range(2):
    bowl.add(Milk.take(ml = 125))
    bowl.mix()

# Eight pancakes are baked from the batter and a little butter
for i in range(8):
    pan.add(Butter.take('a little'))
    pan.add(bowl.take('1/8'))
    # Each pancake is baked for one minute on each side in intervals of 30 seconds
    pan.cook(0.5)
    for ii in range(3):
        pan.flip()
        pan.cook(0.5)
    # Each pancake is added to the stack on the plate
    plate.add(pan.take())

# Our chef can serve eight amazingly delicious pancakes just for you
Rosemary.serve(plate)
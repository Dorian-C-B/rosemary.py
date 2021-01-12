from kitchen import Rosemary
from kitchen.utensils import Bowl, Fridge, BakingTray, Oven, Plate
from kitchen.ingredients import Butter, Sugar, Egg, Salt, Flour, ChocolateChips, BakingPowder

# Getting all utensils ready
bowl = Bowl.use('Tasty cookie dough')
fridge = Fridge.use(degrees = 5)
baking_tray = BakingTray.use('Fresh cookies')
oven = Oven.use()
plate = Plate.use()

# Adding butter and sugar, mixing them together
bowl.add(Butter.take('Packet'))
for i in range(4):
    bowl.add(Sugar.take(grams = 50))
    bowl.mix()

# Adding two cracked eggs to the dough and mix
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Adding a pinch of salt
bowl.add(Salt.take('a pinch'))

# Adding the flour, then the chocolate chips in stages
for i in range(3):
    bowl.add(Flour.take(grams = 100))
    bowl.mix()
for i in range(2):
    bowl.add(ChocolateChips.take(grams = 100))
    bowl.mix()

# Finally, adding some baking powder and mixing for the last time
bowl.add(BakingPowder.take('a teaspoon'))

# Cookies are better when the dough rested in the fridge for a bit
# we can preheat the oven in the meanwhile

fridge.add(bowl)
oven.preheat(degrees = 175)

# Waiting for 10 minutes...

# Taking the bowl from the fridge and scooping the dough to the baking tray
bowl = fridge.take()
baking_tray.add(bowl.take())

# Baking the cookies for ten minutes and taking them out
oven.add(baking_tray)
oven.bake(minutes = 10)
baking_tray = oven.take()

# Waiting for the cookies to cool down and serve on a plate
plate = baking_tray.take()
Rosemary.serve(plate)
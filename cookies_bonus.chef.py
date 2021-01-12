from kitchen import Rosemary
from kitchen.utensils import Bowl, Fridge, BakingTray, Oven, Plate
from kitchen.ingredients import Butter, Sugar, Egg, Salt, Flour, ChocolateChips, BakingPowder

# How many cookies do you want to make?
# ATTENTION: Who wants to eat less than five cookies? Nobody, that's correct.
# The spirits of the kitchen and the cookie monster have decided to let the kitchen explode if anyone dares to try.
cookies = 5

# Getting all utensils ready
bowl = Bowl.use('Tasty cookie dough')
fridge = Fridge.use(degrees = 5)
baking_tray = BakingTray.use('Fresh cookies')
oven = Oven.use()
plate = Plate.use()

# Adding butter and sugar, mixing them together
# Butter is measured by packet, rounding to the first number after the decimal point
bowl.add(Butter.take(str(round(cookies / 16, 1)) + ' packet(s)'))
for i in range(round(cookies / 4)):
    bowl.add(Sugar.take(grams = 50))
    bowl.mix()

# Adding one cracked egg per eight cookies (rounding) to the dough and mix
for egg in Egg.take(round(cookies / 8)):
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Adding a pinch of salt per 16 cookies (rounding)
bowl.add(Salt.take(str(round(cookies / 16)) + ' pinch(es)'))

# Adding the flour, 100 grams per 5.3 cookies (rounding)
for i in range(round(cookies * 0.1875)):
    bowl.add(Flour.take(grams = 100))
    bowl.mix()

#Adding the chocolate chips, 100 grams per 8 cookies (rounding)
for i in range(round(cookies / 8)):
    bowl.add(ChocolateChips.take(grams = 100))
    bowl.mix()

# Finally, adding some baking powder (one teaspoon per 16 cookies, rounding) and mixing for the last time
bowl.add(BakingPowder.take(str(round(cookies / 16)) + ' teaspoon(s)'))

# Cookies are better when the dough rested in the fridge for a bit
# we can preheat the oven in the meanwhile

fridge.add(bowl)
oven.preheat(degrees = 175)

# Waiting for 10 minutes...

# Taking the bowl from the fridge and scooping the dough onto the baking tray in as many portions as you have decided
bowl = fridge.take()
for i in range (cookies):
    baking_tray.add(bowl.take('1/' + str(cookies)))

# Baking the cookies for ten minutes and taking them out
oven.add(baking_tray)
oven.bake(minutes = 10)
baking_tray = oven.take()

# Waiting for the cookies to cool down and serving on a plate
plate = baking_tray.take()
Rosemary.serve(plate)
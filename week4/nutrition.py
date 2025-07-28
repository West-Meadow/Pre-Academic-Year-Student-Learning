# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text.
#  Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
#   Ignore any input that isn’t a fruit.

items = {"apple": 130,
         "avocado":50,
         "cantaloupe":50,
         "grapes":90,
         "kiwifruit":90,
         "lime":20,
         "plums":70,
         "pear":100,
         "orange":80,
         "banana": 110,
         "grapefruit":60,
         "honeydew Melon":50,
         "lemon":15,
         "nectarine":60,
         "peach":60,
         "pineapple":50,
         "strawberries":50,
         "sweet cherries":100,
         "tangerine": 50,
         "watermelon": 80}


fruit = input("Item: ").lower()

for item in items:
        if fruit == item:
                print(items.get(fruit))
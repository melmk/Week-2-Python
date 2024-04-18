# nesting of data structures is acceptable in python
# this is a list that houses dictionaries
people = [
    {"name":"harry", "house": "gryffindor"},
    {"name":"cho", "house": "ravenclaw"},
    {"name":"draco", "house": "slytherin"},
]

# This function tells the sort method what to sort by (i.e by names)
def sortNames(people):
    return people["name"]

people.sort(key=sortNames)

print(people)

# However, there's another way to do this using lambda/anonymous functions
# Instead of creating a whole function just to return the key, we can define it inline

people.sort(key=lambda person: people["name"])
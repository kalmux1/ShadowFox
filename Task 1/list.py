                                # LIST TASK IN Beginner Level
#---------------------------------------------------------------------------------------------------------------------#


# 1. You have a list of superheroes representing the Justice League. 

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

#   Perform the following tasks:

# 1. Calculate the number of members in the Justice League.
    
print(justice_league)
length = len(justice_league)
print (f"The Total numbers of members in Justice League are {length}")

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.

justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print(justice_league)

# 4. Aquaman and Flash are having conflicts, and you need to separate them. 
#    Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.

popelement = justice_league.pop(1)
justice_league.insert(3,popelement)
print(justice_league)

# 5. The Justice League faced a crisis, and Superman decided to assemble a new team. 
#   Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".

justice_league.clear()
justice_league = justice_league + ["Superman","Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.

justice_league.sort()
print(justice_league)

# BONUS: Can you predict who the new leader will be?

print(f"The Leader of Justice League is {justice_league[0]}")
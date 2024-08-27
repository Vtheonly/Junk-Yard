# from rename import list_dirs_in_directory as ListD , list_files_in_directory as ListF
# from os import mkdir ,rename
# from shutil import move
# from greenShell import print_in_green as printG , printnlist as Plist
# import os
# import shutil
# directory =r"C:\Users\merse\OneDrive\Documents\Learn\Notes\GitHub\Level 1\\"


# # print(
    
# # ListF(directory)
# # )

# old = [

# '4 - what is a repositry.md',
# '5 - readme.md.md',
# '5 - what does the .gitignore do.md',
# '6 - coomtits.md',
# '7 - clone vs pull.md',
# '8 - github life cycle.md',
# '9 - github SSH.md',
# 'staged changes.md',
# 'status.md']


# new  = [

#     "4 - What is a Repository.md",
#     "5 - README.md",
#     "5 - What Does the .gitignore Do.md",
#     "6 - Commits.md",
#     "7 - Clone vs Pull.md",
#     "8 - GitHub Lifecycle.md",
#     "9 - GitHub SSH.md",
#     "12 - Staged Changes.md",
#     "13 - Status.md"
# ]




# from rename import rename_files


# rename_files(old,new)


x= [
	"You're far from god"
    "No one cares about you. You have no life.",
    "You don't know anything.",
    "You can't buy anything.",
    "You'll always be second to everyone.",
    "You always work under someone.",
    "You're always a disappointment to your father.",
    "You talk too much.",
    "You don't think in a way that matters. It's pointless.",
    "No one will remember you in a good light.",
    "You don't matter.",
    "You hurt the ones around you.",
    "Everyone is right about you.",
    "You will always be the lesser self.",
    "You're homeless and belong nowhere.",
    "Your dreams will never be a reality.",
    "You're going to waste your life.",
    "You keep repeating the cycle.",
    "You have no friends.",
    "No one wants you or care about you.",
    "You're a joke and a victim of you're own.",
    "Can't think for yourself and do something difficult.",
    "You're always in your comfort zone.",
    "You're not better than anyone.",
    "You're weak, useless, and less than average.",
    "You're insane, pathetic, and unattractive.",
    "You're alone because of people's choice, rejected, and an outcast.",
    "You don't love, respect, or care for yourself.",
    "You're so tasteless and unattractive.",
    "You're a waste of money, hope, time, breath, a construct of heat and space.",
    "You're imperfect in many ways.",
    "You depend on others, a parasite.",
    "You're a coward, lazy, ignored, and insignificant.",
    "You're poor in every way that matters."
  ]



x.sort()
x.reverse()

from greenShell import printnlist
printnlist(x)
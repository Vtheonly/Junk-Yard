from rename import list_files_in_directory as ListF
from rename import list_dirs_in_directory as ListD
from rename import rename_folders
from rename import rename_files

directory =r"/home/mersel/Documents/Projects/Junk Yard/Intro"
# print(ListD(directory))


old = (ListD(directory))




# old = ['Level 0 Baseics', 'Level 1 Library', 'Level 2 OOP', 'Level 4 JavaFX', 'Level 3 Maven Gradle']

new = ['Laravel', 'React ', 'Python', 'Django', 'Android Developemt', 'Electron', 'Flask', 'Machine Learning Models', 'Node.js', 'Firebase', 'Docker', 'PHP', 'Linux Scripting', 'JavaScript', 'JavaFX', 'SQL', 'C++', 'Express.js', 'java']


# print((old))



rename_folders(old,new)
# rename_files(old,new)

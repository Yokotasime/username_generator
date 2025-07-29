import random           # Imports the random module for random selection
import functools        # Imports functools to use reduce()

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']           # Prefix options
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']              # Suffix options

def capitalize_suffix(suffix): return suffix.capitalize()             # Capitalizes each suffix

capitalize_suffixes = list(map(capitalize_suffix, suffixes))          # Applies capitalization to all suffixes

def create_fantasy_name(list_1, list_2):                               # Combines a prefix + suffix into a fantasy name
    return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = list(map(lambda x: create_fantasy_name(prefixes, capitalize_suffixes), range(5)))  # Generates 5 random names

def fire_in_name(name): return True if 'Fire' in name else False      # Checks if the name contains 'Fire'

def concatenate_names(name1, name2): return name1 + ' ' + name2       # Combines two names into one string

filtered_names = list(filter(fire_in_name, random_names))             # Filters names that contain 'Fire'
reduced_name = functools.reduce(concatenate_names, filtered_names)    # Reduces filtered names into a single string

def display_name_info():                                              # Displays output info about fantasy names
    for name in random_names:                                         
        print("\n" + "-" * 50 + "\n")                                  # Adds divider for readability
        print(f"Fantasy Name: {name}")                                 # Prints the name
        print(f"Contains 'Fire': {fire_in_name(name)}")               # Checks and shows if 'Fire' is in the name
        print(f"Concatenated Name: {reduced_name}")                   # Shows reduced name string

display_name_info()                                                   # Calls the display function

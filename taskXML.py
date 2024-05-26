import xml.etree.ElementTree as ET

# Read in the movie.xml file
tree = ET.parse('movie.xml')
root = tree.getroot()

# Use the iter() function to list all the child tags of the movie element
print("Child tags of the movie elements:")
for movie in root.iter('movie'):
    for child in movie:
        print(child.tag)

# Use the itertext() function to print out the movie descriptions
print("\nMovie descriptions:")
for movie in root.iter('movie'):
    for element in movie.iter('description'):
        print("".join(element.itertext()))

# Find the number of movies that are favorites and the number of movies that are not
favorite_count = 0
non_favorite_count = 0

for movie in root.iter('movie'):
    if movie.get('favorite') == 'True':
        favorite_count += 1
    else:
        non_favorite_count += 1

print(f"\nNumber of favorite movies: {favorite_count}")
print(f"Number of non-favorite movies: {non_favorite_count}")

# array_lists.py

class Album:
    def __init__(self, albumName, numberOfSongs, albumArtist):
        self.albumName = albumName
        self.numberOfSongs = numberOfSongs
        self.albumArtist = albumArtist

    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"

# Create a new list called albums1 and add 5 albums to it
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("The Bodyguard", 12, "Whitney Houston"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Hotel California", 9, "Eagles")
]

# Print out albums1
print("Albums1 List:")
for album in albums1:
    print(album)

# Sort the list according to the numberOfSongs and print it out
albums1.sort(key=lambda album: album.numberOfSongs)
print("\nAlbums1 List Sorted by Number of Songs:")
for album in albums1:
    print(album)

# Swap the element at position 1 with the element at position 2 and print it out
albums1[1], albums1[2] = albums1[2], albums1[1]
print("\nAlbums1 List After Swapping Position 1 and 2:")
for album in albums1:
    print(album)

# Create a new list called albums2
albums2 = [
    Album("21", 11, "Adele"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("Born to Run", 8, "Bruce Springsteen"),
    Album("Nevermind", 12, "Nirvana"),
    Album("Purple Rain", 9, "Prince")
]

# Print out albums2
print("\nAlbums2 List:")
for album in albums2:
    print(album)

# Copy all of the albums from albums1 into albums2
albums2.extend(albums1)

# Add the additional albums to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# Print out albums2
print("\nAlbums2 List After Adding Albums from Albums1 and Additional Albums:")
for album in albums2:
    print(album)

# Sort the courses in albums2 alphabetically according to the album name and print it out
albums2.sort(key=lambda album: album.albumName)
print("\nAlbums2 List Sorted Alphabetically by Album Name:")
for album in albums2:
    print(album)

# Search for the album “Dark Side of the Moon” in albums2 and print out the index of the album in the list
album_name_to_search = "Dark Side of the Moon"
index = next((i for i, album in enumerate(albums2) if album.albumName == album_name_to_search), None)

print(f"\nIndex of '{album_name_to_search}' in albums2: {index}")

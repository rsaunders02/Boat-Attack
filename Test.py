coordinates = []
valid_rows = ['a','b','c','d','e','f','g','h','i', 'j']

coordinate = raw_input("Enter a coordinate(ex. A8): ")
letter = coordinate[0].lower()
number = int(coordinate[1:])
if letter in valid_rows:
    coordinates.append(letter)
if number > 0 and number < 11:
    coordinates.append(number)
print coordinates

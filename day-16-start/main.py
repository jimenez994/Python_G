# from turtle import Turtle, Screen
# from prettytable import PrettyTable


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("black", "orange")
# timmy.left(90)
# timmy.forward(300)
# timmy.right(165)
# timmy.forward(300)
# timmy.left(65)
# timmy.forward(300)
# timmy.right(150)
# timmy.forward(300)
# timmy.left(65)
# timmy.forward(300)
# timmy.right(150)
# timmy.forward(300)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# table = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
# print(table)

from prettytable import PrettyTable

# Create a PrettyTable instance
pokedex_table = PrettyTable()
pokedex_table.border = True


# Define table headers
pokedex_table.field_names = ["ID", "Name", "Type", "Description"]

# Add Pokémon data
pokedex_data = [
    (1, "Bulbasaur", "Grass/Poison", "The plant sprouts and grows with this Pokémon."),
    (4, "Charmander", "Fire", "When it rains, steam is said to spout from the tip of its tail."),
    (7, "Squirtle", "Water", "Powerfully sprays foam from its mouth."),
    # Add more Pokémon data as needed
]

# Add rows of data to the table
for pokemon in pokedex_data:
    pokedex_table.add_row(pokemon)

# Set column alignment
pokedex_table.align["Name"] = "l"
pokedex_table.align["Type"] = "c"
pokedex_table.align["Description"] = "r"

# Print the Pokédex table
print(pokedex_table)

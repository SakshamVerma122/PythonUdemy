# module --> each file that we create is a module in itself....
# package differs from a module -> Lots of code written by other people to achieve a goal

# pypi.org -> archive

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

# align is an object attrubute
table.align = "l"


print(table)
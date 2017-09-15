# set initial variable list of lists of string
# loop range 4 over sublists
#

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
colwidths = []

columns = []


for i in tableData:
    column = []
    strlen = 0
    for n in range(4):
        column.append(i[n])
        if strlen < len(i[n]):
            strlen = len(i[n])
    columns.append(column)
    colwidths.append(strlen)


print(columns)
print(colwidths)

# for i in range(4):
#     strlen = 0
#     for l in tableData:
#         if strlen < len(l[i]):
#             strlen = len(l[i])
#     colwidths.append(strlen)
#
# print(colwidths)

# TODO: fix this shit
# we have the longest string in the list, not the column

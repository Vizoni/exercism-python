def format_matrix(stringMatrix):
    rowsNotSpliited = matrix.split(' \n ')
    rows = []
    for row in rowsNotSpliited:
        rows.append(row.split())
    return rows

def print_row(rows):
    # formated_matrix_row = []
    # for x in range(len(rows[0])):
    #     for y in range(len(rows[0])):
    #         # print(rows[x][y])
    #         formated_matrix_row.append(rows[x][y])
    # print(rows)
    return rows

def print_column(rows):
    columns = []
    for x in range(len(rows[0])):
        for y in range(len(rows[0])):
            #falta arrumar aqui
            columns.append(rows[y][x])
    return columns

matrix = '9 8 7 \n 5 3 2 \n 6 6 7'
matrix_formated = format_matrix(matrix)
print(print_row(matrix_formated))
print(print_column(matrix_formated))
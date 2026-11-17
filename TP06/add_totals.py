def add_totals(table):
    for row in table:
        row.append(sum(row))

    col_totals = []
    for col in range(len(table[0])):
        total = sum(row[col] for row in table)
        col_totals.append(total)

    table.append(col_totals)
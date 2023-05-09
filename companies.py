eleks_company = ['Toni', 'Anna', 'Bob', 'Den']
toshiba_company = ['Marry', 'Tod', 'Den', 'Anna']
toshiba_company.extend(eleks_company)
eleks_company.clear()
print(*toshiba_company, sep=', ')


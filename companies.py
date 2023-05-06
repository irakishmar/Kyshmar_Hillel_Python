eleks_company = ['Toni', 'Anna', 'Bob', 'Den']
toshiba_company = ['Marry', 'Tod', 'Den', 'Anna']
toshiba_company.extend(eleks_company)
print(*toshiba_company, sep=', ')

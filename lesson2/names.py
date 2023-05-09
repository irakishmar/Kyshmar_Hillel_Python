duplicate_names = ['John Dow', 'John Dow', 'Marta Dow']
non_duplicate_names = dict.fromkeys(duplicate_names)
non_duplicate_names = list(non_duplicate_names)
print(*non_duplicate_names, sep=', ')

casino_blacklist = {'John Dow', 'Johnny Depp', 'Will Smith', 'Anthony Hopkins'}
poker_blacklist = {'Johnny Depp', 'Will Smith', 'John Dow', 'Forest Whitaker'}
alcohol_blacklist = {'Tom Hanks', 'John Dow', 'Johnny Depp', 'Anthony Hopkins'}

blacklist_persons = casino_blacklist.intersection(alcohol_blacklist, poker_blacklist)
print(*blacklist_persons, sep=', ')

# another option for choosing a blacklist person

print(*(casino_blacklist & poker_blacklist & alcohol_blacklist), sep=', ')



def directions(symbols_string: str) -> int:
    counts_of_symbols = {'^': 0, '>': 0, 'v': 0, '<': 0}
    for symbol in symbols_string:
        counts_of_symbols[symbol] += 1
    count_of_roated_element = len(symbols_string) - max(counts_of_symbols.values())

    return (count_of_roated_element)

if __name__ == "__main__":
    string_dir = '<<<>>>'
    print(directions(string_dir))


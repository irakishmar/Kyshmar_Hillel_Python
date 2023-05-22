def vowels(text):
    for letter in text:
        if letter in 'aeiouAEIOU':
            text = text.replace(letter, '')
    return text


if __name__ == "__main__":
    sting_text = 'Hello! Today is 24th of May, 2023. The current time is 10:30 AM. This is an example text with a mix of letters, numbers (123), and symbols (!@#).'
    print(vowels(sting_text))

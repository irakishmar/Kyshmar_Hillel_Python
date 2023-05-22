def is_prime(number: int) -> bool or str:
    if number < 2 or number > 1000:
        return "The number is incorrect. Please enter numbers from 2 to 1000"
    else:
        result = True
        for item in range(2, 1001):
            if number % item == 0 and number != item:
                result = False
                break
        return result


if __name__ == "__main__":
    print(is_prime(3))

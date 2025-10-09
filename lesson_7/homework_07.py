def multiplication_table(number: int):
    multiplier = 1

    while True:  # Keep original condition
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

def sum_of_2_numbers(x, y):
    return x + y

def average_number(numbers: list[float], counter=0) -> None:
    for x in numbers:
        counter += x

    return counter/(len(numbers))

def reverted_word(word: str) -> str:
    return word[::-1]

#Кастомний спосіб, все сам та руцями
def find_longest_word(words: list) -> str:
    counter = ""
    for x in words:
        if len(counter) < len(x):
            counter = x
        else:
            continue

    return counter
#Скучний та правильний:
"""
def find_longest_word_shorter(words: list) -> str:
    :return max(words, key=len)
"""

def find_substring(str1, str2) -> int:
   return str1.find(str2)

def main():
    multiplication_table(4)
    print(f"The sum of your numbers is: {sum_of_2_numbers(2, 3)}\n")
    print(f"Your average value is: {average_number([1, 2, 3, 4, 4])}")
    print(f"Your reversed word: {reverted_word('-1qwe-1qewqwlkelq;ke;````')}")
    print(f"The longest word is: {find_longest_word(["qwe", "12321", "12", '`', "0", 'q', 'queue', 'SongOfSiren', '11111111111'])}")
    print(f"Substring index is: {find_substring("Hello, world!", "world")}")
    print(f"Substring result is {find_substring("The quick brown fox jumps over the lazy dog", "cat")}")

if __name__ == "__main__":
    main()
def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: This describes the input the function is going to receive. the number is the integer and the function needs to determine if its even or odd.
    :return: This describes the function's answer that it gives back. It can either give back a True or False, and that depends on the integer given.
    """
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(3))


def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: The string of text looks for vowels
    :return: This just returns the total number of vowels that were found in the text.
    """
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count = count + 1

    return count

print(count_vowels("hello"))
print(count_vowels("Apple"))


def celsius_to_fahrenheit(celsius: float)-> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: The temperature is shown in degrees Celsius.
    :return: The temperature gets converted into degrees Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))


def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: This is the string that needs to be reversed
    :return: This results in the string having its characters in reverse order.
    """
    return text[::-1]
print(reverse_text("hello"))
print(reverse_text("machine"))


def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: This is the first integer being compared
    :param b: Second integer being compared.
    :return: Compares the numbers and returns the larger of the two intergers.
    """
    if a > b:
        return a
    else:
        return b
print(larger_number(8,3))
print(larger_number(5,10))


def average_two(a:int,b:int) -> float:
    """Calculate and return the average of two integers.

    :param a: the first integer.
    :param b: the second integer.
    :return: the average of both integers.
    """
    return (a + b) / 2

print(average_two(4,8))
print(average_two(6,10))



def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: The amount of money that is available
    :param cost: Price of the item
    :return: Result is either true if the balance you have covers the cost, otherwise it's False.
    """
    if balance >= cost:
        return True
    else:
        return False

print(can_afford(20,15))
print(can_afford(11,25))
print(can_afford(14,14))


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: The text that needs to be repeated.
    :param times: The amount of times you need to repeat the text.
    :return: The repeated text
    """
    result = ""
    for i in range(times):
        result = result + text
    return result
print(repeat_text("Hi", 3))
print(repeat_text("goodbye", 2))


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: The sentence we are searching.
    :param word: The word we are looking for in the sentence.
    :return: True if the word is located, otherwise its False.
    """
    return word in sentence
print(contains_word("I like basketball", "basketball"))
print(contains_word("I like basketball", "Football"))


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The original cost of the meal.
    :param percent: the percentage of the tip given.
    :return: the tip total.
    """
    return cost * percent / 100
print(calculate_tip(20.0, 15))
print(calculate_tip(50.0, 20))


def make_initials(first_name: str, last_name: str)-> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: The person's first name.
    :param last_name: The person's last name.
    :return: The uppercase initials
    """
    return first_name[0].upper() + last_name[0].upper()
print(make_initials("Agambir", "Singh"))
print(make_initials("Lebron", "James"))


def percent_score(points: float, possible: float) -> float|None:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: The points earned.
    :param possible: The total possible points.
    :return: The percentage earned, or it can be None if possible is less than 1.

    """
    if possible < 1:
        return None
    return (points/possible) * 100
print(percent_score(18,20))
print(percent_score(15, 20))
print(percent_score(5,0))


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: The number being checked.
    :param minimum: the lowest allowed value.
    :param maximum: The maximum allowed value.
    :return: True if the number stays within the range, otherwise it would be False.
    """
    return minimum <= number <= maximum
print(is_between(5,1,10))
print(is_between(1,1,10))
print(is_between(12,1,10))


def all_different(a: str, b: str, c: str)-> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: The first string.
    :param b: Second string.
    :param c: Third string.
    :return: True if all three string are different, otherwise it's False.
    """
    return a != b and a != c and b !=c
print(all_different("red", "blue", "orange"))
print(all_different("red", "blue", "red"))


def average_three(a: float, b: float, c: float) -> float:
    """Calculate and return the average of three integers.

    :param a: The first number.
    :param b: Second number.
    :param c: Third number.
    :return: The average of the three numbers combined.
    """
    return (a + b + c) / 3
print(average_three(3, 6, 9))
print(average_three(2, 4, 5))


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float)-> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: The current temperature.
    :param cold_limit: The temperature below which it is cold.
    :param hot_limit: The temperature above which it is hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"
print(describe_temperature(5, 10, 25))
print(describe_temperature(30, 10, 25))
print(describe_temperature(20, 10, 25))


if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    pass


def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f : float) -> bool:
    """ Checks whether a Celsius temperature is within a safe Fahrenheit range.
    :param celsius: The temperature in Celsius.
    :param minimum_f: The minimum safe temperature in Fahrenheit.
    :param maximum_f: The maximum safe temperature you can reach in Fahrenheit.
    :return: True if the converted temperature is within the range, otherwise it would be false.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return minimum_f <= fahrenheit <= maximum_f
print(temperature_in_safe_range(20, 50, 80))
print(temperature_in_safe_range(0, 50, 80))
print(temperature_in_safe_range(30, 50, 90))


def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """ Check whether the balance will cover the cost and tip price.
    :param balance: The amount of money we have access too.
    :param cost: The original cost.
    :param tip_percent: the tip percentage.
    :return: True if the balance covers the total, if not the result is False.
    """
    tip = cost * tip_percent / 100
    total = cost + tip
    return balance >= total
print(can_afford_with_tip(25, 20, 15))
print(can_afford_with_tip(20, 20, 15))
print(can_afford_with_tip(50, 40, 20))


def meets_average(score1: float, score2: float,score3: float, required_average : float) -> bool:
    """ Check if the average of the three scores meets the requirements.
    :param score1: the first score.
    :param score2: Second score.
    :param score3: Third score.
    :param required_average: The minimum average required.
    :return: True if the average meets the minimum requirement, otherwise it's false.
    """

    average = (score1 + score2 + score3) / 3
    return average >= required_average
print(meets_average(80, 90, 100, 85))
print(meets_average(60, 70, 80, 75))
print(meets_average(70, 70, 70, 70))


def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """ Check if the names initia matches with the expected initial
    :param first_name: The person's first name.
    :param last_name:  THe person's last name.
    :param expected_initials: The initials we are comparing it against.
    :return: True if the initials match, capitalization does not matter.
    """
    initials = first_name[0].upper() + last_name[0].upper()
    return initials == expected_initials.upper()
print(initials_match("Agambir", "Singh", "AS"))
print(initials_match("lebron", "james", "LJ"))
print(initials_match("Luka", "Doncic", "LD"))


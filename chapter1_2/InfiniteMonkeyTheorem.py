def score(generated: str, goal: str) -> float:
    """Compare the generated string with the goal.

    Args:
        generated (str): [description]
        goal (str): [description]

    Returns:
        float: A value from 0 to 1; the rate of characters in generated string that
            match the goal string. E.g. A score of 0 means no character matches in the
            generated string matches the goal.
    """


def generate(length: int) -> str:
    """Generates a string by choosing random characters from [a-z ]

    Args:
        length (int): The length of the string to be generated.

    Returns:
        str: {length}-long string.
    """


def monkey_tries_to_type(goal: str) -> int:
    """This monkey (function) attempts to type the {goal} by hitting random keys.

    Repeatedly calls `generate()` and `score()` until {goal} is achieved.

    "The theorem states that a monkey hitting keys at random on a typewriter keyboard
    for an infinite amount of time will almost surely type a given text, such as the
    complete works of William Shakespeare. Well, suppose we replace a monkey with a
    Python function. How long do you think it would take for a Python function to
    generate just one sentence of Shakespeare?"

    "If 100% of the letters are correct we are done. If the letters are not correct
    then we will generate a whole new string. [This function] should print out the
    best string generated so far and its score every 1000 tries."

    Args:
        goal (str): The string that the "monkey" attempts to type.

    Returns:
        int: The number of attempts until the monkey finally types the {goal}
    """

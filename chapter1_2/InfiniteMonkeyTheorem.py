import random

GOAL = "methinks it is like a weasel"
GOAL_LENGTH = len(GOAL)
CHARACTER_SET = "abcdefghijklmnopqrstuvwxyz "


def score(generated: str) -> float:
    """Compare the generated string with the goal.

    Args:
        generated (str): The generated string

    Returns:
        float: A value from 0 to 100; Percentage of characters in generated string that
            match the goal string. E.g. A score of 0 means no character matches in the
            generated string matches the goal.
    """
    errors = sum(generated[index] != goal_char for index, goal_char in enumerate(GOAL))
    return (GOAL_LENGTH - errors) / GOAL_LENGTH * 100


def generate() -> str:
    """Generates a string by choosing random characters from [a-z ]

    Returns:
        str: {length}-long string.
    """
    list_of_char = [random.choice(CHARACTER_SET) for _ in range(GOAL_LENGTH)]
    return "".join(list_of_char)


def report_progress(
    print_progress: bool, attempts: int, best_generated_string: str, best_score: float
):
    if attempts % 1000 == 0 and print_progress:
        print(f"Attempt {attempts}: {best_generated_string} {best_score:.2f}")


def monkey_tries_to_type(print_progress: bool = False) -> int:
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
        print_progress (bool): If True, for every 1000 tries, print out the best string
            generated so far and its score.

    Returns:
        int: The number of attempts until the monkey finally types the {goal}
    """
    attempts, best_score = 0, 0
    best_generated_string = ""
    while best_score != 100:
        generated = generate()
        current_score = score(generated=generated)
        if current_score >= best_score:
            best_score = current_score
            best_generated_string = generated
        attempts += 1
        report_progress(print_progress, attempts, best_generated_string, best_score)

    return attempts


if __name__ == "__main__":
    monkey_tries_to_type(print_progress=True)

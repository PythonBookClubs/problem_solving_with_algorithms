import random
from time import time
from timeit import timeit
from typing import List

from chapter1_2.InfiniteMonkeyTheorem import CHARACTER_SET, GOAL, GOAL_LENGTH
from chapter1_2.InfiniteMonkeyTheorem import generate as generate_fresh
from chapter1_2.InfiniteMonkeyTheorem import score

# One way to make chapter1_2 imports to work is to modify PYTHONPATH:
# bash$ export PYTHONPATH=$PYTHONPATH:/path/to/problem_solving_with_algorithms
# bash$ python /path/to/problem_solving_with_algorithms/Infinite...HillClimbing.py


def generate(print_progress: bool, generated_str: str, attempts: int) -> int:
    """Generates GOAL by modifying one key at a time from the {generated} string.

    Args:
        generated (str): The best generated string.
        attempts (int): The number of attempts until the program created
            the {generated} string.

    Returns:
        int: Number of attempts until the {GOAL} text has been generated.
    """

    generated = list(generated_str)
    for index in range(GOAL_LENGTH):
        while generated[index] != GOAL[index]:
            generated[index] = random.choice(CHARACTER_SET)
            attempts += 1
        report_progress(print_progress, attempts, generated)

    return attempts


def report_progress(print_progress: bool, attempts: int, generated: List[str]):
    if print_progress:
        print(f"Attempt {attempts}: {''.join(generated)}")


def monkey_tries_to_type(print_progress: bool = False) -> int:
    """This monkey (function) attempts to type the {goal} by hitting random keys.

    "...improve upon the program ... by keeping letters that are correct and **only
    modifying one character** in the best string so far. This is a type of algorithm in
    the class of ‘hill climbing’ algorithms, that is we only keep the result if it is
    better than the previous one."

    Args:
        print_progress (bool): If True, print out the string generated whenever the
            program chooses the correct key.

    Returns:
        int: The number of attempts until the monkey finally types the {GOAL}
    """
    attempts, current_score = 0, 0
    generated = ""

    # Completely create new string with random keys
    # until there's least one correct character (best generated string).
    while current_score == 0:
        generated = generate_fresh()
        current_score = score(generated=generated)
        attempts += 1
        report_progress(print_progress, attempts, list(generated))

    return generate(print_progress, generated, attempts)


if __name__ == "__main__":
    print("Run the program...")
    monkey_tries_to_type(print_progress=True)

    print("\nHow does it scale?")
    for num in [1, 10, 100, 1000]:
        print(
            f"Executing {num}x:",
            timeit(
                "monkey_tries_to_type()",
                "from __main__ import monkey_tries_to_type",
                number=num,
            ),
        )

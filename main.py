def main():
    import random
    import string
    import sys

    global score
    global lives
    score = 0
    lives = 3

    # def receive_answer(question_type):
    #     while True:
    #         user_answer = input(">>> ").lower()
    #         try:
    #             if (
    #                 question_type == "multiple_choice"
    #                 and user_answer.isalpha()
    #                 and len(user_answer) == 1
    #             ):
    #                 break
    #             elif question_type == "arithmetic" and user_answer.isdigit():
    #                 user_answer = int(user_answer)
    #                 break
    #             elif question_type == "text" and user_answer.isalpha():
    #                 break
    #             else:
    #                 raise ValueError()
    #         except:
    #             print(
    #                 "That doesn't seem to be a valid answer format for this question. Try again:"
    #             )

    #     return user_answer

    def receive_answer(question_type):
        while True:
            user_answer = input(">>> ").lower()

            if (
                question_type == "multiple_choice"
                and user_answer.isalpha()
                and len(user_answer) == 1
            ):
                break
            elif question_type == "arithmetic" and user_answer.isdigit():
                user_answer = int(user_answer)
                break
            elif question_type == "text" and user_answer.isalpha():
                break
            else:
                print(
                    "That doesn't seem to be a valid answer format for this question. Try again:"
                )

        return user_answer

    def check_answer(given_answer, correct_answer):
        global score
        global lives
        if given_answer == correct_answer:
            print(r"Correct!")
            score += 1
            print(f"score: {score}   ~~~~~~   lives: {lives}", "\n")
        else:
            print("!!!WRONG!!!", "\n")
            print(f"correct answer was {correct_answer}...")
            lives -= 1
            print(f"score: {score}   ~~~~~~   lives: {lives}")
            if lives > 0:
                print("\nwatch out!\n")
            else:
                print(
                    r"""
                         _                               _ _                     _
                        | |_ __ ___   __ _  ___     __ _(_) |_    __ _ _   _  __| |
                        | | '_ ` _ \ / _` |/ _ \   / _` | | __|  / _` | | | |/ _` |
                        | | | | | | | (_| | (_) | | (_| | | |_  | (_| | |_| | (_| |
                        |_|_| |_| |_|\__,_|\___/   \__, |_|\__|  \__, |\__,_|\__,_|
                                                   |___/         |___/
                    """,
                    sep="",
                )
                sys.exit()

    print(r"""
        *  .  . *       *    .        .        .   *    ..
      .    *        .   ###     .      .        .            *
         *.   *        #####   .     *      *        *    .
       ____       *  ######### *    .  *      .        .  *   .
      /   /\  .     ###\#|#/###   ..    *    .      *  .  ..  *
     /___/  ^8/      ###\|/###  *    *            .      *   *
     |   ||%%(        # }|{  #
     |___|,  \\  ejm    }|{             the quizzzzzz
        """)

    # --multiple choice questions stage--

    # first in list is correct answer
    multiple_choice_qbank = {
        "Which planet is known as the 'Red Planet'?": ["Mars", "Venus", "Mercury"],
        "What is the capital of Japan?": ["Tokyo", "Osaka", "Kyoto", "Nagoya"],
        "Which element has the chemical symbol 'O'?": [
            "Oxygen",
            "Gold",
            "Osmium",
            "Hydrogen",
            "Neon",
        ],
        "Which of the following is the largest mammal on Earth?": [
            "Blue Whale",
            "African Elephant",
            "Hippopotamus",
            "Orca (Killer Whale)",
            "Giraffe",
            "Polar Bear",
            "Walrus",
        ],
    }

    for i in multiple_choice_qbank:
        print(i)
        # print(multiple_choice_qbank[i])

        options = random.sample(multiple_choice_qbank[i], len(multiple_choice_qbank[i]))

        correct_letter = string.ascii_lowercase[
            (options).index((multiple_choice_qbank[i])[0])
        ]

        for j in options:
            print(string.ascii_uppercase[options.index(j)], j)

        print("What is the correct answer? Input the letter for your pick below:")

        check_answer(receive_answer("multiple_choice"), correct_letter)

        # print(*options, sep="\n")
        # for j in options:
        #     print(j)

    # --arithmetic questions stage--

    left_number = random.randint(1, 10)
    right_number = random.randint(1, 10)

    # given_product = int(input(f"what's {left_number} x {right_number} ?\n"))
    # if given_product == (left_number * right_number):
    #     print("yea")

    print(f"What's {left_number} x {right_number} ?")

    check_answer(receive_answer("arithmetic"), (left_number * right_number))

    # --text answer stage--

    print("What is the capital of Great Britain?")

    check_answer(receive_answer("text"), "london")

    print(
        r"""
                                                                  _               _
                         _   _  ___  _   _   ___ _   _ _ ____   _(_)_   _____  __| |
                        | | | |/ _ \| | | | / __| | | | '__\ \ / / \ \ / / _ \/ _` |
                        | |_| | (_) | |_| | \__ \ |_| | |   \ V /| |\ V /  __/ (_| |
                         \__, |\___/ \__,_| |___/\__,_|_|    \_/ |_| \_/ \___|\__,_|
                         |___/
        """,
        sep="",
    )


if __name__ == "__main__":
    main()

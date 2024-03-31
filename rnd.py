from random import randint
from sys import argv, exit


def main():
    try:
        if len(argv) != 6:
            print(
                "Usage: python rnd.py <countFrom> <countTo> <numberOfElements> <numberFrom> <numberTo>")
            exit(1)

        countFrom = int(argv[1])
        countTo = int(argv[2])
        numberOfElements = int(argv[3])
        numberFrom = int(argv[4])
        numberTo = int(argv[5])

        print("\nCombinations: \n")
        for i in range(countFrom - 1, countTo):
            print(i + 1, end=":\t")
            for _ in range(numberOfElements):
                print(randint(numberFrom, numberTo), end="\t")
            print()
        print("\n")
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit(1)


if __name__ == "__main__":
    main()

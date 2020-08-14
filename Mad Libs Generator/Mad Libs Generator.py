import random


def main():
    print("\nMad Libs!!!")
    print("\nEnter an example of each of the following(Add quotes if you wish to distinguish the words you entered)")

    random_name = input('\nRandom name: ')
    your_name = input('Your name: ')
    place = input('Place: ')
    adjective = input('Adjective, ex. weird: ')

    adj = ["Crazy", "Nice", "Lovely", "Gross"]
    verbs = ["met", "proposed to", "robbed", "pushed"]
    prepositions = ["above the", "near the", "around the", "behind", "beside"]

    print((random.choice(adj)) + " " + random_name + " " + (random.choice(verbs)) + " " + your_name + " " + (random.choice(prepositions)) + " " + adjective + " " + place)


if __name__ == "__main__":
    main()
# Part 2

# Question Link : https://adventofcode.com/2023/day/2


# We just need to find out the maximum count per color and multiply it , and finally add the result

tot = 0

while True:

    try:

        passes = {
            'green': 0,
            'red': 0,
            'blue': 0
        }

        s = input()

        colon = s.find(":")

        games = s[colon + 1:].split(';')

        for contest in games:

            print("The contest is : ", contest)
            for single in contest.split(','):
                print("The single entry is", single)
                [value, color] = single.strip().split(' ')
                print("The value is", value, "The color is", color)
                if int(value) > passes[color]:
                    passes[color] = int(value)
                    print("The color is", color, "and its new value is", passes[color])

        print("The passes are", passes)
        tot += (passes['green'] * passes['blue'] * passes['red'])

        print("Total is", tot)
        print('Next contest \n')

    except e:
        break

print(tot)

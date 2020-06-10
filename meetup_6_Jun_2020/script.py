import sys

# get arguments from python command line
numbers = sys.argv[1:]

# summation
total = 0
for number in numbers:
    total += int(number)

if __name__ == "__main__":
    # print output
    print("program name is:", sys.argv[0])
    print("program arguments are:", numbers)
    print("total is:", total)
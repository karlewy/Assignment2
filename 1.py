def solve(s):
    return ' '.join(word.capitalize() if word else '' for word in s.split(' '))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

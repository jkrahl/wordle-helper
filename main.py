import argparse
import io

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', default='5')
    parser.add_argument('--green', default='*****')
    parser.add_argument('--yellow', default='')
    parser.add_argument('--gray', default='')

    args = parser.parse_args()

    length = int(args.length)
    green = args.green
    yellow = args.yellow
    gray = args.gray

    if len(green) != length or len(yellow) > length:
        print('Invalid arguments')
        return

    with io.open('palabras.txt', 'r', encoding='utf-8') as f:
        words = f.read().splitlines()

    # Filter the words
    words = [word for word in words if len(word) == length]
    words = [word for word in words if checkGreen(word, green, length)]
    words = [word for word in words if checkYellow(word, yellow, length)]
    words = [word for word in words if checkGray(word, gray, length)]

    # Print the words
    for word in words:
        print(word)


# green is like '**e**' or 'a***e' or '*****'
# checkGreen reurns true if the word has all green characters in the correct positions
def checkGreen(word, green, length):
    for i in range(length):
        if green[i] != '*' and green[i] != word[i]:
            return False
    return True

# yellow is like 'a' or 'ae' or 'aei' or 'aeiou'
# checkYellow returs true if the word has all yellow letters
def checkYellow(word, yellow, length):
    for char in yellow:
        if char not in word:
            return False
    return True

# gray is like 'a' or 'ae' or 'aei' or 'aeiou'
# checkGray returns true if the word has none of the gray letters
def checkGray(word, gray, length):
    for char in gray:
        if char in word:
            return False
    return True

if __name__ == '__main__':
    main()

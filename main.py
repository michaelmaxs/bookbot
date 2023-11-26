def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    count = count_words(file_contents)
    print (f"{count} words in file")
    letters = count_letters(file_contents)
    print (f"{letters}")

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_contents):
    words = file_contents.split()
    number_of_words = 0
    for word in words:
        number_of_words = number_of_words + 1
    return number_of_words   

def count_letters(file_contents):
    lettercount = {}
    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            if char in lettercount:
                lettercount[char] = lettercount[char] + 1
            else:
                lettercount[char] = 1
    return lettercount

#def report_printing(file_contents):
#    report_body = []


main()

def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    count = count_words(file_contents)
    letters = count_letters(file_contents)
    sorted_letters = letter_sorting(letters)
    print ("")
    print (f"--- Begin report of {path} ---")
    print (f"{count} words found in the document")
    print ("")
    for char, count in sorted_letters:
        print(f"The '{char}' character was found {count} times")
    print ("--- End report ---")
    print ("")
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

def letter_sorting(letters):
    letters_list = list(letters.items())
    letters_list.sort(key=lambda x: x[1], reverse=True)
    return letters_list

main()

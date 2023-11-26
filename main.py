def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    count = count_words(file_contents)
    print (f"{count} words in file")

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_contents):
    words = file_contents.split()
    number_of_words = 0
    for word in words:
        number_of_words = number_of_words + 1
    return number_of_words   

#def count_letter(file_contents):
#this is a test

main()

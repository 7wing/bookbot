import sys
from stats import count_words, count_characters, generate_report


def main():
        if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)

        frakenstein_filepath = sys.argv[1]
        file_text = get_book_text(frakenstein_filepath)
        counted_words = count_words(file_text)
        counted_characters = count_characters(file_text)
        sorted_characters = sorted(counted_characters.items(), key=sort_on, reverse=True)
        report = generate_report(counted_words, dict(sorted_characters))
        # print(file_text)
        # print(f"{counted_words} words found in the document")
        # print(counted_characters)
        print(report)


def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
                return file_contents

def sort_on(item):
        return item[1]

main()
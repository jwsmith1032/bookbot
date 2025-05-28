from stats import counter
from stats import c_counter
from stats import sort

import sys

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents

def main():
	if(len(sys.argv) != 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		
	text = get_book_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print("Found " + str(counter(text)) + " total words")
	print("--------- Character Count -------")
	for c in (sort(c_counter(text))):
		if(c["char"].isalpha()):
			print(c["char"] + ": " + str(c["num"]))
	print("============= END ===============")

if __name__ == "__main__":
    main()	

from text import Text_Class
from pprint import pprint


def main():
	text_toolkit = Text_Class()
	print("Which text to use? A) Heart of Darkness, B) Moby Dick, C) Babbitt \nEnter the letter")
	choice = input()
	if choice == "A" or choice == "a":
		filename = "heart_of_darkness"
	elif choice == "B" or choice == "b":
		filename = "moby_dick"
	elif choice == "C" or choice == "c":
		filename = "babbitt"
	text_toolkit.readFile("./" + filename + ".txt")
	text_toolkit.clean()
	print("Enter a sequence of percentiles separated by commas:")
	input_list = input().split(",")
	percentiles_template = []
	for percentile in input_list:
		percentiles_template.append(int(percentile))
	print("\n\n\n")
	for i in range(20):
		text = ""
		for percentile in percentiles_template:
			text += text_toolkit.get_random_word_by_percentile(percentile) + " "
		print(text)

if __name__ == "__main__":
    main()
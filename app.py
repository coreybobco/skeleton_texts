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
	# text_toolkit.calculate_frequencies_and_counts()
	# print(text_toolkit.indexed_frequencies_and_counts)
	text_toolkit.index_words_by_frequency()
	prompt = "Enter a sequence of numbers between 1 and " + str(text_toolkit.frequency_count) + ". A higher number will randomly select a word that appears "
	prompt += "at a low level of frequency (based on how high the number is), and a lower number will select a word that appeared at a high level  of frequency. "
	prompt += "For the lowest numbers, this will not be random because only one word appeared at that frequency level. Generally, a higher number indicates a "
	prompt += "higher level of randomness and will select words that are more unique to the overall book."
	print(prompt)
	input_list = input().split(",")
	percentiles_template = []
	for percentile in input_list:
		percentiles_template.append(int(percentile))
	print("\n\n\n")
	for i in range(20):
		text = ""
		for frequency_input in percentiles_template:
			text += text_toolkit.get_random_word_by_frequency_input(frequency_input) + " "
		print(text)

if __name__ == "__main__":
    main()
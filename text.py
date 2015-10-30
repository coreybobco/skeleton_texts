import re
from random import shuffle
from collections import OrderedDict

class Text_Class:
    """
    divide into words, clauses, sentences, stanzas, lines of dialogue
    """

    def __init__(self):
        self.source = ""
        self.word_frequencies = {}
        self.flipped_word_frequencies = {}
        self.words_organized_by_frequency = []
        # self.readFile(filename)
        # self.clean_text = self.clean(self.source)
     
    def read(self, string):
        self.source += string

    def readFile(self, filename):
        handle = open(filename, "r")
        file_content = handle.read()
        self.source = file_content

    def clean(self):
        # handle punctuation that ends sentences
        # normalize repeating punctuation
        # abnormal punctuation - any number of .s past 3 is collapsed
        #                      - spaces between ellipses is removed
        #                      - ellipses character expanded to "..."
        #                      - fancy quotes into \" and \'
        #                      - collapse sentence delimiters in general
        #                           - go with the first one
        #                      - remove tab characters 
        #                      - remove newlines
        clean_text = self.source
        # normalize quotes
        clean_text = clean_text.replace("“","\"")
        clean_text = clean_text.replace("”","\"")
        clean_text = clean_text.replace("‘","\'")
        clean_text = clean_text.replace("’","\'")
        # normalize newlines
        clean_text = clean_text.replace("\n"," ")
        # normalize spaces
        while clean_text.find("  ") != -1:
            clean_text = re.sub("[\s\t]{2,}"," ", clean_text)
        # normalize ellipses
        short_ellipses = list(set(re.findall("[^.][.]{2}[^.]", clean_text)))
        corrected_ellipses = []
        for short_ellipsis in short_ellipses:
            corrected_ellipsis = short_ellipsis[0:1] + "." + short_ellipsis[2:3]
            corrected_ellipses.append(corrected_ellipsis.lstrip())
        for index, short_ellipsis in short_ellipses:
            clean_text = clean_text.replace(short_ellipsis, corrected_ellipses[index])
        clean_text = re.sub("\.[\.\ ]{1,}\.","...",clean_text)
        # normalize dashes
        clean_text = clean_text.replace(" - ", "--")
        clean_text = re.sub("[\s]?[-—]+[\s]?","--", clean_text)
        self.clean_text = clean_text

    def divide_into_words(self):
        # use the native python String.split method
        divided_text = self.clean_text.split(" ")
        result = []
        for dividend in divided_text:
            if("--" in dividend):
                for word in dividend.split("--"):
                    result.append(word)
            else:
                result.append(dividend)
        return result

    def divide_into_clauses():
        # use re.split using the clause and sentence delimiters
        return ""

    def divide_into_sentences(self):
        # use re.split using the sentence delimiters
        regex = "[.?!][\"')]?"
        return (re.split(regex, self.clean_text), re.findall(regex, self.clean_text))

    def divide_into_lines_of_dialogue():
        # use re.split using the speaker name regex
        speaker_name = "[A-Z][A-za-z.]+:"

    def organize_words_by_frequency(self):
        if (self.flipped_word_frequencies == {}):
            self.calculate_flipped_word_frequencies()
        words_organized_by_frequency = []
        for frequency, word_list in self.flipped_word_frequencies.items():
            shuffle(word_list)
            for i in range(len(word_list)):
                for j in range(frequency):
                    words_organized_by_frequency.append(word_list[i])
        self.words_organized_by_frequency = words_organized_by_frequency

    def calculate_word_frequencies(self):
        text_as_list = self.divide_into_words()
        word_frequencies = {}
        for word in text_as_list:
            if word in word_frequencies.keys():
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1
        self.word_frequencies = word_frequencies

    def calculate_flipped_word_frequencies(self):
        if (self.word_frequencies == {}):
            self.calculate_word_frequencies()
        flipped_word_frequencies = {}
        for word, frequency in self.word_frequencies.items():
            if frequency in flipped_word_frequencies.keys():
                flipped_word_frequencies[frequency].append(word)
            else:
                flipped_word_frequencies[frequency] = [word]
        self.flipped_word_frequencies = OrderedDict(sorted(flipped_word_frequencies.items(), reverse=True))

    def get_random_word_by_percentile(self, percentile):
        self.organize_words_by_frequency()
        index = round((percentile / 100) * len(self.words_organized_by_frequency))
        return self.words_organized_by_frequency[index]

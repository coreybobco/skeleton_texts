import re
import random
import operator
from collections import OrderedDict
from pprint import pprint

class Text_Class:
    """
    divide into words, clauses, sentences, stanzas, lines of dialogue
    """

    def __init__(self):
        self.source = ""
        self.indexed_frequencies_by_word = {}
        self.indexed_words_by_frequency = {}
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

    def index_frequencies_by_word(self):
        text_as_list = self.divide_into_words()
        indexed_frequencies_by_word = {}
        for word in text_as_list:
            if word in indexed_frequencies_by_word.keys():
                indexed_frequencies_by_word[word] += 1
            else:
                indexed_frequencies_by_word[word] = 1
        self.indexed_frequencies_by_word = indexed_frequencies_by_word

    def index_words_by_frequency(self):
        if (self.indexed_frequencies_by_word == {}):
            self.index_frequencies_by_word()
        indexed_words_by_frequency = {}
        for word, frequency in self.indexed_frequencies_by_word.items():
            if frequency in indexed_words_by_frequency.keys():
                indexed_words_by_frequency[frequency].append(word)
            else:
                indexed_words_by_frequency[frequency] = [word]
        self.indexed_words_by_frequency = indexed_words_by_frequency
        # Sort indexed words by frequency by length of list of words paired with each frequency
        self.index_unique_word_counts_by_frequency()
        indexed_words_by_frequency = OrderedDict()
        for frequency in self.indexed_unique_word_counts_by_frequency.keys():
            indexed_words_by_frequency[frequency] = self.indexed_words_by_frequency[frequency]
        self.indexed_words_by_frequency = indexed_words_by_frequency
        self.list_of_frequencies = list(indexed_words_by_frequency.keys())
        self.frequency_count =  len(self.list_of_frequencies)

    def index_unique_word_counts_by_frequency(self):
        if self.indexed_words_by_frequency == {}:
            self.index_words_by_frequency()
        indexed_unique_word_counts_by_frequency = {}
        for frequency, list_of_words in self.indexed_words_by_frequency.items():
            indexed_unique_word_counts_by_frequency[frequency] = len(list_of_words)
        sorted_tuples = sorted(indexed_unique_word_counts_by_frequency.items(), key=operator.itemgetter(1), reverse=False)
        indexed_unique_word_counts_by_frequency = OrderedDict()
        for (frequency, word_count) in sorted_tuples:
            indexed_unique_word_counts_by_frequency[frequency] = word_count
        self.indexed_unique_word_counts_by_frequency = indexed_unique_word_counts_by_frequency

    def get_random_word_by_frequency_input(self, frequency_input):
        return random.choice(self.indexed_words_by_frequency[self.list_of_frequencies[frequency_input]])

    def break_into_bones(self):
        frequency_scale_bones = list(re.findall("{[\S]*\([ABCDEF],[\s]?[\S]*\)}"), skeleton)
        portmanteau_bones = list(re.findall("{frequency_scale\([ABCDEF],[\s]?[\S]*\)}"))
        for ectoplasm in frequency_scale_bones:
            function_name = re.match("\{[\S]{3,}", ectoplasm)
            call = re.search("\([ABCDEF],[\s]?[\S]*\)", ectoplasm)
            call = frequency_scale_call[1:-1].replace(" ", "")
            call_args = call.split(",")






            
        

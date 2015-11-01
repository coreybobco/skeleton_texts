#!/usr/bin/env python2.7
import random

words = open("mangled-wake.txt").read().split("\n")
all_words = open("corncob_lowercase.txt").read().split("\r\n")

def words_beginning_with(substring):
    # given a substring, returns a list of dictionary words starting with that substring
    return filter(lambda s: s.startswith(substring) and len(s) > 3, words)

def random_word():
    word = ''
    while len(word) < 3:
        word = random.choice(words)
    return word

def naive_random_portmanteau(overlap=2):
    if overlap > 0:
        overlap = overlap * -1
    matches = []
    word = ''
    while len(matches) == 0:
        word = random_word()
        substring = word[overlap:]
        matches = words_beginning_with(substring)
        word_sans_overlap = word[0:overlap]
    return word_sans_overlap + random.choice(matches)

for i in range(1,1000):
    print(naive_random_portmanteau(3))

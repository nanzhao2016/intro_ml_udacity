#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
import string, re

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated)

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata

    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(str.maketrans('', '', string.punctuation))
        #tokenizer = RegexpTokenizer(r'\w+')
        #to_stemm = tokenizer.tokenize(text_string)

        ### project part 2: comment out the line below
        text_string = text_string.replace('\n', ' ').replace('  ', ' ').lower()
        tokenizer = RegexpTokenizer(r'\w+')
        to_stemm = tokenizer.tokenize(text_string)
        punctuation = re.compile(r'[-.?!,":;()|0-9]')
        to_stemm = [punctuation.sub("", word) for word in to_stemm]
        to_stemm = [w for w in to_stemm if w is not '']

        """
        tokenizer = RegexpTokenizer(r'\w+')
        to_stemm = tokenizer.tokenize(content[1])
        """
        ## string.punctuation is to remove \', while tokenize is to split the words with \'


        stemmer = SnowballStemmer('english')
        words = [stemmer.stem(plural) for plural in to_stemm]
        #words = ' '.join(w for w in words)
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)


    return (words)

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print (text)

if __name__ == '__main__':
    main()

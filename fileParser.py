import numpy
import operator
import sys


class FileParser:
    def __init__(self, file_name=None):
        # number of letters array and number of occurences per letter
        # hashmap are declared globally because we want the file to be
        # parsed only once and the results from each word and each line
        # are updated to these after each function call with every single 
        #  word and line
        self.nletters = []
        self.lettercount = {}
        self.filename = file_name
        # This is done to avoid breaking the code while running individual
        # functions from this class which do not need passing a file name
        if self.filename is None:
            print "FileParser object created without any input file."

    def parse_word(self, word):
        # process all the letters in lowercase in order to avoid dividing counts
        word = word.strip().lower()
        for i in range(0, len(word)):
            if word[i].isalpha():
        # if the alphabet is seen previously, update count, else create new key
                if word[i] in self.lettercount.keys():
                    self.lettercount[word[i]] += 1
                else:
                    self.lettercount[word[i]] = 1

    def parse_line(self, line):
        wordcount = 0
        # update wordcount for each word read, and append its letter count to 
        # the nletters array, then send the word for further processing to 
        # get number of occurences of the letters in the word
        for word in line.strip().split(' '):
            wordcount += 1
            self.nletters.append(len(word))
            self.parse_word(word)
        return wordcount

    def parse_file(self, file_name):
        #try to open the file, catch exeption and exit if the path is invalid
        try:
            my_file = open(file_name, "r")
        except IOError:
            print "invalid file path: the file does not exist in the specified path." \
                  "Give path relative to FileStats/ folder"
            sys.exit(1)
        linecount = 0
        wordcount = 0
        # reading each line, update line count and send the line for further 
        # processing to obtain the wordcounts of each line
        for line in my_file:
            if line.rstrip():
                linecount += 1
                wordcount += self.parse_line(line)
        return linecount, wordcount

    def process(self):
        # calling parse_file from here to avoid parsing the file multiple number 
        # of times to obtain all the statistics. This way, everything is computed
        # by parsing the file just once
        line_count, word_count = self.parse_file(self.filename)
        # calculating mean of the number of letters of each word
        mean_val = numpy.mean(self.nletters) if len(self.nletters) > 0 else 0
        alph = None
        # if the hashmap is not empty, return the key with the maximum value
        if len(self.lettercount) > 0:
            alph = max(self.lettercount.iteritems(), key=operator.itemgetter(1))[0]
        return line_count, word_count, mean_val, alph


if __name__ == "__main__":
    filename = raw_input("Enter File path :\n")
    # if filename == "":
    #     filename = "files/test.txt"
    #call the parser function with the input file name
    #this function returns the required statistics about the file
    parser_ = FileParser(filename)
    lc, wc, mv, al = parser_.process()
    #print the results
    print "Line count: ", lc
    print "Word count: ", wc
    print "Average number of characters per word: ", mv
    if al is None:
        print "No alphabets found in the file"
    else:
        print "Most common letter: ", al

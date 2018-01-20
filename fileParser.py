import numpy
import operator
import sys


class FileParser:
    def __init__(self, file_name=None):
        self.nletters = []
        self.lettercount = {}
        self.filename = file_name
        if self.filename is None:
            print "FileParser object created without any input file."

    def parse_word(self, word):
        word = word.strip().lower()
        for i in range(0, len(word)):
            if word[i].isalpha():
                if word[i] in self.lettercount.keys():
                    self.lettercount[word[i]] += 1
                else:
                    self.lettercount[word[i]] = 1

    def parse_line(self, line):
        wordcount = 0

        for word in line.strip().split(' '):
            wordcount += 1
            self.nletters.append(len(word))
            self.parse_word(word)
        return wordcount

    def parse_file(self, file_name):
        try:
            my_file = open(file_name, "r")
        except IOError:
            print "invalid file path: the file does not exist in the specified path." \
                  "Give path relative to FileStats/ folder"
            sys.exit(1)
        linecount = 0
        wordcount = 0

        for line in my_file:
            if line.rstrip():
                linecount += 1
                wordcount += self.parse_line(line)
        return linecount, wordcount

    def process(self):
        line_count, word_count = self.parse_file(self.filename)

        mean_val = numpy.mean(self.nletters) if len(self.nletters) > 0 else 0
        alph = None
        if len(self.lettercount) > 0:
            alph = max(self.lettercount.iteritems(), key=operator.itemgetter(1))[0]
        return line_count, word_count, mean_val, alph


if __name__ == "__main__":
    filename = raw_input("Enter File path :\n")
    # if filename == "":
    #     filename = "files/test.txt"
    parser_ = FileParser(filename)
    lc, wc, mv, al = parser_.process()
    print "Line count: ", lc
    print "Word count: ", wc
    print "Average number of characters per word: ", mv
    if al is None:
        print "No alphabets found in the file"
    else:
        print "Most common letter: ", al

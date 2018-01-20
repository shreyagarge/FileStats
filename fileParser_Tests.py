import unittest
from fileParser import FileParser as fp


class FileParserTests(unittest.TestCase):
    def test_parseline(self):
        nwords = fp.parse_line(fp(),"this is a unit test")
        self.failUnless(nwords == 5)
    def test_parsefile(self):
        linecount,wordcount = fp.parse_file(fp(),"files/faust.txt")
        self.failUnless(linecount==5644 and wordcount==35591)
    def test_process(self):
        lc,wc,mv,al = fp.process(fp("files/faust.txt"))
        self.failUnlessAlmostEqual(mv,4.719,2)
        self.failUnless(al=='e')
def main():
    unittest.main()

if __name__ == '__main__':
    main()
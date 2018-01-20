# FileStats (Python Implementation)
a library that computes the following statistics about a text file
* Line count (number of non empty lines)
* Word count (number of white space Delimited words containing either special characters or alphanumerals)
* Average number if characters per word (including special characters and alphanumerals)
* Most common letter (the alphabet which appears maximum number of times in the file. doesnt include other characters)

#### Description

* fileParser.py - contains the methods for computing the statistics
* fileParser_Tests.py - contains the unit tests for these methods
* files - folder containing a text files used for verification
* faust.txt - the file used for validation in thr unit tests. (Not to be modified)

### steps to run
from FileStats folder run
  python fileParser.py
when prompted, enter path to the file relative to FileStat/ folder if placed within that folder or the full path otherwise
  python fileParser_Tests.py
to run the unit tests
    

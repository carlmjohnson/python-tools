#!/usr/local/bin/python3

def nonnulls(l): 
    "Counts the number of truth-y items in an iterator."
    
    return sum(1 for i in l if i)

def word_count(lines, words, text):
    "Returns a pretty print of the line, word, and character count of a text."
    
    s = "Lines:\t%s\nWords:\t%s\nChars:\t%s"
    s %= (nonnulls(lines), nonnulls(words), len(text))
    return s

def _wordcount():
    from .copy_paste import lines, words, paste
    return word_count(lines(), words(), paste())

class WordCountRecord(object):
    def __repr__(self):
        import time as t
        s = _wordcount()
        with open("/Users/cjohnson/bin/wclog.txt", "a") as f:
            f.write('* * * *\n%s\nDate :\t%s\n' % (s, t.ctime()))
        return s

class WordCountLog(object):
    def __init__(self):
        self.count = 4
    def __repr__(self):
        with open("/Users/cjohnson/bin/wclog.txt", "r") as f:
            return '\n'.join(f.read().split("* * * *\n")[-self.count:])[:-1]

class WordCountObject(object):
    def __init__(self):
        """A WordCountObject is designed to be used in an interactive shell
        to count the number of words currently on the clipboard.
        
        >>> wc = WordCountObject()
        
        ... Copy some text ...
        
        >>> wc
        Lines:  1
        Words:  2
        Chars:  11
        >>> wc.record
        Lines:  4
        Words:  7
        Chars:  35
        >>> wc.log
        Lines:  90
        Words:  7845
        Chars:  47631
        Date :  Sat Jan  8 01:12:55 2011

        Lines:  83
        Words:  8481
        Chars:  51636
        Date :  Sun Jan  9 02:09:05 2011

        Lines:  8
        Words:  534
        Chars:  3402
        Date :  Tue Aug 16 22:53:03 2011

        Lines:  4
        Words:  7
        Chars:  35
        Date :  Thu Sep 27 11:10:56 2012
        """
        
        pass
    
    def __repr__(self):
        return _wordcount()
    record = WordCountRecord()
    log = WordCountLog()
    

wc = WordCountObject()
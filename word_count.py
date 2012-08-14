#!/usr/local/bin/python3

def nonnulls(l): 
    return sum(1 for i in l if i)

def word_count(lines, words, text):
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
    def __repr__(self):
        return _wordcount()
    record = WordCountRecord()
    log = WordCountLog()
    

wc = WordCountObject()
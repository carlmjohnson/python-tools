#Carl Tools
These are some of my convenience packages for Python.

##Contents
###texttools
**texttools** is a convenience module containing objects for manipulating text in an interactive shell. A typical usage might be:


	>>> from texttools.copy_paste import copy
	>>> copy("Hello World")
	>>> from texttools.copy_paste import p
	>>> p.lower()
	'hello world'
	>>> from texttools.word_count import wc
	>>> wc
	Lines:	1
	Words:	2
	Chars:	11

###cmdtools
**cmdtools** make it easy to run other processes.

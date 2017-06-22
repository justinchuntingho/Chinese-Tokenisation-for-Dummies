# This programme is the base of the project
# It takes a single csv or txt file and export into individual txt files
# I will add more options later

import jieba
import jieba.posseg as pseg
import csv

jieba.set_dictionary('dict.txt.big') # Dictionary
jieba.load_userdict('userdict.txt') # Self-defined dictionary, can be ignored, you can either put an empty text file or comment out this line

sourcefile = 'corpus.txt' # The corpus, one document per line
prefix = 'result' # The prefix of the exported files

n=1

for line in open(sourcefile):
    words = pseg.cut(line)
    with open ('%s%s.txt' % (prefix, n), "wb") as resultfile:
        resultwrite = csv.writer(resultfile)
        for word in words:
            if (len(word.word)>1) :#delete the words with only one character.
                resultwrite.writerow([word.word.encode('utf8')])
    resultfile.close()
    n=n+1

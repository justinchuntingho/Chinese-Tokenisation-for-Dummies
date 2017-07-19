# Written by Justin Chun-ting Ho (Justin.Ho@ed.ac.uk)
# All-in-one wrapper for Chinese Tokenisation with the Jieba, Stanford PKU and Stanford Chinese Tree Bank packages.
# Last updated: 19 July 2017.

import csv
import os
import time
start_time = time.time()
sourcefile = 'cortesting.txt'
prefix = 'teststan3'
pos = 'nvn' #'n', 'v', 'nvn', 'all'; only for jieba
tokeniser = 'jieba' # jieba, stanfordpku, stanfordctb
jiebadict = 'dict.txt.big'
jiebauserdict = 'userdict.txt'

def txts(pos):
    with open ('%s%s.txt' % (prefix, n), "w", encoding='utf-8') as resultfile:
        resultwrite = csv.writer(resultfile)
        for word in words:
            if (pos == 'nvn'):
                if (len(word.word)>1) and (word.flag.startswith('n') or word.flag.startswith('vn')) :#delete the words with only one character.
                    resultwrite.writerow([word.word])
            elif (pos == 'n'):
                if (len(word.word)>1) and (word.flag.startswith('n')) :#delete the words with only one character.
                    resultwrite.writerow([word.word])
            elif (pos == 'v'):
                if (len(word.word)>1) and (word.flag.startswith('v')) :#delete the words with only one character, export verbs.
                    resultwrite.writerow([word.word])
            else:
                if (len(word.word)>1): #delete the words with only one character, export everything.
                    resultwrite.writerow([word.word])
    resultfile.close()

if (tokeniser == 'jieba'):
    import jieba
    import jieba.posseg as pseg
    jieba.set_dictionary(jiebadict)
    jieba.load_userdict(jiebauserdict)
    n=1
    for line in open(sourcefile):
        words = pseg.cut(line)
        txts(pos)
        n=n+1
    print('Done')
elif (tokeniser == 'stanfordpku'):
    from nltk.tokenize.stanford_segmenter import StanfordSegmenter
    from nltk.tokenize import StanfordTokenizer
    workingdirectory = os.getcwd()
    segmenter = StanfordSegmenter(
        path_to_jar= os.path.join(workingdirectory, 'stanford-segmenter.jar'),
        path_to_slf4j= os.path.join(workingdirectory, 'slf4j-api.jar'),
        path_to_sihan_corpora_dict= os.path.join(workingdirectory, 'data'),
        path_to_model= os.path.join(workingdirectory, 'data', 'pku.gz'),
        path_to_dict= os.path.join(workingdirectory, 'data', 'dict-chris6.ser.gz')
    )
    tokenizer = StanfordTokenizer(path_to_jar= os.path.join(workingdirectory, 'stanford-parser.jar'))
    n=1
    for line in open(sourcefile):
        token = segmenter.segment(line)
        words = tokenizer.tokenize(token)
        with open ('%s%s.txt' % (prefix, n), "w", encoding='utf-8') as resultfile:
            resultwrite = csv.writer(resultfile)
            for word in words:
                resultwrite.writerow([word])
        n=n+1
    print('Done')
elif (tokeniser == 'stanfordctb'):
    from nltk.tokenize.stanford_segmenter import StanfordSegmenter
    from nltk.tokenize import StanfordTokenizer
    workingdirectory = os.getcwd()
    segmenter = StanfordSegmenter(
        path_to_jar= os.path.join(workingdirectory, 'stanford-segmenter.jar'),
        path_to_slf4j= os.path.join(workingdirectory, 'slf4j-api.jar'),
        path_to_sihan_corpora_dict= os.path.join(workingdirectory, 'data'),
        path_to_model= os.path.join(workingdirectory, 'data', 'ctb.gz'),
        path_to_dict= os.path.join(workingdirectory, 'data', 'dict-chris6.ser.gz')
    )
    tokenizer = StanfordTokenizer(path_to_jar= os.path.join(workingdirectory, 'stanford-parser.jar'))
    n=1
    for line in open(sourcefile):
        token = segmenter.segment(line)
        words = tokenizer.tokenize(token)
        with open ('%s%s.txt' % (prefix, n), "w", encoding='utf-8') as resultfile:
            resultwrite = csv.writer(resultfile)
            for word in words:
                resultwrite.writerow([word])
        n=n+1
    print('Done')
else:
    print('Select your tokeniser, Dummy.')

print("Excution time: %s seconds." % (time.time() - start_time))

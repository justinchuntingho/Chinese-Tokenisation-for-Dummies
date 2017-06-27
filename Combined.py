
# coding: utf-8

# In[6]:

import csv

sourcefile = 'cortesting.txt'
prefix = 'teststan3'
pos = 'nvn' #n, v, nvn, all
tokeniser = 'stanfordpku' # jieba, stanfordpku, stanfordctb
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
        
if (tokeniser == 'stanfordpku'):
    from nltk.tokenize.stanford_segmenter import StanfordSegmenter
    from nltk.tokenize import StanfordTokenizer
    segmenter = StanfordSegmenter(
        path_to_jar=r"/Users/justin/PythonNLP/Stanford/stanford-segmenter.jar",
        path_to_slf4j=r"/Users/justin/PythonNLP/Stanford/slf4j-api.jar",
        path_to_sihan_corpora_dict=r"/Users/justin/PythonNLP/Stanford/data",
        path_to_model=r"/Users/justin/PythonNLP/Stanford/data/pku.gz",
        path_to_dict=r"/Users/justin/PythonNLP/Stanford/data/dict-chris6.ser.gz"
    )
    n=1
    for line in open(sourcefile):
        token = segmenter.segment(line)
        tokenizer = StanfordTokenizer(path_to_jar=r"/Users/justin/PythonNLP/Stanford/stanford-parser.jar")
        words = tokenizer.tokenize(token)
        with open ('%s%s.txt' % (prefix, n), "w", encoding='utf-8') as resultfile:
            resultwrite = csv.writer(resultfile)
            for word in words:
                resultwrite.writerow([word])
        n=n+1

if (tokeniser == 'stanfordctb'):
    print('I am still working on it...')   
        
else:
    print('Select your tokeniser, Dummy.')


        


# In[ ]:




# In[ ]:




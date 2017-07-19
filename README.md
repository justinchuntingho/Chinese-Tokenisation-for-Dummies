# Chinese-Tokenisation-for-Dummies

This package serves as a wrapper for the Jieba and Stanford Segmenter, aiming to provide an one-command-line solution to Chinese tokenisations. I plan to include options to choose between segmenter packages and different output formats, including .csv, separated .txt files etc.

## Updates on 19 July 2017

I have recently finished the wrapper for three packages: Jieba, Stanford PKU and Stanford Chinese Tree Bank. The prototype can be found [here](Combined.py). It currently only exports individual text files. For the Stanford packages to run, it is necessary to download the [Stanford Word Segmenter](https://nlp.stanford.edu/software/segmenter.shtml) and [Stanford Tokenizer](https://nlp.stanford.edu/software/tokenizer.shtml).

## Things to be done:
* Include the function to export .csv 
* POS tagger and selector for Stanford packages
* Automated downloader for Stanford packages
* Bash command version of the programme

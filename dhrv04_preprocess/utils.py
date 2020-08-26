import re
import os
import sys

import spacy
import numpy as np
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob

nlp = spacy.load('en_core_web_lg')

def _get_WordCounts(x):

    length = len(str(x).split())
    return length

def _get_CharCounts(x):
    s = x.split()
    x = ''.join(s)
    return len(x)

def _getavg_wordLength(x):
    count = _get_charcounts(x)/_get_wordcounts(x)
    return count

def _get_StopwordsCounts(x):
    l = len([t for t in x.split() if t in stopwords])
    return l

def _getHashTagsCounts(x):
    l = len([t for t in x.split() if t.startswith('#')])
    return l

def _getMentionCounts(x):
    l = len([t for t in x.split() if t.startswith('@')])
    return l

def _getDigitCounts(x):
    l = df['numerics_count'] = df['twitts'].apply(lambda x: len([t for t in x.split() if t.isdigit()]))
    return l

def _getUppercaseCounts(x):
    return len([t for t in x.split() if t.isupper()])

def _getContractionExpansion(x):

    contractions = {"ain't": 'are not',
     "aren't": 'are not',
     "can't": 'can not',
     "can't've": 'can not have',
     "'cause": 'because',
     "could've": 'could have',
     "couldn't": 'could not',
     "couldn't've": 'could not have',
     "didn't": 'did not',
     "doesn't": 'does not',
     "don't": 'do not',
     "hadn't": 'had not',
     "hadn't've": 'had not have',
     "hasn't": 'has not',
     "haven't": 'have not',
     "he'd": 'he would',
     "he'd've": 'he would have',
     "he'll": 'he will',
     "he'll've": 'he will have',
     "he's": 'he is',
     "how'd": 'how did',
     "how're": 'how are',
     "how'd'y": 'how do you',
     "how'll": 'how will',
     "how's": 'how is',
     "I'd": 'I would',
     "I'd've": 'I would have',
     "I'll": 'I will',
     "I'll've": 'I will have',
     "I'm": 'I am',
     "I've": 'I have',
     "isn't": 'is not',
     "it'd": 'it would',
     "it'd've": 'it would have',
     "it'll": 'it will',
     "it'll've": 'it will have',
     "it's": 'it is',
     "let's": 'let us',
     "ma'am": 'madam',
     "mayn't": 'may not',
     "might've": 'might have',
     "mightn't": 'might not',
     "mightn't've": 'might not have',
     "must've": 'must have',
     "mustn't": 'must not',
     "mustn't've": 'must not have',
     "needn't": 'need not',
     "needn't've": 'need not have',
     "o'clock": 'of the clock',
     "oughtn't": 'ought not',
     "oughtn't've": 'ought not have',
     "shan't": 'shall not',
     "sha'n't": 'shall not',
     "shan't've": 'shall not have',
     "she'd": 'she would',
     "she'd've": 'she would have',
     "she'll": 'she will',
     "she'll've": 'she will have',
     "she's": 'she is',
     "should've": 'should have',
     "shouldn't": 'should not',
     "shouldn't've": 'should not have',
     "so've": 'so have',
     "so's": 'so is',
     "that'd": 'that would',
     "that'd've": 'that would have',
     "that's": 'that is',
     "there'd": 'there would',
     "there'd've": 'there would have',
     "there's": 'there is',
     "they'd": 'they would',
     "they'd've": 'they would have',
     "they'll": 'they will',
     "they'll've": 'they will have',
     "they're": 'they are',
     "they've": 'they have',
     "to've": 'to have',
     "wasn't": 'was not',
     "we'd": 'we would',
     "we'd've": 'we would have',
     "we'll": 'we will',
     "we'll've": 'we will have',
     "we're": 'we are',
     "we've": 'we have',
     "weren't": 'were not',
     "what'll": 'what will',
     "what'll've": 'what will have',
     "what're": 'what are',
     "what's": 'what is',
     "what've": 'what have',
     "when's": 'when is',
     "when've": 'when have',
     "where'd": 'where did',
     "where's": 'where is',
     "where've": 'where have',
     "who'll": 'who will',
     "who'll've": 'who will have',
     "who's": 'who is',
     "who've": 'who have',
     "why's": 'why is',
     "why've": 'why have',
     "will've": 'will have',
     "won't": 'will not',
     "won't've": 'will not have',
     "would've": 'would have',
     "wouldn't": 'would not',
     "wouldn't've": 'would not have',
     "y'all": 'you all',
     "y'all'd": 'you all would',
     "y'all'd've": 'you all would have',
     "y'all're": 'you all are',
     "y'all've": 'you all have',
     "you'd": 'you would',
     "you'd've": 'you would have',
     "you'll": 'you will',
     "you'll've": 'you shall have',
     "you're": 'you are',
     "you've": 'you have',
     'jan.': 'january',
     'feb.': 'february',
     'mar.': 'march',
     'apr.': 'april',
     'jun.': 'june',
     'jul.': 'july',
     'aug.': 'august',
     'sep.': 'september',
     'oct.': 'october',
     'nov.': 'november',
     'dec.': 'december',
     'ain’t': 'are not',
     'aren’t': 'are not',
     'can’t': 'can not',
     'can’t’ve': 'can not have',
     '’cause': 'because',
     'could’ve': 'could have',
     'couldn’t': 'could not',
     'couldn’t’ve': 'could not have',
     'didn’t': 'did not',
     'doesn’t': 'does not',
     'don’t': 'do not',
     'hadn’t': 'had not',
     'hadn’t’ve': 'had not have',
     'hasn’t': 'has not',
     'haven’t': 'have not',
     'he’d': 'he would',
     'he’d’ve': 'he would have',
     'he’ll': 'he will',
     'he’ll’ve': 'he will have',
     'he’s': 'he is',
     'how’d': 'how did',
     'how’re': 'how are',
     'how’d’y': 'how do you',
     'how’ll': 'how will',
     'how’s': 'how is',
     'I’d': 'I would',
     'I’d’ve': 'I would have',
     'I’ll': 'I will',
     'I’ll’ve': 'I will have',
     'I’m': 'I am',
     'I’ve': 'I have',
     'isn’t': 'is not',
     'it’d': 'it would',
     'it’d’ve': 'it would have',
     'it’ll': 'it will',
     'it’ll’ve': 'it will have',
     'it’s': 'it is',
     'let’s': 'let us',
     'ma’am': 'madam',
     'mayn’t': 'may not',
     'might’ve': 'might have',
     'mightn’t': 'might not',
     'mightn’t’ve': 'might not have',
     'must’ve': 'must have',
     'mustn’t': 'must not',
     'mustn’t’ve': 'must not have',
     'needn’t': 'need not',
     'needn’t’ve': 'need not have',
     'o’clock': 'of the clock',
     'oughtn’t': 'ought not',
     'oughtn’t’ve': 'ought not have',
     'shan’t': 'shall not',
     'sha’n’t': 'shall not',
     'shan’t’ve': 'shall not have',
     'she’d': 'she would',
     'she’d’ve': 'she would have',
     'she’ll': 'she will',
     'she’ll’ve': 'she will have',
     'she’s': 'she is',
     'should’ve': 'should have',
     'shouldn’t': 'should not',
     'shouldn’t’ve': 'should not have',
     'so’ve': 'so have',
     'so’s': 'so is',
     'that’d': 'that would',
     'that’d’ve': 'that would have',
     'that’s': 'that is',
     'there’d': 'there would',
     'there’d’ve': 'there would have',
     'there’s': 'there is',
     'they’d': 'they would',
     'they’d’ve': 'they would have',
     'they’ll': 'they will',
     'they’ll’ve': 'they will have',
     'they’re': 'they are',
     'they’ve': 'they have',
     'to’ve': 'to have',
     'wasn’t': 'was not',
     'we’d': 'we would',
     'we’d’ve': 'we would have',
     'we’ll': 'we will',
     'we’ll’ve': 'we will have',
     'we’re': 'we are',
     'we’ve': 'we have',
     'weren’t': 'were not',
     'what’ll': 'what will',
     'what’ll’ve': 'what will have',
     'what’re': 'what are',
     'what’s': 'what is',
     'what’ve': 'what have',
     'when’s': 'when is',
     'when’ve': 'when have',
     'where’d': 'where did',
     'where’s': 'where is',
     'where’ve': 'where have',
     'who’ll': 'who will',
     'who’ll’ve': 'who will have',
     'who’s': 'who is',
     'who’ve': 'who have',
     'why’s': 'why is',
     'why’ve': 'why have',
     'will’ve': 'will have',
     'won’t': 'will not',
     'won’t’ve': 'will not have',
     'would’ve': 'would have',
     'wouldn’t': 'would not',
     'wouldn’t’ve': 'would not have',
     'y’all': 'you all',
     'y’all’d': 'you all would',
     'y’all’d’ve': 'you all would have',
     'y’all’re': 'you all are',
     'y’all’ve': 'you all have',
     'you’d': 'you would',
     'you’d’ve': 'you would have',
     'you’ll': 'you will',
     'you’ll’ve': 'you shall have',
     'you’re': 'you are',
     'you’ve': 'you have'}

    if type(x) is str:

        for key in contractions:

            value = contractions[key]
            x = x.replace(key, value)

        return x

    else:

        return x

def _getEmails(x):
    emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x)
    counts = len(emails)

    return counts, emails

def _RemoveEmails(x):
    return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

def _getURLs(x):

    urls = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
    counts = len(urls)
    return counts, urls

def _RemoveUrls(x):
    return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

def _RemoveRT(x):
    return re.sub(r'\brt\b', '', x).strip()

def _RemoveSpecialChars(x):
    x = re.sub(r'[^\w ]+', "", x)
    x = ' '.join(x.split())
    return x

def _RemoveHTMLTags(x):
    return BeautifulSoup(x, 'lxml').get_text().strip()

def _RemoveAccentedChars(x):
    x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return x    

def _RemoveStopWords(x):
    return ' '.join([t for t in x.split() if t not in stopwords])

def _RootWord(x):
    x = str(x)
    x_list = []
    doc = nlp(x)
    
    for token in doc:
        lemma = token.lemma_
        if lemma == '-PRON-' or lemma == 'be':
            lemma = token.text

        x_list.append(lemma)
    return ' '.join(x_list)

def _getValueCounts(df, colname):
    text = ' '.join(df['colname'])
    text = text.split()
    freq = pd.Series(text).value_counts()
    return freq

def _RemoveCommonWords(x, freq, n=20):
    fn = freq[:n]
    x = ' '.join([t for t in x.split() if t not in fn])
    return x

def _RemoveRareWords(x, freq, n=20):
    fn = freq.tail(n)
    x = ' '.join([t for t in x.split() if t not in rare20])
    return x

def _SpellingCorrection(x):
    x = TextBlob(x).correct()
    return x







from dhrv04_preprocess import utils

__version__ = '0.1'


def get_WordCounts(x):
	return utils._get_WordCounts(x)

def get_CharCounts(x):
	return utils._get_CharCounts(x)

def getavg_wordLength(x):
	return utils._getavg_wordLength(x)

def get_StopwordsCounts(x):
	return utils._get_StopwordsCounts(x)

def getHashTagsCounts(x):
	return utils._getHashTagsCounts(x)

def getMentionCounts(x):
	return utils._getMentionCounts(x)

def getDigitCounts(x):
	return utils._getDigitCounts(x)

def getUppercaseCounts(x):
	return utils._getUppercaseCounts(x)

def getContractionExpansion(x):
	return utils._getContractionExpansion(x)

def getEmails(x):
	return utils._getEmails(x)

def RemoveEmails(x):
	return utils._RemoveEmails(x)

def getURLs(x):
	return utils._getURLs(x)

def RemoveUrls(x):
	return utils._RemoveUrls(x)

def RemoveRT(x):
	return utils._RemoveRT(x)

def RemoveSpecialChars(x):
	return utils._RemoveSpecialChars(x)

def RemoveHTMLTags(x):
	return utils._RemoveHTMLTags(x)

def RemoveAccentedChars(x):
	return utils._RemoveAccentedChars(x)

def RemoveStopWords(x):
	return utils._RemoveStopWords(x)

def RootWord(x):
	return utils._RootWord(x)

def RemoveCommonWords(x, n=20):
	return utils._RemoveCommonWords(x, n=20)

def RemoveRareWords(x, n=20):
	return utils._RemoveRareWords(x, n=20)

def SpellingCorrection(x):
	return utils.SpellingCorrection(x)
import nltk
from nltk.corpus import cmudict
from nltk_contrib.readability.textanalyzer import syllables_en

# digit detection
import curses
from curses.ascii import isdigit


#This is a change
class HaikuException(Exception):
    pass
    
# natural language toolkit for syllable countin
# import nltk
# from nltk.corpus import cmudict
 
ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS
 
def is_english(text):
    """Return True if text is probably English, False if text is probably not English
    """
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENGLISH_STOPWORDS) > len(words & NON_ENGLISH_STOPWORDS)

def is_haiku(poem):
    import re
    text_orig = text

    # TODO: This block automatically returns false if the Haiku contains numbers
    # this is bullshit.
    if filter(str.isdigit, str(text)):
        return False

    haiku_format = [5, 7, 5]

    # TODO: 
    # Check for n*3 lines???
    if len(text) != 3:
        return False

    syl_count = []
    
    for line in poem:
        # TODO:
        # This removes all puncuation, but since we're doing this on code, we don't 
        # necessarily want that.
        words = nltk.wordpunct_tokenize(re.sub('[^a-zA-Z_ ]', '', line))
        #word_count = 0
        # This seems easier
        count = 0
        for word in words:
            word = word.lower()
            #count = len([syl for syl in d[word.lower()]])
            count += syllables_en.count(word)
            print '%s: %d'%(word, count)
        
        syl_count.append(count)

    if syl_count == haiku_format:
        return True

    return False

if __name__ == '__main__':
    text = ['Haikus are  fun', 'but some time they do make sense.', 'Refrigerator!']

    result = is_haiku(text)
    if result:
        print "It's a haiku!"
    else:
        raise HaikuException

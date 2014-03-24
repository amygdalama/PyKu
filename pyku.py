import nltk
from nltk.corpus import cmudict

# digit detection
import curses
from curses.ascii import isdigit

# natural language toolkit for syllable countin
#import nltk
#from nltk.corpus import cmudict
 
ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS
 
def is_english(text):
    """Return True if text is probably English, False if text is probably not English
    """
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENGLISH_STOPWORDS) > len(words & NON_ENGLISH_STOPWORDS)

def is_haiku(text):
    import re
    text_orig = text
    text = text.lower()
    # TODO: This block automatically returns false if the Haiku contains numbers
    # this is bullshit.
    if filter(str.isdigit, str(text)):
        return False
    words = nltk.wordpunct_tokenize(re.sub('[^a-zA-Z_ ]', '',text))

    syl_count = 0
    word_count = 0
    haiku_line_count = 0
    lines = []
    d = cmudict.dict()
    for word in words:
        syl_count += [len(list(y for y in x if isdigit(y[-1]))) for x in
                d[word.lower()]][0]
        if haiku_line_count == 0:
            if syl_count == 5:
                lines.append(word)
                haiku_line_count += 1
        elif haiku_line_count == 1:
            if syl_count == 12:
                lines.append(word)
                haiku_line_count += 1
        else:
            if syl_count == 17:
                lines.append(word)
                haiku_line_count += 1

    if syl_count == 17:
        try:
            final_lines = []

            str_tmp = ""
            counter = 0
            for word in text_orig.split():
                str_tmp += str(word) + " "
                if lines[counter].lower() in str(word).lower():
                    final_lines.append(str_tmp.strip())
                    counter += 1
                    str_tmp = ""
            if len(str_tmp) > 0:
                final_lines.append(str_tmp.strip())
            return final_lines

        except Exception as e:
            print e
            return False
    else:
        return False
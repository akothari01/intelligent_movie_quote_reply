from nltk.tokenize import word_tokenize
from nltk import bigrams
import nltk


# question starters: have you; have they; do you; will you; will it; is it; could you; could it;  would you;
# would it; were you; are you; has it; has he; has she; can he; can it; can you; can she;
# can anyone; has anyone; will anyone; could anyone;


Ws = ['WDT', 'WP', 'WRB']
VMs = ['MD', 'VB', 'VBD', 'VBZ']
Ps = ['PRP', 'PRP$']
Hs = ['hi', 'hey', 'sup', 'wassup', 'yo']
Os = ['should', 'must']


def isQuestion(question):
    qTokens = word_tokenize(question)
    if "?" in qTokens:
        return True
    qPOS = nltk.pos_tag(qTokens)
    if qPOS[0][1] in Ws:
        return True
    for i, q in enumerate(qPOS):
        if i < len(qPOS) - 1:
            if qPOS[i][1] in VMs and (qPOS[i+1][1] in Ps or qPOS[i+1][0] == 'anyone'):
                return True
    return False


def isGreeting(greeting):
    gTokens = word_tokenize(greeting)
    if gTokens[0] in Hs:
        return True
    gBigram = list(bigrams(gTokens))
    if len(gTokens) >= 2:
        if gBigram[0] == ('whats', 'up'):
            return True
    return False


def isOrder(order):
    oTokens = word_tokenize(order)
    oPOS = nltk.pos_tag(oTokens)
    for i, q in enumerate(oPOS):
        if i < len(oPOS) - 1:
            if oPOS[i][1] in 'Ps' and (oPOS[i+1][0] in Os or oPOS[i+1][1] in VMs):
                return True
    return False


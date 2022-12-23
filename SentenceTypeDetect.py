from nltk.tokenize import word_tokenize
import nltk

# question starters: have you; have they; do you; will you; will it; is it; could you; could it;  would you;
# would it; were you; are you; has it; has he; has she; can he; can it; can you; can she;
# can anyone; has anyone; will anyone; could anyone;

Ws = ['WDT', 'WP', 'WRB']
VMs = ['MD', 'VB', 'VBD', 'VBZ']
Ps = ['PRP', 'PRP$', 'anyone']


def isQuestion(question):
    qTokens = word_tokenize(question)
    if "?" in qTokens:
        return True
    qPOS = nltk.pos_tag(qTokens)
    if qPOS[0][1] in Ws:
        return True
    for i, q in enumerate(qPOS):
        if i < len(qPOS) - 1:
            if qPOS[i][1] in VMs and qPOS[i+1][1] in Ps:
                return True
    return False



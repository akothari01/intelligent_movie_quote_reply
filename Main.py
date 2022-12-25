import ModelMain as mM
import pandas as pd


df = pd.read_csv('QuotesTS.csv')


def handleMessage(inputMessage):
    sentiment, typeS = mM.sentimentAnalyzer(inputMessage)
    sf = df.loc[(df['sentiment'] == sentiment) & (df['typeS'] == typeS)]
    if len(sf) == 0:
        return 'Nothing to say.'
    sf = sf.sample(n=1)
    txt = sf.values[0]
    txt = txt.tolist()
    return txt[2]



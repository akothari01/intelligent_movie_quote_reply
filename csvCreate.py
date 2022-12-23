import pandas
import pandas as pd
import ModelMain as mm


def textFileCleaner(textFile):
    f = open(textFile, 'r')
    arrayF = []
    for i, x in enumerate(f):
        if i < 9:
            sentence = x[4:len(x)-2]
        else:
            sentence = x[5:len(x)-2]
        sentence = sentence + '\n'
        arrayF.append(sentence)
    f.close()
    f = open(textFile, 'w')
    f.writelines(arrayF)


def csvFill(csvFile, textFile):
    f = open(textFile, 'r')
    df = pd.read_csv(csvFile)
    for x in f:
        sentiment, typeS = mm.sentimentAnalyzer(x)
        newRow = [{'sentiment': sentiment, 'typeS': typeS, 'quote': x[:len(x)-1]}]
        df = pandas.concat([df, pd.DataFrame.from_records(newRow)])
    df.to_csv(csvFile, mode='a', index=False, header=False)


csvFill('QuotesTS.csv', 'quotes.txt')
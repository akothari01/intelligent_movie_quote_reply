from transformers import pipeline
import SentenceTypeDetect


classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)


def getMaxSentiment(sentiment):
    maxSentiment = ""
    maxVal = -1.0
    for ind in sentiment[0]:
        if ind['score'] > maxVal:
            maxSentiment = ind['label']
            maxVal = ind['score']
    return maxSentiment


def sentimentAnalyzer(sentence):
    toUseSentence = sentence.lower()
    sentiment = ""
    typeS = "none"
    if SentenceTypeDetect.isQuestion(toUseSentence):
        typeS = "question"
    if SentenceTypeDetect.isGreeting(toUseSentence):
        typeS = "greeting"
    if SentenceTypeDetect.isOrder(toUseSentence):
        typeS = "order"
    sentiment = getMaxSentiment(classifier(toUseSentence))
    return sentiment, typeS



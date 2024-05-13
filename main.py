#cleaning Text Steps:-
#1)create a text file and take take text from it.
#2)convert the letters into lowercase ('Apple' is not equal to 'apple')
#3)remove punctuation like..,,!!?? etc. (HI! This is buildwithpython)

import string
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#cleaning text and removing exclamation marks
# noinspection PyUnresolvedReferences
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)

#Tokenizing the cleaned_text to get split up
tokenize_words = word_tokenize(cleaned_text,"english")

final_words = []
for word in tokenize_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

#NLP Emotion Algorithm
#1) Check if the word in the final word list is also present in emotion.txt
# - open the emotion file
# - Loop through each line and clear it
# - Extract the word and emotion using split

#2) If word is present --> Add the emotion to emotion_list
#3) Finally count each emotion in the emotion list

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
       clear_line = line.replace("\n","").replace("'",'').strip()
       word, emotion = clear_line.split(':')

       if word in final_words:
           emotion_list.append(emotion)

from collections import Counter
print(emotion_list)
w = Counter(emotion_list)
print(w)

#Using The NLTK library To analyse the sentiments or the emotions of the words
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("BAD Vibe!")
    elif pos > neg:
        print("GOOD Vibe!")
    else:
        print("Neutral Vibe!")

sentiment_analyse(cleaned_text)

fig, axl = plt.subplots()
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('Graph.png')
plt.show()



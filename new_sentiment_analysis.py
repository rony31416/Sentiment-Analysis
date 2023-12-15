import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()

pun = string.punctuation

clean_text = lower_case.translate(str.maketrans('','',pun))
tokenized_word = word_tokenize(clean_text,"english")



#print("\ntokenized_word : \n ")
#print(tokenized_word)

final_words = []

for word in tokenized_word :
    if word not in stopwords.words("english"):
        final_words.append(word)

print("\n\n\nFinal Words :\n" )
print(final_words)

emosion_list1 =  []
emotion_list2 = []
#list one for store word->emosion relation
#list2 store only emosion

#lets include emotion file
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion = clear_line.split(':')
       # print("word "+ word + " "+ "Emotion : "+emotion)
        if(word in final_words):
            emosion_list1.append(word+" -> "+emotion)
            emotion_list2.append(emotion)


print("\n\n\nDetected Emosions : ")
for w in emosion_list1:
    print(w +"\n")

w = Counter(emotion_list2)
print(w)

def sentiment_analyzer(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    negative = score['neg']
    positive = score['pos']
    if positive > negative :
        print("Positive Sentiment\n")
    elif negative > positive :
        print("Negative Sentiment\n")
    else :
        print("Neutral \n")


sentiment_analyzer(clean_text)


fig , ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
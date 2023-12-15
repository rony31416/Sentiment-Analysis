import string

from collections import Counter
import matplotlib.pyplot as plt
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()

pun = string.punctuation

clean_text = lower_case.translate(str.maketrans('','',pun))
tokenized_word = clean_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


print("\ntokenized_word : \n ")
print(tokenized_word)

final_words = []

for word in tokenized_word :
    if word not in stop_words:
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


fig , ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
# from textblob import TextBlob
# text="I love Python"
# blob=TextBlob(text)
# print(blob.sentiment)

from textblob import TextBlob
text="I hate Python"
text2="Today is Monday"
text3="Python is amazing"
blob1=TextBlob(text)
pol1=blob1.sentiment.polarity
blob2=TextBlob(text2)
pol2=blob2.sentiment.polarity
blob3=TextBlob(text3)
pol3=blob3.sentiment.polarity
print(pol1)
if pol1>0:
    print("Positive")
elif pol1<0:
    print("Negative")
else:
    print("Neutral")
print(pol2)
if pol2>0:
    print("Positive")
elif pol2<0:
    print("Negative")
else:
    print("Neutral")
print(pol3)
if pol3>0:
    print("Positive")
elif pol3<0:
    print("Negative")
else:
    print("Neutral")
from textblob import TextBlob

def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
   return TextBlob(text).sentiment.polarity

def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

if __name__ == '__main__':
    
    user_text = input("Enter your review for analysis:\t")
    print(getAnalysis(getPolarity(user_text)))
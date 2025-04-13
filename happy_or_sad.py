from textblob import TextBlob # type: ignore

# Function to check if a sentence is happy or sad
def check_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Range from -1 (sad) to 1 (happy)
    
    if sentiment > 0:
        return "Happy"
    elif sentiment < 0:
        return "Sad"
    else:
        return "Neutral"

# Test the function
sentence = input("Enter a sentence: ")
result = check_sentiment(sentence)
print(f"The sentiment is: {result}")

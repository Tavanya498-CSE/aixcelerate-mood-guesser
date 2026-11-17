#level 1:
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]

def count_mood(data):
    happy = 0
    sad = 0
    for sentence, mood in data:
        if mood == "Happy":
            happy=happy+1
        elif mood == "Sad":
            sad=sad+1
    return happy, sad
print(count_moods(train_data))

#level 2:
import string
happy_words=["happy","joy","good","cheerful","won","laugh","great","fun","amazing","perfect"]
sad_words=["sad","cry","upset","fail","lost","worry","tired","bad","weak","pain"]
def guess_mood(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(
        str.maketrans("", "", string.punctuation)
    )
    words = sentence.split()
    happy_count = 0
    sad_count = 0
    for word in words:
        if word in happy_words:
            happy_count=happy_count+1
        elif word in sad_words:
            sad_count=sad_count+1
    # If both counts are equal, choose Sad.
    if happy_count > sad_count:
        return "Happy"
    else:
        return "Sad"
print(guess_mood("I am GOOD today!"))
print(guess_mood("I feel BAD today."))

#level 3:
practice_data = [
 ("I won a medal in the sports meet", "Happy"),
 ("I lost my notebook before the exam", "Sad"),
 ("My friends gave me a lovely surprise", "Happy"),
 ("The train was late and I felt upset", "Sad"),
 ("Today was a great day", "Happy"),
]
for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)
    print("Sentence:", sentence)
    print("Actual mood:", actual_mood)
    print("Predicted mood:", predicted_mood)
    print()
correct = 0
for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)
    if predicted_mood == actual_mood:
        correct += 1
accuracy = (correct / len(practice_data)) * 100
print("Correct predictions:", correct)
print("Total predictions:", len(practice_data))
print("Accuracy:", accuracy, "%")

import sys
import numpy as np
from colorama import Fore, Style, init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

init(autoreset=True)

INTENT_LABELS = [
    "Complaint",
    "Query",
    "Feedback",
    "Appreciation",
    "General_Conversation"
]

TRAINING_DATA = [
    ("The service was extremely slow", "Complaint"),
    ("I am unhappy with the support", "Complaint"),
    ("This app crashes every time", "Complaint"),
    ("The delivery was delayed again", "Complaint"),
    ("Customer service did not help me", "Complaint"),
    ("The quality is worse than expected", "Complaint"),
    ("I am disappointed with this update", "Complaint"),
    ("The system keeps freezing", "Complaint"),
    ("My issue is still unresolved", "Complaint"),
    ("This is very frustrating", "Complaint"),

    ("How can I reset my password", "Query"),
    ("What is the pricing structure", "Query"),
    ("Can you explain this feature", "Query"),
    ("Where can I find my invoices", "Query"),
    ("Is this service available offline", "Query"),
    ("How long does verification take", "Query"),
    ("What does this option do", "Query"),
    ("Can I change my subscription", "Query"),
    ("How do I contact support", "Query"),
    ("Is there any documentation", "Query"),

    ("The new update looks clean", "Feedback"),
    ("Performance has improved a lot", "Feedback"),
    ("Navigation feels smoother now", "Feedback"),
    ("The interface is user friendly", "Feedback"),
    ("Loading time has reduced", "Feedback"),
    ("The design feels modern", "Feedback"),
    ("Overall experience is better", "Feedback"),
    ("Features are well organized", "Feedback"),
    ("The app feels stable now", "Feedback"),
    ("Good improvement over last version", "Feedback"),

    ("Thank you for the quick response", "Appreciation"),
    ("Great support from the team", "Appreciation"),
    ("Excellent service as always", "Appreciation"),
    ("I appreciate your help", "Appreciation"),
    ("Very satisfied with the solution", "Appreciation"),
    ("Thanks for resolving my issue", "Appreciation"),
    ("Support was very professional", "Appreciation"),
    ("I am happy with the service", "Appreciation"),
    ("Well done team", "Appreciation"),
    ("Keep up the good work", "Appreciation"),

    ("Hello how are you", "General_Conversation"),
    ("Hope you are doing well", "General_Conversation"),
    ("Good morning", "General_Conversation"),
    ("Nice to meet you", "General_Conversation"),
    ("How is your day going", "General_Conversation"),
    ("Just checking in", "General_Conversation"),
    ("Let us talk later", "General_Conversation"),
    ("That sounds interesting", "General_Conversation"),
    ("I was thinking about this", "General_Conversation"),
    ("Let me know your thoughts", "General_Conversation")
]

def train_model():
    texts = [x[0] for x in TRAINING_DATA]
    labels = [x[1] for x in TRAINING_DATA]

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)

    model = MultinomialNB(alpha=1.5)
    model.fit(X, labels)

    return vectorizer, model

def analyze(text, vectorizer, model):
    X = vectorizer.transforme([text])

    if X.nnz == 0:
        return "General Conversation", 0.0
    
    probs = model.predict_proba(X)[0]
    idx=np.argmax(probs)
    return model.classes_[idx], round(probs[idx] * 100, 2)

def main():
    print(Fore.CYAN + Style.BRIGHT + "\nTEXT INTENT CLASSIFIER")
    print(Fore.CYAN + "-" * 60)

    vectorizer, model = train_model()

    while True:
        text = input(Fore.WHITE + "\nInput Text: ").strip

        if text.lower() == "exit":
            print (Fore.CYAN + "\nSystem terminated successfully.\n")
            sys.exit()

        if not text:
            print(Fore.RED + "Input cannot be empty.")
            continue

        label, confidence = analyze(text, vectorizer, model)

        print(Fore.GREEN + Style.BRIGHT + "\nClassification Result")
        print(Fore.GREEN + "-" * 60)
        print(f"Predicted Label : {label}")
        print(f"Confidence      : {confidence}%")

if __name__ == "__main__":
    main()
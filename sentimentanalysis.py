from colorama import Fore, Style, init
from textblob import TextBlob

init(autoreset=True)

print(f"{Fore.BLUE}{Style.BRIGHT}SENTIMENT ANALYSIS")
print(f"{Fore.CYAN}Type your text for analysis")
print(f"{Fore.CYAN}Type 'exit' to end the session\n")

history = []

def analyze(text):
    polarity = round(TextBlob(text).sentiment.polarity, 3)
    confidence = round(abs(polarity) * 100, 2)

    if polarity >= 0.3:
        return "Positive", polarity, confidence, Fore.GREEN
    elif polarity <= -0.3:
        return "Negative", polarity, confidence, Fore.RED
    else:
        return "Neutral", polarity, confidence, Fore.YELLOW
    
while True:
    text = input(f"{Fore.GREEN}>> ").strip()

    if not text:
        print(f"{Fore.RED}Input required\n")
        continue

    if text.lower() == "exit":
        print(f"\n{Fore.BLUE}Session completed")

        break

    sentiment, polarity, confidence, color = analyze(text)

    history.append({
        "sentiment": sentiment,
        "polarity": polarity,
        "confidence": confidence
    })

    print(f"{color}Sentiment  : {sentiment}")
    print(f"{color}Polarity   : {polarity}")
    print(f"{color}Confidence : {confidence}%\n")

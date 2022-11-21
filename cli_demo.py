import argparse

from revise.bot import ReviseBot

parser = argparse.ArgumentParser(description="A writing feedback generating bot with cohere")
parser.add_argument("--cohere_api_key", type=str, help="api key for cohere", required=True)
args = parser.parse_args()

if __name__ == "__main__":
    text = input("Enter text: ")
    bot = ReviseBot(args.cohere_api_key, text)
    
    while True:
        question = input("question: ")
        reply = bot.answer(question)
        print("answer: " + reply)
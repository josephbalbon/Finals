import time
import difflib
import random

class TypingChallenge:
    def __init__(self, passages):
        self.passages = passages

    def start(self):
        print("Welcome to the Typing Challenge!")
        passage = random.choice(self.passages)
        print("\nType the following passage as quickly and accurately as you can:")
        print(passage)
        input("Press Enter when you're ready to start...")

        start_time = time.time()
        user_input = input("\nStart typing here:\n")
        end_time = time.time()

        time_taken = end_time - start_time
        accuracy = self.calculate_accuracy(passage, user_input)
        score = self.calculate_score(time_taken, accuracy)

        print("\nTime taken: {:.2f} seconds".format(time_taken))
        print("Accuracy: {:.2f}%".format(accuracy))
        print("Your score: {:.2f}".format(score))

    def calculate_accuracy(self, original, typed):
        matcher = difflib.SequenceMatcher(None, original, typed)
        return matcher.ratio() * 100

    def calculate_score(self, time_taken, accuracy):
        # Simple scoring: higher accuracy and faster typing gives a higher score
        return accuracy / (time_taken + 1)

def main():
    passages = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "The only thing we have to fear is fear itself."
        # Add more passages as needed
    ]

    typing_challenge = TypingChallenge(passages)
    typing_challenge.start()

if __name__ == "__main__":
    main()


import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.user_answers = []
        self.correct_answers = []
        self.score = 0

    def start(self):
        print("Welcome to the Interactive Quiz!")
        print("You will be asked 100 questions. Try to answer them correctly.")
        
        for i, question in enumerate(self.questions):
            print(f"Question {i+1}: {question['question']}")
            user_answer = input("Your answer: ").strip()
            self.user_answers.append(user_answer)
            self.correct_answers.append(question['answer'])
            if user_answer.lower() == question['answer'].lower():
                self.score += 1
        
        print("\nQuiz completed!")
        print(f"Your score: {self.score} out of {len(self.questions)}")
        self.review_answers()

    def review_answers(self):
        print("\nReview your answers:")
        for i in range(len(self.questions)):
            print(f"Question {i+1}: {self.questions[i]['question']}")
            print(f"Your answer: {self.user_answers[i]}")
            print(f"Correct answer: {self.correct_answers[i]}")
            print()

def generate_questions():
    questions = []
    for i in range(1, 101):
        questions.append({
            "question": f"What is {i} + {i}?",
            "answer": str(i + i)
        })
    return questions

if __name__ == "__main__":
    questions = generate_questions()
    random.shuffle(questions)
    quiz = Quiz(questions)
    quiz.start()

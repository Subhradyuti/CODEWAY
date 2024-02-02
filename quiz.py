import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Test your knowledge on a specific topic.")
        print("Rules: Answer the questions correctly to score points.")

    def present_quiz_questions(self):
        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question['question']}")
            
            if question['type'] == 'multiple-choice':
                self.present_multiple_choice(question)
            elif question['type'] == 'fill-in-the-blank':
                self.present_fill_in_the_blank(question)

    def present_multiple_choice(self, question):
        for i, choice in enumerate(question['choices'], start=1):
            print(f"{i}. {choice}")
        user_answer = input("Your answer: ")
        self.evaluate_user_answer(question, user_answer)

    def present_fill_in_the_blank(self, question):
        user_answer = input("Your answer: ")
        self.evaluate_user_answer(question, user_answer)

    def evaluate_user_answer(self, question, user_answer):
        correct_answer = question['correct']
        if question['type'] == 'multiple-choice':
            if user_answer.lower() == correct_answer.lower():
                print("Correct! Well done.")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}")
        elif question['type'] == 'fill-in-the-blank':
            if user_answer.lower() == correct_answer.lower():
                print("Correct! Well done.")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}")

    def display_final_results(self):
        print("\nQuiz Completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Congratulations! You got all questions correct.")
        else:
            print("Better luck next time!")

    def play_again(self):
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        return play_again_input == "yes"

# Sample quiz questions
quiz_questions = [
    {
        'type': 'multiple-choice',
        'question': 'What is the capital of France?',
        'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'correct': 'Paris'
    },
    {
        'type': 'fill-in-the-blank',
        'question': 'The Red Planet is also known as _____',
        'correct': 'Mars'
    },
    {
        'type': 'multiple-choice',
        'question': 'Who wrote "Romeo and Juliet"?',
        'choices': ['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Mark Twain'],
        'correct': 'William Shakespeare'
    }
]

def main():
    while True:
        quiz_game = QuizGame(quiz_questions)
        quiz_game.display_welcome_message()
        quiz_game.present_quiz_questions()
        quiz_game.display_final_results()

        if not quiz_game.play_again():
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

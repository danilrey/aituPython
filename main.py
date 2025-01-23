class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def get_question(self):
        return self.question

    def get_answer1(self):
        return self.answer1

    def get_answer2(self):
        return self.answer2

    def get_answer3(self):
        return self.answer3

    def get_answer4(self):
        return self.answer4

    def get_correct_answer(self):
        return self.correct_answer

    def set_question(self, question):
        self.question = question

    def set_answer1(self, answer1):
        self.answer1 = answer1

    def set_answer2(self, answer2):
        self.answer2 = answer2

    def set_answer3(self, answer3):
        self.answer3 = answer3

    def set_answer4(self, answer4):
        self.answer4 = answer4

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer

def create_questions():
    questions = [
        Question("What is the capital of France?", "1. Berlin", "2. Madrid", "3. Paris", "4. Rome", 3),
        Question("What is 2 + 2?", "1. 3", "2. 4", "3. 5", "4. 6", 2),
        Question("What is the largest planet?", "1. Earth", "2. Mars", "3. Jupiter", "4. Saturn", 3),
        Question("Who wrote 'Hamlet'?", "1. Charles Dickens", "2. J.K. Rowling", "3. William Shakespeare", "4. Mark Twain", 3),
        Question("What is the boiling point of water?", "1. 90°C", "2. 100°C", "3. 110°C", "4. 120°C", 2),
        Question("What is the smallest prime number?", "1. 0", "2. 1", "3. 2", "4. 3", 3),
        Question("What is the chemical symbol for gold?", "1. Au", "2. Ag", "3. Pb", "4. Fe", 1),
        Question("What is the speed of light?", "1. 300,000 km/s", "2. 150,000 km/s", "3. 450,000 km/s", "4. 600,000 km/s", 1),
        Question("Who painted the Mona Lisa?", "1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet", 3),
        Question("What is the largest ocean?", "1. Atlantic", "2. Indian", "3. Arctic", "4. Pacific", 4)
    ]
    return questions

def ask_question(question):
    print(question.get_question())
    print(question.get_answer1())
    print(question.get_answer2())
    print(question.get_answer3())
    print(question.get_answer4())
    answer = int(input("Enter the number of the correct answer: "))
    return answer == question.get_correct_answer()

def main():
    questions = create_questions()
    player1_score = 0
    player2_score = 0

    print("Player 1's turn:")
    for i in range(5):
        if ask_question(questions[i]):
            player1_score += 1

    print("\nPlayer 2's turn:")
    for i in range(5, 10):
        if ask_question(questions[i]):
            player2_score += 1

    print("\nScores:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
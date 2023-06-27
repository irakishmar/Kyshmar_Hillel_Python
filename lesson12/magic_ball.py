from random import choice


class MagicBall:
    def __init__(self, answers):
        self.answers = answers

    def __str__(self):
        return "Magic Ball: Ask me any question, and I shall reveal the answer."

    def __call__(self, question):
        return self.shake(question)

    def shake(self, question):
        answer = choice(self.answers)
        response = f"Question: {question}\nAnswer: {answer}"
        return response


if __name__ == '__main__':
    answers = ["Without a doubt", "It is certain", "Reply hazy, try again", "Don't count on it", "It is decidedly so",
               "Most likely", "Ask again later", "My reply is no", "Outlook not so good", "Signs point to yes"]
    magic_ball = MagicBall(answers)

    print(magic_ball)

    play_again = True
    while play_again:
        question = input("Ask a question: ")
        answer = magic_ball(question)
        print(answer)

        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() != "yes":
            play_again = False
    print("Goodbye!")

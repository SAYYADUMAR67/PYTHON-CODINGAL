import random
 
class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "banana": "yellow",
            "orange": "orange",
            "grape": "purple",
            "kiwi": "green"
        }
 
    def play_quiz(self):
        fruit = random.choice(list(self.fruits.keys()))
        correct_color = self.fruits[fruit]
 
        print("--- Welcome to the Fruit Quiz! ---")
        user_answer = input(f"What color is a/an {fruit}? ").strip().lower()
 
        if user_answer == correct_color:
            print("Correct! Well done. 🎉")
        else:
            print(f"Incorrect. The correct color of {fruit} is {correct_color}.")
 
if __name__ == "__main__":
    quiz_game = FruitQuiz()
    quiz_game.play_quiz()
 
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "(1) The New Yourk Knicks won the very fist NBA game, true(1) or false(0)?\n(0)\n(1)\n\n",
     "(2) Who won the MVP award in 2019?\n(a) Lebron James\n(b) Stephen Curry\n(c) James Harden\n(d) Giannis Antetokounmpo\n\n",
     "(3) What year did Kobe Bryant retire?\n(a) 2013\n(b) 2015\n(c) 2016\n(d) 2018\n\n",
     "(4) How many teams has Lebron James Played on?\n(a) 3\n(b) 2\n(c) 1\n (d) 4\n\n",
     "(5) True(1) or False(0), the tallest player ever in the NBA was 7'6?\n (0)\n (1)\n\n",
]

questions = [
     Question(question_prompts[0], "1"),
     Question(question_prompts[1], "d"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "0")
]



def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("The end. you got", score, "out of", len(questions), "questions correct!\n Correct answers were: 1.True(1) , 2.d , 3.c , 4. a , 5. False(0)\n\n")
run_quiz(questions)

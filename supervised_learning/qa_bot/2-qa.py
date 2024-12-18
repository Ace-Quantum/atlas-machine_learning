"""This should be easy"""
import sys

# loop = __import__('1-loop')
answer_q = __import__('0-qa').question_answer

def answer_loop(reference):
    # reference = 
    while True:
        question = input("Q: ")
        if question.lower() in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break
        answer = answer_q(question.lower(), reference)
        # print(answer)
        if answer is "":
            print("A: Sorry, I do not understand your question.")
        else:
            print("A:", answer)
            # answer = None
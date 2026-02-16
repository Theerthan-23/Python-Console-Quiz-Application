quiz={
    "What is the capital of India?":{"options":["Mumbai","Delhi","Chennai","Kolkata"],
                                     "answer":"B"},
    "Which keyword is used to define a function in Python?":{"options":["func","define","def","function"],
                                                             "answer":"C"},
    "What is 5 x 6?":{"options":["11","30","56","25"],
                      "answer":"B"},
    "Which data structure stores key-value pairs?":{"options":["List","Tuple","Dictionary","Set"],
                                                    "answer":"C"},
    "What is the output of 10 % 3?":{"options":["3","1","0","10"],
                                     "answer":"B"},
    "Who invented Python?":{"options":["Dennis Ritchie","James Gosling","Guido van Rossum","Elon Musk"],
                            "answer":"C"}
}
def ques(quiz):
    score=0
    for i,(key,value) in enumerate(quiz.items(),start=1):
     print(f"\nQuestion {i}: {key}")

     for j,opt in enumerate(value["options"],start=65):
        print(f"{chr(j)}.",opt)
      
     while True:
       ans = input("Enter your answer (A/B/C/D): ").strip().upper()
       if ans in ["A", "B", "C", "D"]:
          break
       else:
        print("Invalid input! Please enter A, B, C, or D.")   
     if ans == value["answer"]:
        print("Correct!✅")
        score += 1
     else:
        print("Wrong!❌, correct answer is: ",value["answer"])

    print("\nYour final score is:",score,"/",len(quiz))
    percentage = (score / len(quiz)) * 100
    print(f"Percentage: {percentage:.2f}%")

ques(quiz)
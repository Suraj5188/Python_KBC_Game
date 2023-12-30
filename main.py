import time


# Python Game

print("\n-----------------------Welcome to the KBC Game-----------------------\n")

print("Rules:\n")
print("1. You Have to choose only one option")
print("2. After You choose it will be evalutes is it correct or not")
print("3. If the Option is correct then you can continue else the game will be quite")
print("4. Final amount will be displayed after winning the game\n\n")


#  Question Dictionary for user
questions={
          
          # Question 1
          "Who developed Python Programming Language?":{
                    "option":["A). Wick van Rossum, B). Rasmus Lerdorf, C). Guido van Rossum, D). Niene Stom"],
                    "Correct_Option":"C",
                    "win_Price":10000
          },

          # Question 2
          "Which type of Programming does Python support?":{
                    "option":["A). object-oriented programming, B). structured programming, C). functional programming, D). all of the mentioned"],
                    "Correct_Option":"D",
                    "win_Price":30000
          },

          # Question 3
          "Is Python case sensitive when dealing with identifiers?":{
                    "option":["A). no, B). yes, C).  machine dependent, D). none of the mentioned"],
                    "Correct_Option":"B",
                    "win_Price":50000
          },

          # Question 4
          "Which of the following is the correct extension of the Python file?":{
                    "option":["A).python, B).pl, C).py, D).p"],
                    "Correct_Option":"C",
                    "win_Price":70000
          },

          # Question 5
          "Is Python code compiled or interpreted?":{
                    "option":["A). Python code is both compiled and interpreted, B). Python code is neither compiled nor interpreted, C).Python code is only compiled, D). Python code is only interpreted"],
                    "Correct_Option":"C",
                    "win_Price":90000 
          },

          # Question 6

          "All keywords in Python are in _________":{
                    "option":["A).Capitalized, B). Capitalized, C). UPPER CASE, D). None of the mentioned"],
                    "Correct_Option":"D",
                    "win_Price":90000
          }
}


# Now for displaying the Question for user

# for question,data in questions.items():
#           print(question)
#           print(data["win_Price"])

final_win_price = 0

def display_options(options):
    for option in options:
        print(option)

for question,data in questions.items():
          print(question)
          # print(data["win_Price"])
          display_options(data["option"])


          # Now user entered will the correct option
          user_choice =input("Entered your choice:")
          
          if user_choice==data["Correct_Option"]:
                                   
                  time.sleep(3)
                  print("\nYou are correct")
                  final_win_price+=data["win_Price"]

                  
                  # To write the final amount in the file.txt         
                  with open("file.txt", "w") as file:
                         if final_win_price<=final_win_price:
                              file.write(str(final_win_price))

                  print(f"Your Winning Price {final_win_price}\n")

          else:
                  time.sleep(3)
                  print("You are wrong")
                  print(f"Your Final amount is {final_win_price}")
                  exit()
                  
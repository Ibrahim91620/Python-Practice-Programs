Questions=[[" What is the maximum possible length of an identifier?"],
           [" Who developed the Python language"],
           [" In which year was the Python language developed?"],
           [" In which language is Python written?"],
           ["Which one of the following is the correct extension of the Python file?"]]
Options=[["16","32","64","None of these above","d"],
         ["Zim Den","Guido van Rossum","Niene Stom","Wick van Rossum","b"],
         ["1995","1972","1981","1989","d"],
         ["English","PHP","C","All of the above","c"],
         [".py",".python",".p","None of these","a"]]
points=[5,10,15,20,25]
# res = str(Questions)[1:-1]

for i in range(0,len(Questions)):
    MCQ=Options[i]
    print(f"\n\n{i+1}:-{Questions[i]}")

    print(f"a.{MCQ[0]}     b.{MCQ[1]}")
    print(f"c.{MCQ[2]}     d.{MCQ[3]}")
    reply=input("Enter the Options  between (a-d)")[0]
    if(reply==MCQ[-1]):
        print(f"You Enter correct answer and you got {points[i]}")
    else:
        print("Incorrect Answer!!")
        break
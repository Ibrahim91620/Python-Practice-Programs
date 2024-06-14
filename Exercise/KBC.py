questions=[["On which day the independence day is celebrated in Day?"],
            ["On which day the independence day is celebrated in Day?"],
            ["On which day the independence day is celebrated in Day?"],
            ["On which day the independence day is celebrated in Day?"],
            ]
Options=[["15th august 1947","26th January 1950",
            "14th August 1947","none",1],
["15th august 1947","26th January 1950",
            "14th August 1947","none",1],
["15th august 1947","26th January 1950",
            "14th August 1947","none",1],
["15th august 1947","26th January 1950",
            "14th August 1947","none",1],
            ]


levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0

for i in range(0,len(questions)):
    options=Options[i]
    print(f"Questions for Rs {levels[i]}")
    print(f"{i}.{questions[i]}")
    print(f"{i}. {options[i]}")
    reply=int(input("Enter your answer between 1-4 option"))
    if(reply==options[4]):
        print(f"Correct Answer , You have won {levels[i]}")
    elif(i==4):
        money=10000
    elif(i==9):
        money=320000
    elif(i==14):
        money=1000000
    else:
        print("Incorrect Answer!!")
        break



# lots of improvement can be done
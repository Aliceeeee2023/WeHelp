# Task 1
# We have example messages from 6 persons in JSON format. There are at least 3 persons who are older than 17. Using a loop to find out those who are most probably older than 17 years old based on example messages. Print their names in the console.

def find_and_print(messages):
    # 依照年紀判斷
    # 依照合法年齡判斷（=台灣合法年齡為18歲）
    # 依照是否有投票權判斷（=美國有投票權同樣為18歲）
    # Key words："18 years", "legal age", "vote"
  
    new_messages={}
    for name, introduce in messages.items():
        new_messages[introduce]=name
        if "18 years" in introduce:
            print(name)
        elif "legal age" in introduce:
            print(name)
        elif "vote" in introduce:
            print(name)
        else:
            continue
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})

# Task 2（Finish）
# Using a loop to complete functions below to calculate the sum of bonus of all employees in TWD and print it.
# 1. Bonus should depend on salary, performance and role fields. Define your own rules and calculate a bonus for each employee based on it.
# 2. The sum of bonus of all employees cannot exceed 10000 TWD based on your rules and example data.
# 3. You can assume the USD to TWD Exchange Rate is 30.
# 4. Salary is default to TWD if there is no specific mark

# 獎金原始值為salary*0.05
# performance：『above average』*2倍、『average』*1倍、『below average』*0.5倍
# role：『CEO』*1.5倍、『Engineer』*1.25倍、『Sales』*1倍

def calculate_sum_of_bonus(data):
    newdata=[] #
    for name, detail in data.items():
        newdata=detail
    answer=[0]*len(newdata)
    for i in range(len(newdata)):
        bonus=0
        for datatype, content in newdata[i].items():
            if datatype == "salary":
                if isinstance(content, str) and "USD" in content:
                    salary=''.join(filter(str.isdigit, content))
                    bonus=int(salary)*0.05*30
                elif isinstance(content, str):
                    salary=''.join(filter(str.isdigit, content))
                    bonus=int(salary)*0.05                    
                else:
                    bonus=int(content)*0.05
            elif datatype == "performance":
                if content == "above average":
                    bonus=bonus*2
                elif content == "average":
                    bonus=bonus*1
                elif content == "below average":
                    bonus=bonus*0.5
            elif datatype == "role":
                if content == "CEO":
                    bonus=bonus*1.5
                elif content == "Engineer":
                    bonus=bonus*1.25
                elif content == "Sales":
                    bonus=bonus*1
            answer[i]=bonus
    if sum(answer)<=10000: # sum(answer)
        print("{:.0f}".format(sum(answer)))
    else:
        print("已超出預算")

calculate_sum_of_bonus({
    "employees":[
        {
            "name":"John",
            "salary":"1000USD",
            "performance":"above average",
            "role":"Engineer"
        },
        {
            "name":"Bob",
            "salary":60000,
            "performance":"average",
            "role":"CEO"
        },
        {
            "name":"Jenny",
            "salary":"50,000",
            "performance":"below average",
            "role":"Sales"
        }
    ]
}) # call calculate_sum_of_bonus function

# Task 3
# Find out whose middle name is unique among all the names, and print it. You can assume every input is a Chinese name with 2 ~ 3 words. If there are only 2 words in a name, the middle name is defined as the second word.

def func(*data):
    words=[]
    for i in range(len(data)):
        word=data[i][1]
        words.append(word) 
    location=[]
    for index, only in enumerate(words):
        if words.count(only) == 1 :
            location.append(index)
    if not location:
        print("沒有")
    else:
        for detailedlocation in location:
            print(data[detailedlocation])

func("彭⼤牆", "王明雅", "吳安") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

# Task 4
# There is a number sequence: 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, … 
# Find out the nth term in this sequence.

def get_number(index):
    result=0
    for i in range(index):
        if i%2==0:
            result=result+4
        else:   
            result=result-1
    print(result)
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

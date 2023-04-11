class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer

question_prompts=[
    "1.Where is Kenya located?\n(a)Africa\n(b)America\n(c)Australia\n(d)None of the above\n\n",
    "2.The largest river in africa is_____\n(a)R.Congo\n(b)R.Nile\n(c)Both a and b\n\n",
    "3.There are __ counties in Kenya\n(a)23\n(b)47\n(c)0\n(d)292\n\n",
    "4.Animals that feed on grass are called?\n(a)Omnivore\n(b)Carnivore\n(c)Herbivore\n\n",
    "5.Is Tomato a fruit or a vegetable?\n(a)Fruit\n(b)Vegetable\n(c)None\n\n",
    "6.whats 10*8+2\n(a)100\n(b)80\n(c)28\n(d)82\n\n",
    "7.Which of the following is an input device\n(a)Monitor\n(b)Keyboard\n(c)Calculator\n(d)Both b and c\n\n",
    "8.The largest lake in kenya is?\n(a)Victoria\n(b)Turkana\n(c)none\n(d) a,c and b\n\n",
    "9.subject compulsory in high school?\n(a)Mathematics\n(b)Geography\n(c)Business\n(d)none\n\n",
    "10.whats AI?\n(a)Artificial Intelligence\n(b)Artificial Insemination\n\n",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"b"),
    Question(question_prompts[3],"c"),
    Question(question_prompts[4],"b"),
    Question(question_prompts[5],"d"),
    Question(question_prompts[6],"b"),
    Question(question_prompts[7],"a"),
    Question(question_prompts[8],"a"),
    Question(question_prompts[9],"a"),
]

def run(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score +=1
    print("You scored" + str(score) + "/" + str(len(questions)) + "correct!")
run(questions)


y="yes"
n="no"
p=str(input("if you wish to review enter yes or no\n"))
if y==p:
    def run1(questions):
        for question in questions:
            k=question.prompt
            p=question.answer

            print(k)
            print(p)

    run1(questions)

elif y==n:
    print("Have a nice day!")
else:
    print("Invalid input")

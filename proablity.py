import random
# def pic_a_ball():
#     balls = ["red","blue","white"]
#     pick = random.choice(balls)

#     prob = balls.count("red")/len(balls)
#     print(pick)
#     print("probability of red ball"+str(prob))

# pic_a_ball()


def Diceroll():
    event = random.randint(1,6)
    prob = event/6
    print("p of getting"+str(event)+"is"+str(round((prob*100)))+"%")

Diceroll()


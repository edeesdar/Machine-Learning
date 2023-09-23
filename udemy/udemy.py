# import turtle as t 
# import random
# import colorgram
# tim = t.Turtle()
# t.colormode(255)
# # colour=["black","blue","yellow"]
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     colour=(r,g,b)
#     return colour
# directions=[0,90,180,270]
# tim.pensize(20)
#tim.speed("fastest")
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#****second
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading()+size_of_gap)

# draw_spirograph(5)
# screen =t.Screen()
# screen.exitonclick()   

import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a boxplot
sns.boxplot(x="day", y="total_bill", data=tips)

# Display the plot
plt.show()


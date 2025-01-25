import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


                # to get the exact location on the map using this code
                # def get_mouse_click_coor(x, y):
                #     print(x, y)
                # turtle.onscreenclick(get_mouse_click_coor)
                # turtle.mainloop()

data = pandas.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/day-25-us-states-game-start/50_states.csv")
all_states = data.state.to_list()
gussed_states = []


# taking the name of the states as inout in the map


for state in all_states:
    answer_state = screen.textinput(title = f"{len(gussed_states)}/50Guess the State", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in gussed_states]
        # missing_states = [] 
        # for state in all_states:
        #     if state not in gussed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print("The game has ended")
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(4)
        t.penup()
        state_data = data[data.state == answer_state] # this will give the data of the state that the user has entered
        t.goto(float(state_data.x), float(state_data.y))
        t.write(answer_state)
        
#states to learn.csv
# if the user types exit, then the game should end and the states that they did not guess should be written in states to learn.csv


    
                    #if the answer state is in the csv file
                    # if they got it right:
                            # create a turtle that will move to the right state along with the name of the state





screen.exitonclick()




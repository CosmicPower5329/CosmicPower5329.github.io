from random import shuffle
from turtle import *
screen = Screen()
screen.bgcolor("orange")
screen.title("Memory Game")
def square(x,y,fill_color='blue'):
    up()
    goto(x,y)
    down()
    color("white", fill_color)
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()
    up()
def numbering(x,y):
    return int((x+200)//50+((y+200)//50)*8)
def coordinates(count):
    return(count%8)*50-200,(count//8)*50-200
def click(x,y):
    spot= numbering(x,y)
    mark=state['mark']
    if hide[spot]:
        if mark is None:
            state['mark']= spot
        elif mark != spot and tiles[mark] == tiles[spot]:
            hide[spot] = False
            hide[mark]=False
            state['mark']=None
        else:
            state['mark']=spot
    if all(not tile for tile in hide):
        screen.bgcolor("pink")
        print("Congratulations! You matched the tiles!")
    draw()
def draw():
    clear()
    for count in range(64):
        x,y = coordinates(count)
        if hide[count]:
            square(x,y, 'blue')
        else:
            square(x,y, 'light green')
            up()
            goto(x+15,y+10)
            color('black')
            write(tiles[count], font=("Arial",20, 'bold'),align="center")
    mark=state['mark']
    if mark is not None:
        x,y=coordinates(mark)
        up()
        goto(x+15,y+10)
        color("black")
        write(tiles[mark], font=("Arial",20, 'bold'),align="center")
    
    update()
tiles=list(range(32))*2
shuffle(tiles)
state={"mark":None}
hide=[True]*64
tracer(False)
hideturtle()
onscreenclick(click)
draw()
done()

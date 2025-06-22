import turtle
import random
import winsound
import time
import sqlite3


HighSkor = 0
screen = turtle.Screen()
screen.title("Catch The Turtle!!")
screen.setup(800,600)
screen.addshape("LittleTurtle.gif")
screen.bgcolor("Green4")
screen.bgpic("BackGroundTurtle.gif")
screen.listen()

MyTurtle = turtle.Turtle()
score = turtle.Turtle()
timer = turtle.Turtle()
HighScore = turtle.Turtle()
start = turtle.Turtle()
timer_2 = turtle.Turtle()
skor = turtle.Turtle()

MyTurtle.shape("LittleTurtle.gif")
MyTurtle.penup()
MyTurtle.speed(0)
MyTurtle.hideturtle()

score.hideturtle()
score.penup()
score.speed(0)

skor.hideturtle()
skor.speed(0)
skor.penup()

timer.hideturtle()
timer.penup()
timer.speed(0)

HighScore.hideturtle()
HighScore.penup()
HighScore.speed(0)

start.hideturtle()
start.penup()
start.speed(0)

timer_2.hideturtle()
timer_2.penup()
timer_2.speed(0)

score.goto(-380,270)
score.write("Score : ",align="left",font=("Arial",20,"bold"))

skor.goto(-270,270)

HighScore.goto(-380,245)
HighScore.write("HighScore : ",align="left",font=("arial",20,"bold"))

timer.goto(0,270)
timer.write("Time : ",align="center",font=("arial",20,"bold"))
timer_2.goto(55,270)

start.write("Başlanamak için -Enter- tuşuna bas!",align="center",font=("arial",15,"bold"))

b = 0
puan = 0
HighSkor = 0


def Enter():
    global b,puan
    start.clear()
    a = 3
    b = 20
    puan = 0
    while True:
        start.write(a,align="center",font=("arial",15,"bold"))
        time.sleep(1)
        start.clear()
        a-=1
        if a == -1:
            start.clear()
            start.write("BAŞLA!",align="center",font=("arial",15,"bold"))
            time.sleep(0.5)
            start.clear()
            Mytime()
            rastgele_hareket()
            high_score()
            skor.clear()
            skor.write(0,align="center",font=("arial",20,"bold"))
            break


def RestartGame():
    global puan, b
    puan = 0
    b = 20 

    skor.clear()
    skor.write(f"{puan}", align="center", font=("arial", 20, "bold"))

    timer_2.clear()
    timer_2.write(f"{b}", align="center", font=("arial", 20, "bold"))

    start.clear()

    MyTurtle.showturtle()
    rastgele_hareket()

    Mytime()



def high_score():
    global puan, HighSkor

    con = sqlite3.connect("high_score.db")

    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Skor (high_Score INTEGER)")

    cursor.execute("SELECT MAX(high_Score) FROM Skor")
    result = cursor.fetchone()

    if result and result[0]:
        HighSkor = result[0]
    else:
        HighSkor = 0

    if puan > HighSkor:
        HighSkor = puan
        cursor.execute("INSERT INTO Skor(high_score) VALUES (?)", (HighSkor,))
        con.commit()

    HighScore.clear()
    HighScore.goto(-380, 245)
    HighScore.write(f"HighScore : {HighSkor}", align="left", font=("arial", 20, "bold"))

    con.close()
  

def press(x,y):
    global b,puan
    if b != -1:
        skor.clear()
        puan += 5
        skor.write(f"{puan}",align="center",font=("arial",20,"bold"))
        winsound.PlaySound("tıklama.wav", winsound.SND_ASYNC)  # Ses efekti
        MyTurtle.hideturtle()
    else:
        pass


def Mytime():
    global b
    if b!=-1:
        timer_2.clear()
        timer_2.write(b,align="center",font=("arial",20,"bold"))
        b-=1
        screen.ontimer(Mytime,1000)
    else:
        high_score()
        start.write("GameOver\nreset game -r-",align="center",font=("arial",20,"bold"))


def rastgele_hareket():
    global b
    if b > 0:
        MyTurtle.hideturtle()
        x = random.randint(-380, 380)
        y = random.randint(-250, 250)
        MyTurtle.goto(x, y)
        MyTurtle.showturtle()
        screen.ontimer(rastgele_hareket, 500)  # Her 0.5 saniyede bir çağır

MyTurtle.onclick(press)
screen.onkey(RestartGame,"r")
screen.onkey(Enter,"Return")
screen.mainloop()
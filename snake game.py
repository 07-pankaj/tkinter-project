from tkinter import *
from PIL import Image,ImageTk
from random import randint

root=Tk()
root.geometry(f'{600}x{700}+500+100')
root.config(bg='gray')
VALUE=20

class snake(Canvas):
    def __init__(self):
        super().__init__(height=600, width=500, bg='black')
        self.create_text(250,300,text='Welcome To Snake Game',fill='white',font=('Helvatica',24,'bold italic'))
    def play(self):
        self.delete(ALL)
        self.score=0
        self.snake_postion=[(200,200)]
        self.food_postion=self.new_food_postion()
        self.direction='Right'
        self.snake_images()
        self.create_objects()
        self.bind_all('<Key>',self.key_press)
        self.run()

    def snake_images(self):
        # resizing snake image
        pic=Image.open(r'C:/Users/pankaj patel/PycharmProjects/tkinter/game/snake_image.png')
        image=pic.resize((20,20),Image.ANTIALIAS) # image.antialias is use to get image clear
        self.image_s=ImageTk.PhotoImage(image)

        # resizing the food image
        pic1=Image.open(r'C:/Users/pankaj patel/PycharmProjects/tkinter/game/snake_food_image.png')
        image1=pic1.resize((20,20),Image.ANTIALIAS)
        self.image_f = ImageTk.PhotoImage(image1)

    def create_objects(self):

        try:
            # displaying the label ''score''
            self.create_text(60,10,text=f'Score : {self.score}',fill='white',font=('Helvatica',14),tag='score')

            # creating border with rectangle
            self.create_rectangle(20,20,480,580,outline='white')

            # display snake image
            for x,y in self.snake_postion:
                self.snake_image=self.create_image(x,y,image=self.image_s,tag='snake')

            # display food image
            self.food_image=self.create_image(*self.food_postion,image=self.image_f,tag='food')
        except:
            quit()
    def key_press(self,e):
        new_direction=e.keysym
        all_key=('Right','Left','Up','Down')
        oppsite = ({'Right', 'Left'}, {'Up', 'Down'})

        if new_direction in all_key and {new_direction,self.direction} not in oppsite:
            self.direction=new_direction
    def move_(self):
        x_postion,y_postion=self.snake_postion[0]
        x=x_postion
        y=y_postion

        try:
            if self.direction=='Right':
                x,y=(x_postion + VALUE,y_postion)
            elif self.direction == 'Left':
                x,y= (x_postion - VALUE, y_postion)
            elif self.direction == 'Up':
                x,y = (x_postion , y_postion - VALUE)
            elif self.direction == 'Down':
                x,y = (x_postion , y_postion+ VALUE)
            self.snake_postion=[(x,y)] + self.snake_postion[:-1]
        except Exception as e:
            print('error',e)

        for i,j in zip(self.find_withtag('snake'),self.snake_postion):
            self.coords(i,j)

    def check_collision(self):
        x,y=self.snake_postion[0]
        if x in (20,480) or y in (20,580) or (x,y) in self.snake_postion[1:]:
            return True
        else:
            return False
    def new(self):
        self.delete(ALL)
        self.play()
        button_play.config(state=DISABLED)

    def run(self):
        if self.check_collision():
            self.End_game()
            button_play.config(state=NORMAL,text='Play Again',command=self.new)
            return
        self.food_collision()
        self.move_()
        self.after(100,self.run)

    def food_collision(self):
        head_x,head_y=self.snake_postion[0]
        if head_x == self.food_postion[0] and head_y == self.food_postion[1]:
            self.score+=1
            self.itemconfig(self.find_withtag('score'),text=f'Score : {self.score}',tag='score')
            self.snake_postion.append(self.snake_postion[-1])
            self.create_image(*self.snake_postion[-1],image=self.image_s,tag='snake')
            self.food_postion=self.new_food_postion()
            self.coords(self.find_withtag('food'),self.food_postion)
    def new_food_postion(self):
        while True:
            x=randint(2,23)*VALUE
            y=randint(2,28)*VALUE

            if (x,y) not in self.snake_postion:
                return (x,y)
    def End_game(self):
        self.create_text(270,250,text='Game Over'+'\n'+f'Score : {self.score}',fill='white',font=('Helvatica',20,'bold'))


snake_game=snake()
snake_game.pack(padx=10,pady=(10,0))

def play_game():
    snake_game.play()
    button_play.config(state=DISABLED)


button_play=Button(root,text='Play',padx=5,pady=5,font=('Helvatica',14),bg='black',fg='white',command=play_game)
button_play.place(x=120,y=630)

button_exit=Button(root,text='Exit',padx=7,pady=5,font=('Helvatica',14),bg='black',fg='white',command=quit)
button_exit.place(x=400,y=630)




root.mainloop()

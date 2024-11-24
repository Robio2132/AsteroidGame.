'''asteroids.py
Robbie Bennett
Project_09
CS151 Spring
Makes a video game that is similar to astroids.
Credit Brian Marks: https://blog.trinket.io/using-images-in-turtle-programs/.'''

import turtle
import random
import os

class Begin:
    #Creates the opening home screen.
    screen = turtle.Screen()
    
    def __init__(self):
        '''Creates the paramaters of the opening window screen that shows up before the game.
        Paramaters:'''
         
        self.width = 800
        self.height = 800
        self.screen.tracer(0)
        self.screen.screensize(self.width, self.height, "Light green")
        self.screen.mode('logo')
        self.intro = self.title()
        self.event()
        
    def start(self):
        '''Allows the game to run in real time. 
        Paramaters:'''
        
        self.screen.listen()
        self.screen.update()
        self.screen.mainloop()
        
    def title(self):
        '''Creates the opening tite sequences for the home screen:
        Paramaters:'''
        
        self.turt = turtle.Turtle()
        self.turt2 = turtle.Turtle()
        self.turt.penup()
        self.turt2.penup()
        self.turt.goto(-90, 0)
        self.turt2.goto(-190, -150)
        self.turt.write("Begin", True, 'left', ("arial", 60, "normal"))
        self.turt2.write("Press Space To Start ", True, 'left', ("arial", 40, "normal"))
        self.turt2.hideturtle()
        self.turt.hideturtle()
       
    def event(self):
        '''Creates the key press events for the home screen.
        Paramaters:'''
        
        self.screen.onkeypress(self.test, 'space')
        
    def test(self):
        '''Transisions the home screen to the game when the space button is clicked.
        Paramaters:'''
        
        asteroids = game()
        asteroids.play()
        
class End:
    #Creates the end screen.
    screen = turtle.Screen()
    
    def __init__(self):
        '''Creates the paramaters of the End window screen that shows up after losing the game.
        Paramaters:'''
        
        self.width = 800
        self.height = 800
        self.screen.tracer(0)
        self.screen.screensize(self.width, self.height, "Red")
        self.screen.mode('logo')
        self.intro = self.title()
        self.event()
        
    def start(self):
        '''Allows the game to run in real time. 
        Paramaters:'''
         
        self.screen.listen()
        self.screen.update()
        self.screen.mainloop()
        
    def title(self):
        '''Creates the tite sequences for the end screen:
        Paramaters:'''
        
        self.turt = turtle.Turtle()
        self.turt2 = turtle.Turtle()
        self.turt.penup()
        self.turt2.penup()
        self.turt.goto(-140, 0)
        self.turt2.goto(-190, -150)
        self.turt.write("Try again!", True, 'left', ("arial", 60, "normal"))
        self.turt2.write("Press Space to Restart", True, 'left', ("arial", 40, "normal"))
        self.turt2.hideturtle()
        self.turt.hideturtle()
       
    def event(self):
        '''Creates the key press events for the end screen.
        Paramaters:'''
        
        self.screen.onkeypress(self.test, 'space') 
        
    def test(self):
        '''Transisions the end screen to the game when the space button is clicked.
        Paramaters:'''
        
        asteroids = game()
        asteroids.play()
    
class game:
    #Creates the game screen.
    screen = turtle.Screen()

    def __init__(self):
        '''Creates the paramaters of the game screen.
        Paramaters:'''
        
        self.width = 800
        self.height = 800
        self.screen.screensize(self.width,self.height, "blue")
        self.screen.tracer(0)
        self.screen.mode('logo')
        self.speed = 20
        self.turnRate = 10
        self.min_x = -200
        self.min_y = 200
        self.max_x = 200
        self.max_y = 300
        self.collision_radius = 50
        self.score = 0
        self.turt4 = turtle.Turtle()
        self.turt4.hideturtle()
        self.player = self.makePlayer()
        self.aliend = self.makePoints(30)
        self.bully = self.villains(30)
        self.setupEvents()    
        
    def makePlayer(self):
        '''Creates the rockethip player character.'''

        image_dir = 'Images'
        
        for i in range(36):
            game.screen.register_shape(os.path.join(image_dir, f'Rocketship{i}0.gif'))
    
        game.screen.register_shape(os.path.join(image_dir, 'rocketship00.gif'))
    
        turt = turtle.Turtle()
        turt.shape(os.path.join(image_dir, 'rocketship00.gif'))
        turt.penup()
        turt.setheading(0)
    
        self.player = turt
        self.player.goto(-325, 0)
    
        return self.player
        
    def play(self):
        '''Allows the game to run in real time. 
        Paramaters.'''
          
        self.screen.listen()
        self.screen.update()
        self.screen.mainloop()
        
    def makePoints(self, n=20):
        '''Creates the points of the game that the player character is collecting.
        Paramaters:
        n -- the number of point objects being created.'''
        
        list1=[]
        for i in range(n):
            pellet = turtle.Turtle()
            pellet.shape('square')
            pellet.color("green") 
            pellet.penup()
            self.placeEnemyRandomly(pellet)
            list1.append(pellet)
        return(list1)
    
    def villains(self, n=10):
        '''Creates the villains of the game that the player object is avoiding
        Paramaters: 
        n -- The amount of villains being created.'''
        
        list2=[]
        for i in range(n):
            villain = turtle.Turtle()
            villain.shape('square')
            villain.color("Dark Green") 
            villain.penup()
            self.placeEnemyRandomly(villain)
            list2.append(villain) 
        return(list2)
    
    def placeEnemyRandomly(self, turt):
        '''Moves the points and enemies to random positions on the screen.
        Paramaters:
        turt -- the turtle object that will be moved to a random position.'''
        
        turt.goto(random.randint(-310, 350), random.randint(-310, 350))
    
    def moveEnemiesRandomly(self):
        '''Constantly moves the points and villain objects in random positions on the screen.'''
        
        #Points
        for i in (self.aliend):
            x, y = i.pos()
            i.goto(x+random.randint(-10, 10), y+random.randint(-10, 10))
        self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.update()
        
        #Villains.
        for i in (self.bully):
            x, y = i.pos()
            i.goto(x+random.randint(-10, 10), y+random.randint(-10, 10))
        self.screen.ontimer(self.moveVillainsRandomly, 50)
        self.screen.update()
            
    def checkForCollisions(self):  
        '''Checks to see if the player character collides with either points or villains. If the character 
        collides with points, it will add to the score. If the player collides with an enemie, it will bring
        them to the end screen.
        Paramaters:'''
        
        #Light Green.
        for i in (self.aliend):
            if self.player.distance(i) <= self.collision_radius:
                self.turt4.goto(0, 0)
                self.turt4.clear()
                self.score += 1
                self.turt4.write(self.score, True, 'left', ("arial", 60, "normal"))  
                print(self.score)
                self.placeEnemyRandomly(i)
                self.screen.update()
                print("BOOM!")
                
        #Dark Green
        for i in (self.bully):
            if self.player.distance(i) <= self.collision_radius:
                self.screen.clear()
                e = End()
                e.start()
                print("BOOM!")   
        self.screen.ontimer(self.checkForCollisions, 5)
        self.screen.update()
        
    def setupEvents(self):
        '''Creates the key press events for the game screen.
        Paramaters:'''
        
        self.screen.onkeypress(self.moveUp, 'Up')
        self.screen.onkeypress(self.moveDown, 'Down')
        self.screen.onkeypress(self.moveLeft, 'Left')
        self.screen.onkeypress(self.moveRight, 'Right')
        self.screen.onkeypress(self.screen.bye, 'space')
        self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.ontimer(self.checkForCollisions, 5)
      
    def moveUp(self):
        '''Moves the character forward.
        Paramaters:'''
        
        self.player.forward(self.speed)
        self.screen.update()
        
    def moveDown(self):
        '''Moves the character down on the screen.
        Paramaters:'''
        
        self.player.backward(self.speed)
        self.screen.update()
        
    def moveLeft(self):
        '''Moves the character left on the screen.
        Paramaters:'''
        
        currentangle = self.player.heading()
        newangleLeft = (360 - currentangle) % 360
        self.player.left(self.turnRate)
        self.player.shape(os.path.join('Images', f'Rocketship{int(newangleLeft)}.gif'))
        self.screen.update()
        
    def moveRight(self):
        '''Moves the character right on the screen.
        Paramaters:'''
        
        currentangle = self.player.heading()
        newangleRight = (360 - currentangle) % 360
        self.player.right(self.turnRate)
        self.player.shape(os.path.join('Images', f'Rocketship{int(newangleRight)}.gif'))
        self.screen.update()

if __name__ == '__main__':
    b = Begin()
    b.start()
""" import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QAction, QMenuBar, QDialog

class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        label = QLabel("This is the second window",self)
        layout.addWidget(label)
        self.setLayout(layout)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Example")
        self.setGeometry(100,100,400,300)

        self.central_widget=QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout=QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.Label=QLabel("Hello,PyQt!",self)
        self.layout.addWidget(self.Label)

        self.button=QPushButton("clickMe",self)
        self.layout.addWidget(self.button)

        self.init__menu()

    def init__menu(self):
        menubar=self.menuBar()
        file_menu=menubar.addMenu("File")
        exit_action=QAction("Exit",self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        view_menu=menubar.addMenu("view")
        second_Window_action=QAction("open Second Window",self)
        second_Window_action.triggered.connect(self.open_second_window)
        view_menu.addAction(second_Window_action)
    
    def open_second_window(self):
        self.second_window=SecondWindow()
        self.second_window.exec_()

app=QApplication(sys.argv)
window=MyWindow()
window.show()
sys.exit(app.exec_())


 """
#bs4
""" import requests 
from bs4 import BeautifulSoup
url="https://www.google.com"
resonse=requests.get(url)
soup=BeautifulSoup(resonse.content,"html.parser")
article_titles=soup.find_all("div")
for title in article_titles:
    print(title.get_text())
 """
#image showing
""" import pygame
pygame.init()
white=(255,255,255)
height=400
width=400
display_surface=pygame.display.set_mode((height,width))
pygame.display.set_caption('Image')
image=pygame.image.load(r'panda.jpg')
while True:
    display_surface.fill(white)
    display_surface.blit(image,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()"""

import pygame
import random

# Define some colors
BLACK = (0, 255, 0)
WHITE = (255, 255, 255)
color=[0,0,255]
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BALL_SIZE = 20

# Define the starting color and the increment for each new ball
START_COLOR = (0, 0, 0)


class Ball:
    """
    Class to keep track of a ball's location, vector, and color.
    """
    def __init__(self,c):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.color=c
        

            

def make_ball(ball_list,c):
    """
    Function to make a new ball with a color.
    """
    # Calculate the color for the new ball based on the current number of balls
    num_balls = len(ball_list)
    """ color = tuple(min(255, START_COLOR[i] + num_balls * COLOR_INCREMENT[i]) for i in range(3))
    print(color) """
    ball = Ball(c)
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    # Speed and direction of rectangle
    ball.change_x = 5
    ball.change_y = 5

    return ball

def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Bouncing Balls")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []

    # Create the initial ball
    ball = make_ball(ball_list,color)
    ball_list.append(ball)

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if color[0]<245:
                    color[0]+=10
                elif color[2]<245:
                    color[2]+=10
                elif color[1]<245:
                    color[1]+=10
                else:
                    color[0]=0
                    color[1]=0
                    color[2]=0
                if event.key == pygame.K_SPACE:
                    ball = make_ball(ball_list,color)
                    ball_list.append(ball)

        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        # --- Drawing
        # Set the screen background
        screen.fill(WHITE)

        



        # Draw the balls with their respective colors
        for ball in ball_list:
          
            pygame.draw.circle(screen, color, [ball.x, ball.y], BALL_SIZE)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(200)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()

       

    
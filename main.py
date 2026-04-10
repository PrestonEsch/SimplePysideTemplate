from gui import GUI
from logic import *
# NOTE: Importing the * means import all | Delete this message after you understand it

gui = GUI()

# Put your variables n stuff here
# Delete the logic file if you're not going to use it, it can look sloppy
# Keep most logic stuff in there (Like functions to update a shopping cart), and you can keep UI changes out here

# Don't forget to bind your buttons with gui.ui.<BUTTON NAME>.clicked.connect(<FUNCTION NAME>)


#
# From this point on, it's example code to look at then delete
#
score = 0

def updateScore():
    global score
    score = addOneRandomScore(score)

    gui.ui.scoreLabel.setText(f"Score: {score}")


gui.ui.addScoreButton.clicked.connect(updateScore)

#
# END OF EXAMPLE CODE
#


if __name__ == '__main__':
    gui.start()
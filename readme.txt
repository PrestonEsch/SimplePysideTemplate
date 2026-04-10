Guide on what to do from the start:

1. Download it

2. Open it in Pycharm
    - Hit the 4 lines
    - Click 'file'
    - Hit 'Open'
    - Open the code (You have to extract the zip first)

3. Create the virtual environment 
    - Once eyou have the folder opened, go back the the 'file' tab
    - Click settings
    - Click 'Project: SimplePysideTemplate'
    - Click 'Python Interpreter'
    - Then click 'Add interpreter' on the top right, and add existing/from local
    - WHen the window pops up, make sure the environment is New, and not not existing 
    - click 'ok' in the bottom right
    - click apply
    - Close the settings

4. Install pyside6
    - In the terminal, enter the line 'pip install pyside6'
    - You'll know it worked when you look into the folder .venv/Scripts/ and you see pyside6 stuff

5. Add correct run commands
    - In the top right, you should see some thing says 'current file'
    - Click that and click 'Edit Configurations'
    - Click plus icon in the top left, and then click 'python'
    - On the section in the right, name it 'Main'
    - For the empty space the right of where it says 'script', type main.py

    - Do the same thing again, except instead of adding 'Main' and 'main.py', add 'Compile UI' and 'compile_ui.py'

6. Should be set from here
    - To change between compiling all of your UI files and running main, click on the button to the left of the run arrow 

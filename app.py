from flask import Flask
app = Flask(__name__)

myText1 = "__________\n"
myText2 = "|         |\n"
myText3 = "|  0   0  |\n"
myText4 = "|         |\n"
myText5 = "|  (===)  |\n"
myText6 = "|_________|\n"
myText7 = "BEEP BOOP"

@app.route('/')
def hello_world():
    print(myText1)
    print(myText2)
    print(myText3)
    print(myText4)
    print(myText5)
    print(myText6)
    return myText7

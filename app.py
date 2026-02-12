from flask import Flask
app = Flask(__name__)

myText1 = "__________\n"
myText2 = "|         |\n"
myText3 = "|  0   0  |\n"
myText4 = "|         |\n"
myText5 = "|  (===)  |\n"
myText6 = "|_________|\n"
myText7 = "BEEP BOOP"

myTextFinal = myText1+myText2+myText3+myText4+myText5+myText6+myText7

@app.route('/')
def hello_world():
    return 

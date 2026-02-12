from flask import Flask
app = Flask(__name__)

myText1 = "__________<br>"
myText2 = "|         |<br>"
myText3 = "|  0   0  |<br>"
myText4 = "|         |<br>"
myText5 = "|  (===)  |<br>"
myText6 = "|_________|<br>"
myText7 = "BEEP BOOP"

myTextFinal = myText1+myText2+myText3+myText4+myText5+myText6+myText7
@app.route('/')
def hello_world():
    return myTextFinal

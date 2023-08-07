from flask import Flask,request,render_template,jsonify
import json

# Creating a object for flask to store the module which __main__ which will store inside the __name__,
# so if we are running it in standalone mode then we need to store this special varaible into the object
# so here we are creating a object of the class name and the class name is Flask
obj=Flask(__name__)

@obj.route('/') # this is default url
def welcome():
    return "Welcome to The Flask"


# To build calculator
@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']
    if operation=='add':
        result=int(number1)+int(number2)
    elif operation=='multiply':
        result=int(number1)*int(number2)
    elif operation=='division':
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return jsonify(result)
    



# Beacuse we are running a stand alone file so we need to write a condition
if __name__=='__main__':
    # by default flask will take the 5000 port but if we want to mention a particulat port we can mention in below 
    # Ex: obj.run(port=8000)
    obj.run(debug=True)



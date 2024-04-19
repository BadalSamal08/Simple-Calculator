from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return "This is the Home Page"

@app.route('/via_postman',  methods=['POST'])
def calculator():
    if request.method== 'POST':
        data = request.get_json()
        print(data)
        # data=data.json()
        num2 = data.get('num2')
        num1 = data.get('num1')
        # print(num2)
        # print(data['operation'])
        operation = data.get('operation')
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return "Invalid input: num1 and num2 must be integers"
        # # print(num2)
        # operation=request.json(['operation'])
        # print(operation)
        # num1=int(request.json['num1'])
        # num2=int(request.json['num2'])
        if operation == 'add':
            r = int(num1)+int(num2)
            result='The sum of ' + str(num1) + 'and ' + str(num2) + 'is' + str(r)
        if operation == 'subtract':
            r = num1-num2
            result='The subtraction of' + str(num1) + 'and ' + str(num2) + 'is' + str(r)
        if operation == 'mul':
            r = num1*num2
            result='The multiplication  of' + str(num1) + 'and ' + str(num2) + 'is' + str(r)
        if operation == 'division':
            r = num1/num2
            result='The division of' + str(num1) + 'and ' + str(num2) + 'is' + str(r)
        return result

if __name__ == '__main__' :
    app.run(debug=True)

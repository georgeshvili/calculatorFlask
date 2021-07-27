from flask import Flask, render_template, request

app = Flask(__name__)
# client = app.test_client()

@app.route('/', methods=['GET'])
def main():
    return render_template('calculator.html')

@app.route('/result', methods=['POST'])
def result():

    try:
        x = float(request.form['input1'])
        y = float(request.form['input2'])
        operation = request.form['operation']

        if operation == '+':
            result = x + y

        elif operation == '-':
            result = x - y

        elif operation == '*':
            result = x * y

        elif operation == '/':
            result = x / y

        else:
            result = x % y

        return render_template('calculator.html',
                               x=x,
                               y=y,
                               operation=operation,
                               result=result,
                               calculation_success=True
                               )

    except ZeroDivisionError:
        return render_template('calculator.html',
                               calculation_success=False,
                               error="Error, you can't divide by y = 0"
                               )

    except ValueError:
        return render_template('calculator.html',
                               calculation_success=False,
                               error="Error, it's calculator, so fill it with numbers"
                               )

if __name__=='__main__':
    app.run()
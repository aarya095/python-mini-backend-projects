# Third Party Modules
from flask import Flask

# Local Modules
from calculator.add import Add
from calculator.subtract import Subtract
from calculator.multiply import Multiply
from calculator.divide import Divide
from engine.calculator_engine import CalculatorEngine
from utils import get_and_validate_user_input as get_and_validate

app = Flask(__name__)
engine = CalculatorEngine()

@app.route('/home')
def index():
    return "Hello World!"

@app.route('/add/<int:num_1>/<int:num_2>')
def add(num_1, num_2):
    result = engine.execute_operation(Add(num_1, num_2))
    return str(result)

@app.route('/sub/<int:num_1>/<int:num_2>')
def subtract(num_1, num_2):
    result = engine.execute_operation(Subtract(num_1, num_2))
    return str(result)

@app.route('/mul/<int:num_1>/<int:num_2>')
def multiply(num_1, num_2):
    result = engine.execute_operation(Multiply(num_1, num_2))
    return str(result)

@app.route('/div/<int:num_1>/<int:num_2>')
def divide(num_1, num_2):
    result = engine.execute_operation(Divide(num_1, num_2))
    return str(result)
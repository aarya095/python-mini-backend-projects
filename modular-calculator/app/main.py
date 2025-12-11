from calculator.add import Add
from engine.calculator_engine import CalculatorEngine

engine = CalculatorEngine()
result = engine.execute_operation(Add(2,4))
print(result)
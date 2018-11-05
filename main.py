
from graphbuilder import GraphBuilder

#TO_DO
# 1. Fix graph view
# 2. Fix

# TESTING PART

input_temp = [1, 1, 1, 3, 0.01]
builder = GraphBuilder()
builder.build(input_temp)


# from flask import Flask, render_template, request
# app = Flask(__name__)
#
# @app.route('/')
# def start():
#     return render_template('index.html')
#
# @app.route('/result', methods = ['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         dictionary =  request.form
#
#         input - [x_initial, y_initial, diapazone_start, diapazone_end, h]
#         input = [dictionary['x_initial'],dictionary['y_initial'],dictionary['diapazone_start'],dictionary['diapazone_end'],dictionary['h']]
#
#         for i in range(len(input)):
#             temp = float(input[i])
#             input[i] = temp
#
#         builder = Graph_builder()
#         builder.build(input)
#
#         # # output = [[] for k in range(3)]
#         # methods = Methods()
#         # graphs = Graph_builder()
#         # methods.euler_method(input)
#
#         return render_template("result.html", result = input)
#     else:
#         return render_template("result.html")
#
# if __name__ == '__main__':
#     app.run(debug=True)

from graph_builder import Graph_builder

#TO_DO
# 1. Solve and check the result
# 2. Add some functions and restruct to OOP requirements
# 3. Add graph drawing
# 4. Submit to Github
# 5. Add comments
# Optional: 6. Add graphical interface
#

# TESTING PART

input_temp = [1, 1, 1, 3, 0.01]
builder = Graph_builder()
builder.set_inf(input_temp)
builder.build('methods',input_temp)


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
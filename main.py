import math
from matplotlib import pyplot as pylab
# import pylab

#TO_DO
# 1. Solve and check the result
# 2. Add some functions and restruct to OOP requirements
# 3. Add graph drawing
# 4. Submit to Github
# 5. Add comments
# Optional: 6. Add graphical interface
#

class Graph_builder:

    def __init__(self):
        self.x_common = []
        self.y_exact = []
        self.y_euler = []
        self.y_imp_euler = []
        self.y_fk = []
        self.diff_exact_euler = []
        self.diff_exact_imp_euler = []
        self.diff_exact_rk = []

    def get_points(self, arg, input_parameters):
        methods = Methods()
        if arg == 'exact':
            self.x_common = methods.exact_solution(input_parameters)[0]
            self.y_exact = methods.exact_solution(input_parameters)[1]
        if arg == 'euler':
            self.y_euler = methods.euler_method(input_parameters)[1]
        if arg == 'euler_imp':
            self.y_imp_euler = methods.improved_euler_method(input_parameters)[1]
        if arg == 'rk':
            self.y_fk = methods.runge_kutta_method(input_parameters)[1]

    def set_inf(self, input_parameters):
        self.get_points('exact', input_parameters)
        self.get_points('euler', input_parameters)
        self.get_points('euler_imp', input_parameters)
        self.get_points('rk', input_parameters)

        for i in range(len(self.y_exact)):
            self.diff_exact_euler.append(abs(self.y_exact[i] - self.y_euler[i]))
            self.diff_exact_imp_euler.append(abs(self.y_exact[i] - self.y_imp_euler[i]))
            self.diff_exact_rk.append(abs(self.y_exact[i] - self.y_fk[i]))

    def build(self,  input_parameters, show=False):
        num_operations_temp = NumericOperations()

        # Values for each line of graph, describing how all of them will look like, define markers
        pylab.subplot(211)
        exact_line, euler_line, imp_euler_line, fk_line = pylab.plot(self.x_common, self.y_exact, 'm-',self.x_common, self.y_euler, 'b-', self.x_common, self.y_imp_euler, 'g-', self.x_common,
                                                             self.y_fk, 'c-')
        # X and Y axis intervals
        pylab.title(u'Numeric methods solution of differential equation')
        pylab.xlabel(u'x axis')
        pylab.ylabel(u'y axis')

        pylab.legend((exact_line,euler_line, imp_euler_line, fk_line),
                         (u'Exact Solution' ,u'Euler Method ', u'Improved Euler Method ', u'Runge-Kutta Method'), loc='best')
        pylab.grid()


        pylab.subplot(212)
        err_euler_line, err_imp_euler_line, err_fk_line = pylab.plot(self.x_common, self.diff_exact_euler, 'm-',
                                                                     self.x_common, self.diff_exact_imp_euler,
                                                                     'b-', self.x_common, self.diff_exact_rk, 'g-')
        pylab.title(u'Approximation error of numeric methods solution of differential equation')
        pylab.xlabel(u'x axis')
        pylab.ylabel(u'y axis')
        pylab.legend((err_euler_line, err_imp_euler_line, err_fk_line),
                     (u'Euler Method ', u'Improved Euler Method ', u'Runge-Kutta Method'),
                     loc='best')
        pylab.grid()
        pylab.show()

        # Сохраняем построенную диаграмму в файл
        # Задаем имя файла и его тип
        pylab.savefig('./static/graphs.png', format='png')
        # if show:
        #     pylab.show()

class NumericOperations:

    def find_value(self, arg, list):
        value = 0
        for k in range(len(list)):
            for i in list[k]:
                if arg == 'max':
                    if (value >= i):
                        value = i
                if arg == 'min':
                    if (value <= i):
                        value = i
        return value

class Methods:

    # my equation is 13th:
    # change it little bit, cause "math" in Python doesn't have a ctg function, but ctg = 1/tg so ...

    def get_value(self, x, y):
        return math.sin(x)**2 + y / math.tan(x)


    def get_const(self, x0, y0):
        return  (y0 + math.sin(x0)*math.cos(x0))/math.sin(x0)

    def exact_solution(self, input):
        # input - [x_initial, y_initial, diapazone_start, diapazone_end, h]
        x0 = input[0]
        y0 = input[1]
        h = input[4]
        pointer = input[2]

        table_x = []
        table_y = []

        const = self.get_const(x0, y0)

        while (pointer <= input[3]):
            if not table_x:
                table_x.append(input[0])
                table_y.append(input[1])
            else:
                x_i = table_x[len(table_x) - 1]

                # general sol is y = sin(x) * C - sin(x) * cos(x)
                x_next = x_i + h
                y_next = math.sin(x_next)*const - math.sin(x_next)*math.cos(x_next)


                table_x.append(x_next)
                table_y.append(y_next)
                pointer += h

        table = [table_x, table_y]
        return table


    def euler_method(self, input):
        table_x = []
        table_y = []
        h = input[4]
        pointer = input[2]
        while (pointer <= input[3]):
            if not table_x:
                table_x.append(input[0])
                table_y.append(input[1])
            else:
                x_i = table_x[len(table_x) - 1]
                y_i = table_y[len(table_y) - 1]

                x_next = x_i + h
                y_next = y_i + h * self.get_value(x_i, y_i)

                table_x.append(x_next)
                table_y.append(y_next)
                pointer += h
        table = [table_x,table_y]
        return table


    def improved_euler_method(self, input):
        table_x = []
        table_y = []
        h = input[4]
        pointer = input[2]
        while (pointer <= input[3]):
            if not table_x:
                table_x.append(input[0])
                table_y.append(input[1])
            else:
                x_i = table_x[len(table_x) - 1]
                y_i = table_y[len(table_y) - 1]
                delta_y = h * self.get_value(x_i + h / 2, y_i + h / 2 * self.get_value(x_i, y_i))

                x_next = x_i + h
                y_next = y_i + delta_y

                table_x.append(x_next)
                table_y.append(y_next)
                pointer += h
        table = [table_x, table_y]
        return table


    def runge_kutta_method(self, input):
        table_x = []
        table_y = []
        h = input[4]
        pointer = input[2]
        while (pointer <= input[3]):
            if not table_x:
                table_x.append(input[0])
                table_y.append(input[1])
            else:
                x_i = table_x[len(table_x) - 1]
                y_i = table_y[len(table_y) - 1]
                k1 = self.get_value( x_i, y_i)
                k2 = self.get_value( x_i + h / 2, y_i + h * k1 / 2)
                k3 = self.get_value( x_i + h / 2, y_i + h * k2 / 2)
                k4 = self.get_value( x_i + h, y_i + h * k3)
                delta_y = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

                x_next = x_i + h
                y_next = y_i + delta_y

                table_x.append(x_next)
                table_y.append(y_next)
                pointer += h
        table = [table_x, table_y]
        return table


# input - [x_initial, y_initial, diapazone_start, diapazone_end, h]
# methods = Methods()

# input - [x_initial, y_initial, diapazone_start, diapazone_end, h]

# TESTING PART

input_temp = [1, 1, 1, 3, 0.01]
builder = Graph_builder()

# builder.build('methods_graph', input_temp)
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
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
    # input_temp = [1, 1, 1, 3, 0.01]

    def get_points(self, arg, input_parameters ):
        methods = Methods()
        if arg == 'euler':
            out = methods.euler_method(input_parameters)
        if arg == 'euler_imp':
            out = methods.improved_euler_method(input_parameters)
        if arg == 'rk':
            out = methods.runge_kutta_method(input_parameters)
        return out

    def build(self, what,  input_parameters, show=False):
        output_temp = [[] for k in range(3)]
        num_operations_temp = NumericOperations()
        output_temp[0] = self.get_points('euler', input_parameters)
        output_temp[1] = self.get_points('euler_imp', input_parameters)
        output_temp[2] = self.get_points('rk', input_parameters)

        x_common = output_temp[0][0]
        y_euler = output_temp[0][1]
        y_imp_euler = output_temp[1][1]
        y_fk = output_temp[2][1]

        # Values for each line of graph, describing how all of them will look like, define markers
        euler_line, imp_euler_line, fk_line = pylab.plot(x_common, y_euler, 'b-', x_common, y_imp_euler, 'g-', x_common,
                                                         y_fk, 'm-')

        # X and Y axis intervals
        # input - [x_initial, y_initial, diapazone_start, diapazone_end, h]
        x_start = input_parameters[2] - 2
        x_finish = input_parameters[3] + 2
        y_start = int(num_operations_temp.find_value(min, [y_euler, y_imp_euler, y_fk])) + 0.5
        y_finish = int(num_operations_temp.find_value(max, [y_euler, y_imp_euler, y_fk])) + 2

        pylab.axis([x_start, x_finish, y_start, y_finish], 'tight')

        pylab.title(u'Numeric methods solution of differential equation')
        pylab.xlabel(u'x axis')
        pylab.ylabel(u'y axis')

        pylab.legend((euler_line, imp_euler_line, fk_line),
                     (u'Euler Method ', u'Improved Euler Method ', u'Runge-Kutta Method'), loc='best')

        # Включаем сетку

        pylab.grid()
        # Сохраняем построенную диаграмму в файл
        # Задаем имя файла и его тип
        pylab.savefig('./static/' + what + '.png', format='png')
        if show:
            pylab.show()

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


# output = [[] for k in range(3)]
# methods = Methods()

# output[n]- n - table of the values created by method
# ------------------------------------------------------------------------------------
# indexes
# n [0] - Euler Method
# n [1] - Improved Euler Method
# n [2] - Runge-Kutta Method
# ------------------------------------------------------------------------------------
# input - [x_initial, y_initial, diapazone_start, diapazone_end, h]

# input = [1, 1, 1, 3]

# ---------------
# first equation
# ----------------
# methods.euler_method(output[0], input)
# methods.improved_euler_method(output[1], input)
# methods.runge_kutta_method(output[2], input)
#
#
# for i in result[0]:
#     print("{0:.2f}, {0:.2f}".format(*i))
#     # print(f"({# i[0]},{i[1]})")
#     # print("(" + str(i[0]) + ";" + str(i[1]) +")")

# input_temp = [1, 1, 1, 3, 0.01]
# builder = Graph_builder()
#
# builder.build('methods_graph', input_temp)

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        dictionary =  request.form

        input = [dictionary['x_initial'],dictionary['y_initial'],dictionary['diapazone_start'],dictionary['diapazone_end'],dictionary['h']]

        for i in range(len(input)):
            temp = float(input[i])
            input[i] = temp

        builder = Graph_builder()
        builder.build('methods_graph', input)

        # # output = [[] for k in range(3)]
        # methods = Methods()
        # graphs = Graph_builder()
        # methods.euler_method(input)

        return render_template("result.html", result = input)
    else:
        return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
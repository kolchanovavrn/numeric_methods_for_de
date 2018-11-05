import math


class NumericOperations:
    # Needed for defining the borders of graph. Mostly for defining the border of Y axis

    # Returns max/min value from given list of different list of values
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

    # Returns the value of function dy/dx = sin(x)^2 + y * ctg(x)
    def get_value(self, x, y):
        return math.sin(x) ** 2 + y / math.tan(x)

    # Returns the value of Constant. Necessary for exact solution
    def get_const(self, x0, y0):
        return (y0 + math.sin(x0) * math.cos(x0)) / math.sin(x0)

    def set_x(self, input, table_x):
        x0 = input[0]
        X = input[2]
        h = abs((x0 - X)/input[3])

        curr = x0
        while curr <= X:
            table_x.append(curr)
            curr+=h


    # Returns the value of Y by founded exact solution
    def exact_solution(self, input, table_x, table_y):
        # input format - [x_initial, y_initial, diapazone_end, h]

        x0 = table_x[0]
        y0 = input[1]

        const = self.get_const(x0, y0)

        for i in table_x:
            y_curr = math.sin(i) * const - math.sin(i) * math.cos(i)
            table_y.append(y_curr)


    # Retuns the value of Y by Euler Method
    def euler_method(self, input, table_x, table_y):
        x0 = input[0]
        X = input[2]
        h = abs((x0 - X)/input[3])
        y0 = input[1]


        if not table_y:
            table_y.append(y0)

        index = 1
        while index < len(table_x):
            x_prev = table_x[index-1]
            y_prev = table_y[index-1]
            table_y.append(y_prev + h * self.get_value(x_prev, y_prev))
            index+=1

    # Returns the value of Y by Improved Euler Method
    def improved_euler_method(self, input, table_x, table_y):
        x0 = input[0]
        X = input[2]
        h = abs((x0 - X)/input[3])
        y0 = input[1]


        if not table_y:
            table_y.append(y0)

        index = 1
        while index < len(table_x):
            x_prev = table_x[index-1]
            y_prev = table_y[index-1]

            delta_y = h * self.get_value(x_prev + h / 2, y_prev + h / 2 * self.get_value(x_prev, y_prev))
            table_y.append(y_prev + delta_y)
            index+=1

    # Returns the value of Y by Runge Kutta Method
    def runge_kutta_method(self, input,table_x,  table_y):

        x0 = input[0]
        X = input[2]
        h = abs((x0 - X)/input[3])
        y0 = input[1]


        if not table_y:
            table_y.append(y0)

        index = 1
        while index < len(table_x):
            x_prev = table_x[index-1]
            y_prev = table_y[index-1]

            k1 = self.get_value(x_prev, y_prev)
            k2 = self.get_value(x_prev + h / 2, y_prev + h * k1 / 2)
            k3 = self.get_value(x_prev + h / 2, y_prev + h * k2 / 2)
            k4 = self.get_value(x_prev + h, y_prev + h * k3)
            delta_y = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            table_y.append(y_prev+delta_y)
            index += 1
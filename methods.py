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

    # Returns the value of Y by founded exact solution
    def exact_solution(self, input, table_x, table_y):
        # input format - [x_initial, y_initial, diapazone_start, diapazone_end, h]
        x0 = input[0]
        y0 = input[1]
        h = input[4]
        pointer = input[2]

        const = self.get_const(x0, y0)

        while (pointer <= input[3]):
            if not table_y:
                table_x.append(input[0])
                table_y.append(input[1])
            else:
                x_i = table_x[len(table_x) - 1]

                # general sol is y = sin(x) * C - sin(x) * cos(x)
                x_next = x_i + h
                y_next = math.sin(x_next) * const - math.sin(x_next) * math.cos(x_next)

                table_x.append(x_next)
                table_y.append(y_next)
                pointer += h

    # Retuns the value of Y by Euler Method
    def euler_method(self, input, table_y):
        table_x = []
        h = input[4]
        pointer = input[2]
        while (pointer <= input[3]):
            if not table_y:
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

    # Returns the value of Y by Improved Euler Method
    def improved_euler_method(self, input, table_y):

        table_x = []

        h = input[4]
        pointer = input[2]
        while (pointer <= input[3]):
            if not table_y:
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

    # Returns the value of Y by Runge Kutta Method
    def runge_kutta_method(self, input, table_y):
        table_x = []
        h = input[4]
        pointer = input[2]
        while (pointer <= input[3]):
            if not table_y:
                table_x.append(input[0])
                table_y.append(input[1])
            else:
                x_i = table_x[len(table_x) - 1]
                y_i = table_y[len(table_y) - 1]
                k1 = self.get_value(x_i, y_i)
                k2 = self.get_value(x_i + h / 2, y_i + h * k1 / 2)
                k3 = self.get_value(x_i + h / 2, y_i + h * k2 / 2)
                k4 = self.get_value(x_i + h, y_i + h * k3)
                delta_y = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

                x_next = x_i + h
                y_next = y_i + delta_y

                table_x.append(x_next)
                table_y.append(y_next)
                pointer += h

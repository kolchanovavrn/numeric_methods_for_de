from methods import Methods
class Errors:
    # Needed for defining the borders of graph. Mostly for defining the border of Y axis

    # Returns max/min value from given list of different list of values

    def find_max_val(self, array):
        max_val = array[0]
        for i in array:
            if i>=max_val:
                max_val = i
        return max_val

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

    def get_max_point(self, exact, method):
        diff_arr = []
        print('new')
        print(len(exact))
        print(len(method))

        for index in range(len(exact)):
            diff_arr.append(abs(exact[index] - method[index]))
        max_point = self.find_max_val(diff_arr)
        return max_point


    def local_error(self, result, method_1_table, method_2_table):
        for i in range(len(method_1_table)):
            result.append(abs(method_1_table[i] - method_2_table[i]))

    def max_error(self, input):

        N_start = input[4]
        N_end = input[5]

        x0 = input[0]
        X = input[2]

        n = N_start

        n_x = []
        n_euler = []
        n_euler_imp = []
        n_fk = []
        exact = []


        methods = Methods()
        while n <= N_end:
            n_x.append(n)
            h = abs(X - x0) / n
            input[3] = n

            exact = []
            euler_new_y = []
            euler_imp_new_y = []
            rk_new_y = []
            table_x = []

            table_x = methods.set_x(input, table_x)

            print("Iteration")
            print(n)

            print("len - Exact, euler, IE, RK ")
            exact = methods.exact_solution(input, table_x, exact)

            euler_new_y = methods.euler_method(input, table_x, euler_new_y)
            euler_imp_new_y = methods.improved_euler_method(input,table_x, euler_imp_new_y)
            rk_new_y = methods.runge_kutta_method(input,table_x, rk_new_y)
            print(len(exact))
            print(len(euler_new_y))
            print(len(euler_imp_new_y))
            print(len(rk_new_y))


            n_euler.append(self.get_max_point(exact,euler_new_y))
            n_euler_imp.append(self.get_max_point(exact, euler_imp_new_y))
            n_fk.append(self.get_max_point(exact, rk_new_y))
            n+=1
        return n_x, n_euler, n_euler_imp, n_fk

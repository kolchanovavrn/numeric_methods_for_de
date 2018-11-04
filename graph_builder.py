from matplotlib import pyplot as pylab
from methods import Methods

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
            methods.exact_solution(input_parameters, self.x_common, self.y_exact)
        if arg == 'euler':
            methods.euler_method(input_parameters, self.y_euler)
        if arg == 'euler_imp':
            methods.improved_euler_method(input_parameters, self.y_imp_euler)
        if arg == 'rk':
            methods.runge_kutta_method(input_parameters, self.y_fk)

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
        #num_operations_temp = NumericOperations()

        # Values for each line of graph, describing how all of them will look like, define markers
        pylab.subplot(211)
        exact_line, euler_line, imp_euler_line, fk_line = pylab.plot(self.x_common, self.y_exact, 'm-',self.x_common, self.y_euler, 'b-', self.x_common, self.y_imp_euler, 'g-', self.x_common, self.y_fk, 'c-')
        # X and Y axis intervals
        pylab.title(u'Numeric methods solution of differential equation')
        pylab.xlabel(u'x axis')
        pylab.ylabel(u'y axis')

        pylab.legend((exact_line,euler_line, imp_euler_line, fk_line),
                         (u'Exact Solution' ,u'Euler Method ', u'Improved Euler Method ', u'Runge-Kutta Method'), loc='best')
        pylab.grid()


        pylab.subplot(212)
        err_euler_line, err_imp_euler_line, err_fk_line = pylab.plot(self.x_common, self.diff_exact_euler, 'm-',self.x_common, self.diff_exact_imp_euler,'b-', self.x_common, self.diff_exact_rk, 'g-')
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

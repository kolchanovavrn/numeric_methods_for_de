from matplotlib import pyplot as pylab
from methods import Methods


class GraphBuilder:
    """Class that collects all necessary resources and builds the resulting graphs
    Uses an object of class Methods to get and set the values
    Uses an object of class Numeric operations to set borders of building graph area"""

    def __init__(self):
        # Initialization parameters necessary to build the graps

        # For graph of different methods
        self.x_common = []
        self.y_exact = []
        self.y_euler = []
        self.y_imp_euler = []
        self.y_fk = []

        # For graph of approximation error between numeric methods
        self.diff_exact_euler = []
        self.diff_exact_imp_euler = []
        self.diff_exact_rk = []

    def set_points(self, input_parameters):
        # Gets and sets all the values* to class parameters
        # Values - x and y for every methods and for error approximation

        methods = Methods()
        # ------------------------------------------------
        # Set values given by Numeric methods
        # ------------------------------------------------

        methods.set_x(input_parameters, self.x_common)

        methods.exact_solution(input_parameters, self.x_common, self.y_exact)
        methods.euler_method(input_parameters, self.x_common, self.y_euler)
        methods.improved_euler_method(input_parameters,self.x_common, self.y_imp_euler)
        methods.runge_kutta_method(input_parameters,self.x_common, self.y_fk)

        # ------------------------------------------------
        # Set values of Local approximation errors
        # ------------------------------------------------

        for i in range(len(self.y_exact)):
            self.diff_exact_euler.append(abs(self.y_exact[i] - self.y_euler[i]))
            self.diff_exact_imp_euler.append(abs(self.y_exact[i] - self.y_imp_euler[i]))
            self.diff_exact_rk.append(abs(self.y_exact[i] - self.y_fk[i]))



        print("X _ com = " + str(len(self.x_common)))
        print("Y exac " + str(len(self.y_exact)))
        print("Y euler " + str(len(self.y_euler)))
        print("Y imp euler "+ str(len(self.y_imp_euler)))
        print("Y FK" + str(len(self.y_fk)))

        print("E E " + str(len(self.diff_exact_euler)))
        print("E IE " + str(len(self.diff_exact_imp_euler)))
        print("E FK " + str(len(self.diff_exact_rk)))

    def build(self, input_parameters, show=False):
        # Main function for building the graph
        # Values for each line of graph, describing how all of them will look like, define markers

        # ------------------------------------------------
        # First - Graph of values given by Numeric methods
        # ------------------------------------------------

        self.set_points(input_parameters)

        pylab.rcParams['figure.figsize'] = (15.0, 20.0)
        pylab.subplots_adjust(hspace=0.5)
        pylab.subplot(211)
        exact_line, euler_line, imp_euler_line, fk_line = pylab.plot(self.x_common, self.y_exact, 'm-', self.x_common,
                                                                     self.y_euler, 'b-', self.x_common,
                                                                     self.y_imp_euler, 'g-', self.x_common, self.y_fk,
                                                                     'c-')
        pylab.title(u'Numeric methods solution of differential equation')
        pylab.xlabel(u'x axis')
        pylab.ylabel(u'y axis')

        pylab.legend((exact_line, euler_line, imp_euler_line, fk_line),
                     (u'Exact Solution', u'Euler Method ', u'Improved Euler Method ', u'Runge-Kutta Method'),
                     loc='best')
        pylab.grid()

        # ------------------------------------------------
        # Second - Graph of Local approximation error given by Numeric methods
        # ------------------------------------------------

        pylab.subplot(212)
        err_euler_line, err_imp_euler_line, err_fk_line = pylab.plot(self.x_common, self.diff_exact_euler, 'm-',
                                                                     self.x_common, self.diff_exact_imp_euler, 'b-',
                                                                     self.x_common, self.diff_exact_rk, 'g-')
        pylab.title(u'Approximation error of numeric methods solution of differential equation')
        pylab.xlabel(u'x axis')
        pylab.ylabel(u'y axis')
        pylab.legend((err_euler_line, err_imp_euler_line, err_fk_line),
                     (u'Euler Method ', u'Improved Euler Method ', u'Runge-Kutta Method'),
                     loc='best')

        #  figure.figsize и figure.dpi (свойства можно задать, разумеется и через структуру rcParams,
        pylab.grid()

        # Save the resulting image, that contain pictures of both graphs to the special directory
        pylab.savefig('./static/graphs.png', format='png')
        if show:
            pylab.show()

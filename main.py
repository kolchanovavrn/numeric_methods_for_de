from graphbuilder import GraphBuilder

# TO_DO
# 2. Fix

# # TESTING PART
#
# input_temp = [1, 1, 1, 3, 0.01]
# builder = GraphBuilder()
# builder.build(input_temp)


from flask import Flask, render_template, request

app = Flask(__name__)


@app.after_request
def no_cache(r):
    r.headers['Expires'] = 0
    r.headers['Cache-Control'] = 'must-revalidate, max-age=0, no-cache, no-store'
    return r


@app.route('/', methods=['POST', 'GET'])
def result():
    initial = True
    if request.method == 'POST':
        dictionary = request.form

        # input - [x_initial, y_initial, diapazone_start, diapazone_end, h]
        input = [dictionary['x_initial'], dictionary['y_initial'], dictionary['diapazone_start'],
                 dictionary['diapazone_end'], dictionary['h']]

        for i in range(len(input)):
            temp = float(input[i])
            input[i] = temp

        builder = GraphBuilder()
        builder.build(input)

        # # output = [[] for k in range(3)]
        # methods = Methods()
        # graphs = Graph_builder()
        # methods.euler_method(input)

        return render_template("index.html", result=input, show_image=True, x0=input[0], y0=input[1], start_x=input[2],
                               end_x=input[3], step_x=input[4])
    else:
        return render_template("index.html", show_image=False)
         # return render_template("index.html", show_image=False, x0=1, y0=1, start_x=1, end_x=3, step_x=0.01)


if __name__ == '__main__':
    app.run(debug=True)

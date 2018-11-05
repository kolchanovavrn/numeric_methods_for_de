from graphbuilder import GraphBuilder
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

        return render_template("index.html", result=input, show_image=True, x0=input[0], y0=input[1], start_x=input[2],
                               end_x=input[3], step_x=input[4])
    else:
        return render_template("index.html", show_image=False)


if __name__ == '__main__':
    app.run(debug=True)

from graphbuilder import GraphBuilder
from flask import Flask, render_template, request

# # TESTING PART
# input_temp = [1, 1,3, 200, 150, 200]
# builder = GraphBuilder()
# builder.build(input_temp)


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

        # input - [x_initial, y_initial, diapazone_end, N, N from , N to]
        input = [dictionary['x_initial'], dictionary['y_initial'],
                 dictionary['diapazone_end'], dictionary['h'], dictionary['N_start'], dictionary['N_end']]

        for i in range(len(input)):
            temp = float(input[i])
            input[i] = temp

        builder = GraphBuilder()
        builder.build(input)

        return render_template("index.html", result=input, show_image=True, x0=input[0], y0=input[1],
                               end_x=input[2], amount_x=input[3], n_start=input[4], n_end=input[5])
    else:
        return render_template("index.html", show_image=False)


if __name__ == '__main__':
    app.run(debug=True)

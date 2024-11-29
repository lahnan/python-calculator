from flask import Flask, render_template, request

app = Flask(__name__)

title = "Python Web Calculator (Calculator v2)"

t1 = "           _            _       _                     ____  "
t2 = "  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __  __   _|___ \ "
t3 = " / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__| \ \ / / __) |"
t4 = "| (_| (_| | | (__| |_| | | (_| | || (_) | |     \ V / / __/ "
t5 = " \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|      \_/ |_____|"

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

print (title)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        inp1 = int(request.form['inp1'])
        inp2 = int(request.form['inp2'])
        meth = (request.form['meth'])
        
        if meth == '+':
            answer = inp1 + inp2
            return render_template('index.html', answer=answer)
            print(answer)
        elif meth == '-':
            answer = inp1 - inp2
            return render_template('index.html', answer=answer)
        elif meth == '*':
            answer = inp1 * inp2
            return render_template('index.html', answer=answer)
        elif meth == '/':
            answer = inp1 / inp2
            return render_template('index.html', answer=answer)
        else:
            print('empty input')
        
        if inp1 == None:
            print('empty input')
        elif inp2 == None:
            print('empty input')
    return render_template('index.html', title=title)
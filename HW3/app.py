from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/Mabalot_HW3')
def home():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        sex = request.form['sex']
        institution = request.form['institution']
        email = request.form['email']

        return render_template(
            'output.html',
            lastname=lastname,
            firstname=firstname,
            sex=sex,
            institution=institution,
            email=email
        )
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
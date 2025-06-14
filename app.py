from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Citizen Voice on the Cloud!"

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        with open('feedback.txt', 'a') as f:
            f.write(f'Name: {name}\nMessage: {message}\n---\n')

        return "Thank you for your feedback!"
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



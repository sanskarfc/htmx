from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle')
def toggle_message():
    # Toggle the visibility of the message
    return "<p>This is a visible message.</p>"

if __name__ == '__main__':
    app.run(debug=True, port=8080)

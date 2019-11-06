from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/cases')
def cases():
    return render_template('cases.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/messenger')
def messenger():
    return render_template('messenger.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

if __name__ == '__main__':
   app.run()

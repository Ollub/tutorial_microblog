from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Oleg loves Jane so much!'
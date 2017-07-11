
import Flask 
from model import connect_to_db, db

app = Flask(__name__)


@app.route('/')
def render_home():

    return render_template('hhhomepage.html')


@app.route('/login'):
def render_login(): 

    

@app.route('/signin'):
def render_login():





if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)

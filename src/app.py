from flask import Flask,jsonify
import  datetime
import socket
app = Flask(__name__)

@app.route('/api/vq/details')

def details():
    return jsonify({
        'time' : datetime.datetime.now().strftime("%H:%M:%S"),
        'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'host': socket.gethostname(),
        'message': "You are the great, keep it up :))"
    })


@app.route('/api/vq/health')

def health():
    return jsonify({
        "status": "up!"
    }),200

# Add root route to handle '/'
@app.route('/')
def home():
    return "Welcome to the Python App API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)


#'/api/vq/details'
#'/api/vq/health'
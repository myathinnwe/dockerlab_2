import os
from flask import  Flask


port = int(os.environ.get('PORT' , 5000))

app = Flask(__name__)

@app.route('/')
def hello():
  return 'hello world, running on port {port}'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)

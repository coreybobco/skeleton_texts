from flask import Flask, request, render_template
import json
from skeleton import Skeleton_Class

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/generate", methods=['POST'])
def generate():
	request = json.decode(request.get_data())
	skeleton = request.skeleton 

if __name__ == '__main__':
  app.run(
      host="0.0.0.0",
      port=8080,
      debug=True
  )

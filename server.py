from flask import Flask, request, render_template
import json
from skeleton import Skeleton_Class

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/generate", methods=['POST'])
def generate():
	req_obj = json.loads(request.get_data().decode(encoding='UTF-8'))
	skeleton = req_obj['skeleton'] 
	files = req_obj['files']
	skeleton_toolkit = Skeleton_Class(skeleton, files)
	return skeleton_toolkit.generate()

if __name__ == '__main__':
  app.run(
      host="0.0.0.0",
      port=8080,
      debug=True
  )

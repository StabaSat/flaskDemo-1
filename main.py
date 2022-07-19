from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def base_page():
	return render_template(
		'home.html',  # Template file path, starting from the templates folder. 
	)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)


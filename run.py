from flask import *
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
main_url = "https://instagram.com/{}"

@app.route("/",methods=["POST","GET"])
def index():
	user = request.form.get("user")
	if request.method == "GET":
		return render_template("index.html")
	else:
		r = requests.get(main_url.format(user))
		b = bs(r.text, "html.parser")
		for f in b.findAll("meta"):
			if f.get("property") == "og:image":
				img = f.get("content")

		return render_template("sukses.html",user=user, img=img)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)

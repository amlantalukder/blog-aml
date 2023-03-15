from flask import Flask, render_template, request
import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    app.logger.info("Home page loaded.")
    return render_template("home.html")

@app.route("/login-register", methods=["GET"])
def loginOrReg():
    app.logger.info("Login page loaded.")
    return render_template("login-register.html")

@app.route("/load-blogs/<u_id>", methods=["POST"])
def loadBlogs(u_id):
    app.logger.info(f"Blog load request: {request}, user id: {u_id}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
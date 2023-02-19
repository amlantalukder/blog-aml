from flask import render_template
import uvicorn
import logger

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    logger.info("Home page loaded.")
    return render_template("index.html")


@app.route("/load-blogs/<u_id>", methods=["POST"])
def loadData(u_id):
    logger.info(f"Data load request: {request}, user id: {u_id}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

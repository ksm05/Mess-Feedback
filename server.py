from flask import Flask, render_template, jsonify, request
from shared_memory import create_shared_memory
from semaphore import mutex

app = Flask(__name__)
shm = create_shared_memory()

def read_counts():
    return {
        "good": int.from_bytes(shm.buf[0:4], 'little'),
        "average": int.from_bytes(shm.buf[4:8], 'little'),
        "poor": int.from_bytes(shm.buf[8:12], 'little')
    }

def update_count(feedback):
    mutex.acquire()
    try:
        if feedback == "good":
            shm.buf[0:4] = (read_counts()["good"] + 1).to_bytes(4, 'little')
        elif feedback == "average":
            shm.buf[4:8] = (read_counts()["average"] + 1).to_bytes(4, 'little')
        elif feedback == "poor":
            shm.buf[8:12] = (read_counts()["poor"] + 1).to_bytes(4, 'little')
    finally:
        mutex.release()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    update_count(data["type"])
    return jsonify(read_counts())

@app.route("/counts")
def counts():
    return jsonify(read_counts())

if __name__ == "__main__":
    app.run(debug=True)

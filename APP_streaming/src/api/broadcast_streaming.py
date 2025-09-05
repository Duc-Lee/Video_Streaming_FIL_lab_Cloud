from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/get_stream_info", methods=["GET"])
def get_stream_info():
    return jsonify({
        "ip": "239.0.0.1",
        "port": 1234,
        "protocol": "udp",
        "url": "udp://239.0.0.1:1234"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



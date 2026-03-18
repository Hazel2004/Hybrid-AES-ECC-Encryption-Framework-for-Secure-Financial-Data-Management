from flask import Flask, request, jsonify
from routes.upload import encrypt_and_store
from routes.download import decrypt_and_load

app = Flask(__name__)

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")




# Upload API
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    file_path = f"test_files/{file.filename}"
    file.save(file_path)

    key = encrypt_and_store(file_path)

    return jsonify({
        "message": "File encrypted successfully",
        "aes_key": key   # send key to frontend
    })


@app.route("/download", methods=["POST"])
def download():
    result = decrypt_and_load()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
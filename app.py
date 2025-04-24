from flask import Flask, render_template, request
import csv
import io
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = []
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith('.csv'):
            # Tenta decodificar com UTF-8
            try:
                stream = io.StringIO(file.stream.read().decode("utf-8"))
            except UnicodeDecodeError:
                stream = io.StringIO(file.stream.read().decode("latin1"))
            reader = csv.reader(stream)
            data = list(reader)
    return render_template("index.html", data=data, year=datetime.datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

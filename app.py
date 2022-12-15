from flask import Flask
from python_filesystem.filesystem import FileSystem, DELIMITER
from python_filesystem.filesystem import BinaryFile, LogFile, BufferFile


fs = FileSystem()
app = Flask(__name__)
app.config["FILESYSTEM_OBJ"] = fs


@app.route("/", methods=["GET", "PUT", "DELETE"])
def index():
    pass


@app.route("/directory", methods=["POST"])
def directory():
    pass


@app.route("/binaryfile", methods=["GET", "POST"])
def binaryfile():
    pass


@app.route("/logtextfile", methods=["GET", "POST", "PUT"])
def logtextfile():
    pass


@app.route("/bufferfile", methods=["GET", "PUT", "POST"])
def bufferfile():
    pass


if __name__ == "__main__":
    app.run(debug=True)

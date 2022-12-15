from flask import Flask
from python_filesystem.filesystem import FileSystem

fs = FileSystem()
app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
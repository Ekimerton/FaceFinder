from flask import Flask
app = Flask(__name__)

@app.route("/")

def main():
    print("Hello Lasagna")

main()

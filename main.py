from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>My Portfolio (w/ Flask)</title>
        <style>
            body {
                font-family: Serif, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #B6B6B6;
                color: #333;
                text-align: center;
            }
    """

if __name__ == "__main__":
    app.run(debug=True)

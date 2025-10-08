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
            header {
                background-color: #222;
                color: #fff;
                padding: 1px 0;
            }
            section {
                margin: 40px auto;
                max-width: 600px;
                background: white;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
        </style>

    </head>
    <body>
        <header>
            <h1>Justin Rain C. Mangalindan</h1>
            <p>CPE Student | Aspiring Developer</p>
        </header>

        <section>
            <h2>About Myself</h2>
            <p>I am Justin Rain C. Mangalindan, I am a computer engineering student who is passionate on learning Programming techniques and making my own projects as a practice. I mostly spent on developing my hardware skills such as basic troubleshooting of computers and I tend to focus now on software as a strength.</p>
        </section>

        <section>
            <h2>My Projects</h2>
            <ul>
                <li>• Basic Python Operations</li>
                <li>• Personal Portfolio Website</li>
                <li>• Terminal-based dank-memer</li>
                <li>• Quiz reader and Quiz creator program</li>
            </ul>
        </section>

    """

if __name__ == "__main__":
    app.run(debug=True)

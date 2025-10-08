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
            ul {
                list-style: none;
                padding: 0;
                font-size: 18px;
                text-align: left;
                display: inline-block;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
            a {
                color: #007BFF;
                text-decoration: none;
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
                <li><a href="https://github.com/synchronizedcoding/practice_python_programs_batch_1_to_4" target="_blank">• Basic Python Operations</a></li>
                <li><a href="https://github.com/synchronizedcoding/my_flask_portfolio" target="_blank">• Personal Portfolio Website</a></li>
                <li><a href="https://github.com/synchronizedcoding/python_dank_memer_code" target="_blank">• Terminal-based dank-memer</a></li>
                <li><a href="https://github.com/synchronizedcoding/oop_quiz_creator_and_reader" target="_blank">• Quiz reader and Quiz creator program</a></li>
            </ul>
        </section>

        <section>
            <h2>Contact</h2>
            <p>GitHub: <a href="https://github.com/synchronizedcoding" target="_blank">https://github.com/synchronizedcoding</a></p>
        </section>
    """

if __name__ == "__main__":
    app.run(debug=True)

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
    
    """

if __name__ == "__main__":
    app.run(debug=True)

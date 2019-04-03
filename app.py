import os
from bocadillo import App

app = App()

@app.route("/")
async def index(req, res):
    res.text = "Hello, World!"

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, redirect, request, flash, session

app = Flask(__name__)


@app.route('/')
def show_main():

    return render_template("horror_show.html")

if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask('')

app.route('/')
def index():
  return "hello world!!!!"

app.run('0.0.0.0')

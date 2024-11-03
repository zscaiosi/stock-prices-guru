from flask import Flask, request

app = Flask(__name__)

base_route = "/stocks-prices"

@app.route(base_route + "/login", methods=["POST"])
def post_login():
  print("Request Data:")
  print(request.json.get('password'))
  print(request.json.get('username'))

  return { "jwt": "" }
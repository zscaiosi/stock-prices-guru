from flask import Flask, request
from application.commands.save_stocks_data_command import SaveStocksDataCommand
from application.commands.dtos import save_stocks_data_dto

app = Flask(__name__)

base_route = "/stocks-guru"

save_stocks_command = SaveStocksDataCommand(None)

@app.route(base_route + "/login", methods=["POST"])
def post_login():
  print("Request Data:")
  print(request.json.get('password'))
  print(request.json.get('username'))

  return { "jwt": "" }

@app.route(base_route + "/stocks/data", methods=["POST"])
def post_save_stocks_data():
  print("Request Data:")
  print(request.json)
  save_stocks_command.handle(save_stocks_data_dto.SaveStocksDataDto(
    request.json.get("identifier"),
    request.json.get("price"),
    request.json.get("utc_date_time")
  ))

  return { "success": True }

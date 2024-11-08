from application.commands.dtos.save_stocks_data_dto import SaveStocksDataDto

class SaveStocksDataCommand:
  def __init__(self, command_publisher_port):
    self.command_publisher_port = command_publisher_port

  def handle(self, dto: SaveStocksDataDto):
    print("Handling Command: ")
    print(dto)
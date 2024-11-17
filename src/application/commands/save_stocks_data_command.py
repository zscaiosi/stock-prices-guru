from application.ports.command_publisher_port import CommandPublisherPort
from application.commands.dtos.save_stocks_data_dto import SaveStocksDataDto

class SaveStocksDataCommand:
  def __init__(self, command_publisher_port: CommandPublisherPort):
    self.command_publisher_port = command_publisher_port

  def handle(self, dto: SaveStocksDataDto):
    self.command_publisher_port.publish_historical_price(
      dto.identifier,
      dto.price,
      dto.date_utc
    )
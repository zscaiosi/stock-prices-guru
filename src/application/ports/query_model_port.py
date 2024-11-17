from application.ports.dtos.stock_price_dto import StockPriceDto
import json

class QueryModelPort:
  def get_stock_price(identifier: str, date_utc: str) -> StockPriceDto:
    pass

  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)
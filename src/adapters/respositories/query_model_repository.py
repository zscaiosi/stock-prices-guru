from application.ports.query_model_port import QueryModelPort
from application.ports.dtos.stock_price_dto import StockPriceDto

class QueryModelRepository(QueryModelPort):
  def __init__(self):
    print("new QueryModelRepository")

  def get_stock_price(self, identifier: str, date_utc: str):
    print("QueryModelPort.get_stock_price NOT_IMPLEMENTED")
    return StockPriceDto(identifier, 0.0, date_utc)

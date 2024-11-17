from application.ports.query_model_port import QueryModelPort
from application.queries.dtos.predicted_stock_price_dto import PredictedStockPriceDto
from datetime import datetime

class PredictPriceQuery:
  def __init__(self, query_model_port: QueryModelPort):
    self.query_model_port = query_model_port

  def get_stock_price(self, stock_identifier: str, date_utc: str) -> PredictedStockPriceDto:
    predicted_price = self.query_model_port.get_stock_price(stock_identifier, date_utc)
    print("Querying predicted price for {} at {}.".format(stock_identifier, date_utc))
    
    return PredictedStockPriceDto(predicted_price.identifier, predicted_price.price, 0.035, predicted_price.date_utc)

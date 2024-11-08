from application.ports.query_model_port import QueryModelPort
from datetime import datetime

class PredictPriceQuery:
  def __init__(self, query_model_port: QueryModelPort):
    self.query_model_port = query_model_port

  def get_stock_price(self, stock_identifier: str, date_utc: str):
    predicted_price = self.query_model_port.get_stock_price(stock_identifier, date_utc)
    print("Querying predicted price for {} at {}.".format(stock_identifier, date_utc))
    return {}
  
  def fetch_stock_prices(self, stock_identifier: str, until_date: str):
    current_date_time = datetime.now()
    predicted_prices = self.query_model_port.fetch_stock_prices(
      stock_identifier,
      current_date_time.strftime("%Y-%m-%d")
    )
    print("Fetching predicted prices for {} at {}.".format(stock_identifier, current_date_time.strftime("%Y-%m-%d")))

    return []
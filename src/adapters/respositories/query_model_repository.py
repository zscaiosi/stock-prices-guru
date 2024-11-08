from application.ports.query_model_port import QueryModelPort

class QueryModelRepository(QueryModelPort):
  def __init__(self):
    print("new QueryModelRepository")

  def get_stock_price(self, identifier: str, date_utc: str):
    pass

  def fetch_stock_prices(self, identifier: str, start_date: str, end_date: str):
    pass
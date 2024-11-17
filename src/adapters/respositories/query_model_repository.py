from application.ports.query_model_port import QueryModelPort
from application.ports.dtos.stock_price_dto import StockPriceDto
import pymongo

class QueryModelRepository(QueryModelPort):
  def __init__(self):
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    self.db = mongoClient["stocks-prices-lstm"]

  def get_stock_price(self, identifier: str, date_utc: str) -> StockPriceDto:
    query = {
      "identifier": identifier,
      "date_utc": date_utc
    }
    print("Search query: {}".format(query))
    cursor = self.db["PredictedPrices"].find_one(query)
    print(cursor)

    if cursor == None:
      return cursor
    else:
      return StockPriceDto(cursor["identifier"], cursor["price"], cursor["date_utc"])

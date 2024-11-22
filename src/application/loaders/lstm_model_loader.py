from application.ports.query_model_port import QueryModelPort
from application.dtos.predicted_prices_dto import PredictedPricesDto

class LstmModelLoader:
  def __init__(self, query_model_port: QueryModelPort):
    self.query_model_port = query_model_port
    self.yfinance_data = {}

  def train_from_data(self) -> list[PredictedPricesDto]:
    predicted_prices = []

    historical_prices = self.query_model_port.get_historical_prices()
    for historical_price in historical_prices:
      predicted_prices.append(PredictedPricesDto(
        historical_price["identifier"],
        historical_price["price"],
        historical_price["date_utc"]
      ))
      self.__load_yahoo_finance_data(historical_price["identifier"])

    return predicted_prices

  def __load_yahoo_finance_data(self, sticker: str):
    print("Loading data...")
    self.yfinance_data[sticker] = {}

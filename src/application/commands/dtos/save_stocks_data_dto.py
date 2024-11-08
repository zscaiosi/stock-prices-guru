class SaveStocksDataDto:
  def __init__(self, identifier, price, utc_date_time):
    self.identifier = identifier
    self.price = price
    self.utc_date_time = utc_date_time

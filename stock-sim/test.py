import pickle


class StockData:
	def __init__(self, data, filename):
		self.name = filename
		self.data = data

class DataPoint:
	def __init__(self, date, high, low):
		self.date = datetime.strptime(date, '%Y-%m-%d')
		self.high = float(high)
		self.low = float(low)
# with open("data.pkl", 'rb') as file:
#   stock_data = pickle.load(file)


# print(stock_data)
print(0.1 * float("-inf"))
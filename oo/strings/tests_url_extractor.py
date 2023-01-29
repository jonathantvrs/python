from decimal import Decimal
from forex_python.converter import CurrencyRates

from url_extractor import URLExtractor

UNITED_STATES_CODE = 'USD'
BRAZILIAN_CODE = 'BRL'


url = URLExtractor('bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real')

source_currency = url.get_param_value('moedaOrigem')
source_currency_code = UNITED_STATES_CODE if source_currency == 'dolar' else BRAZILIAN_CODE 
destination_currency = url.get_param_value('moedaDestino')
destination_currency_code = UNITED_STATES_CODE if destination_currency == 'dolar' else BRAZILIAN_CODE 
amount = Decimal(url.get_param_value('quantidade'))

currency_rates = CurrencyRates()
converted_value = currency_rates.convert(source_currency_code, destination_currency_code, amount)
print(converted_value)
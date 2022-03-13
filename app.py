from tipo_cambio import TipoCambioFactoring


tc = TipoCambioFactoring()
response = tc.get_exchange_rate('USD', '13/03/2022','13/03/2022')
print(response)
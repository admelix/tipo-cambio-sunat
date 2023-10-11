# Factoring Total
[![PyPI version](https://badge.fury.io/py/FactoringTotal.svg)](https://pypi.org/project/FactoringTotal)


## Descripción
Libreria para obtener el tipo de cambio de SUNAT Y SBS junto al valor del dolar contable manejado por SBS. Ademas, se permiten realiar conversiones entre divisas.

## Instalación
```
pip install FactoringTotal
```

## Uso básico
```python
from tipo_cambio import TipoCambioFactoring

ft = TipoCambioFactoring()
data = ft.get_exchange_rate('USD', '01/01/2023', '10/01/2023')
print(data)
```
Obtendremos el siguiente resultado:
```python
{'01/01/2023': {'compra': '3.808', 'venta': '3.820'}, '02/01/2023': {'compra': '3.808', 'venta': '3.820'}, '03/01/2023': {'compra': '3.812', 'venta': '3.823'}, '04/01/2023': {'compra': '3.822', 'venta': '3.827'}, '05/01/2023': {'compra': '3.824', 'venta': '3.830'}, '06/01/2023': {'compra': '3.800', 'venta': '3.806'}, '07/01/2023': {'compra': '3.800', 'venta': '3.806'}, '08/01/2023': {'compra': '3.800', 'venta': '3.806'}, '09/01/2023': {'compra': '3.792', 'venta': '3.803'}, '10/01/2023': {'compra': '3.802', 'venta': '3.806'}}
```

## Configuración
| Opción        | Descripción                                | Predeterminado | Valores permitidos |
|:-------------:|--------------------------------------------|:--------------:|:------------------:|
| `source`      | La fuente de dónde se obtendrán los datos. | `SBS`          | `SBS`, `SUNAT`.    |
| `date_format` | Formato de fecha devuelto.                 | `%d/%m/%Y`     | [http://strftime.org](http://strftime.org) |

## Ejemplo Resultado Sunat y SBS junto con el valor del dolar contable. 
```python
from tipo_cambio import TipoCambioFactoring

ft = TipoCambioFactoring()
data = ft.get_exchange_sbs_sunat('01/01/2023', '02/01/2023')
print(data)
```
Obtendremos el siguiente resultado:
```python
{'status': 200, 'sunat': {'01-01-23': {'compra': '3.808', 'venta': '3.820'}, '02-01-23': {'compra': '3.808', 'venta': '3.820'}}, 'sbs': {'01-01-23': {'compra': '3.808', 'venta': '3.820'}, '02-01-23': {'compra': '3.808', 'venta': '3.820'}}, 'sbs_dolar_contable': '3.8250'}
```
## Divisas
Listado de divisas permitidas.

| Divisa               |  ISO  |
|----------------------|:-----:|
| Dólar estadounidense | `USD` |
| Corona Sueca         | `SEK` |
| Franco Suizo         | `CHF` |
| Dólar canadiense     | `CAD` |
| Euro                 | `EUR` |
| Yen japonés          | `JPY` |
| Libra esterlina      | `GBP` |

## Métodos
#### get_exchange_rate(`currency, from_date, to_date=None`)
Obtener el tipo de cambio de la moneda indicada por fecha o rango de fechas. Devolverá por defecto un diccionario ([https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)).

#### get_exchange_sbs_sunat(`from_date, to_date`)
Obtendra el tipo de cambio del dolar segun el rango de fechas, con la excepcion del dolar contable que, siempre sera el valor del dia en que se realice la consulta . Devolverá por defecto un diccionario ([https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)).



## Consideraciones
* Sólo se puede obtener el tipo de cambio desde el año 2000 en adelante.
* El tipo de cambio de la SUNAT es el tipo de cambio del cierre del día anterior de la SBS (fuente [http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias](http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias)).
* El tipo de cambio no se publica en la SBS o SUNAT todos los díás. En estos casos se tomará el tipo de cambio del día anterior.

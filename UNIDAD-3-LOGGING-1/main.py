import logging 
logging.basicConfig(level=logging.DEBUG)
logging.Formatter(fmt=' %(name)s - %(levelname)s - %(message)s')
fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]
for frut in fruits:
    try:
        logging.info(f'conversion exitosa : {frut} ---> {frut.lower()}')
    except:
        logging.error(f'conversion fallida : {frut}')

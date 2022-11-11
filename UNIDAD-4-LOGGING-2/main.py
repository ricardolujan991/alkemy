from functions import extraer_informacion
from functions import logger_main
try: 
    logger_main.info('...Leyendo el archvio...')
    with open('cuento.txt','r') as file:
        extraer_informacion(file)
    logger_main.info('...Archivo procesado...')
except:
    logger_main.info('No se pudo abrir el archvio')
    
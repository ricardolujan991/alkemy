import logging.config
import logging

logging.config.fileConfig('log_config_file.conf')
logger_main = logging.getLogger('main')
logger_functions = logging.getLogger('functions')


def extraer_informacion(file):
        text = file.read()
        renglones = text.split('\n')
        logger_functions.info(f'{file.name} - cantidad de renglones : {len(renglones)}')
        for renglon in range(len(renglones)):  
            logger_functions.info(f'Renglon {renglon} : {len(renglones[renglon].split(" "))} palabras')
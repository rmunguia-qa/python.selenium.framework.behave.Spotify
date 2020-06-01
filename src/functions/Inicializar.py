# -*- coding: utf-8 -*-

# Importando librría para el manejo de Directorios
import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath((os.path.join(__file__, "../..")))
    DateFormat = '%Y%m%d'
    HourFormat = '%H%M%S'

    # Json Data
    Json = basedir + u'/pages'

    # Entorno Tests
    Environment = 'Dev'

    # Navegador Tests
    Browser = u'CHROME'

    # Directorio Evidencias
    ScreenshotPath = basedir + u'/data/screenshot'

    # Datos Excel
    Excel = basedir + u'/data/excel/DataSpotify.xlsx'

    if Environment == 'Dev':
        URL = ''
        User = ''
        Pass = ''
        # Datos para Conexión con BBDD Entorno DEV
        '''
        DB_HOST = ''
        DB_PORT = ''
        DB_DATABASE = ''
        DB_USER = ''
        DB_PASS = ''
        '''

    if Environment == 'Test':
        URL = ''
        User = ''
        Pass = ''
        # Datos para Conexión con BBDD Entorno TEST
        '''
        DB_HOST = ''
        DB_PORT = ''
        DB_DATABASE = ''
        DB_USER = ''
        DB_PASS = ''
        '''
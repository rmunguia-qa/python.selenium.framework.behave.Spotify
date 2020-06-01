# -*- coding: utf-8 -*-

# Importando clase Inicializar
from functions.Inicializar import Inicializar

# Importando librría para el manejo de Directorios
import os
# Importando librerías para Expresiones regulares
import re
# Importando librerías para Json
import json
# Importando librerías para TIME
import time
# Importando librerías para Pytest
import pytest
# Importando librerías para uso Excel
import openpyxl
# Importando librerías para uso de reportes en Allure Framework
import allure

# Importando librerías para uso DataBase
#import pyodbc as pyodbc

# Importando librerías Selenium
from selenium import webdriver

# Importando librerías control de excepciones
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

# Importando librerías Selenium.webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Importando librerías para Locator Elements
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# Importando librerías de webdriver support y poder utilizar "Expected Conditions"
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Declaramos variable del Scenario como diccionario de Datos
Scenary = {}

# Importando librería para el manejo de fecha y hora
import datetime

# Declaramos variable de Fecha Global con el formato AAAA/MM/DD
fechaGlobal = time.strftime(Inicializar.DateFormat)
# Declaramos variable de Hora Global con el formato HH:MM:SS
horaGlobal = time.strftime(Inicializar.HourFormat)

# Definimos la clase Functions y le pasamos la clase Inicializar como argumento
class Functions(Inicializar):
    ##################################################################
    ##################### - INICIALIZAR DRIVER - #####################
    ##################################################################

    # Función para abrir el navegador y le pasamos como argumentos self, la URL y el Navegador de Inicializar
    def open_browser(self, url=Inicializar.URL, browser=Inicializar.Browser):
        print("Directorio Base: " + Inicializar.basedir)
        self.windows = {}
        print("---------------")
        print(browser)
        print("---------------")

        # Microsoft EDGE
        if browser == "EDGE":
            self.driver = webdriver.Edge(executable_path=Inicializar.basedir + "\\drivers\\msedgedriver.exe")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get(url)
            self.principal = self.driver.window_handles[0]
            self.windows = {'Principal': self.driver.window_handles[0]}
            return self.driver

        # CHROME
        if browser == "CHROME":
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(options=options,
                                           executable_path=Inicializar.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.get(url)
            self.principal = self.driver.window_handles[0]
            self.windows = {'Principal': self.driver.window_handles[0]}
            return self.driver

        # FIREFOX
        if browser == "FIREFOX":
            cap = DesiredCapabilities().FIREFOX
            #cap["marionette"] = False
            self.driver = webdriver.Firefox(capabilities=cap,
                                            executable_path=Inicializar.basedir + "\\drivers\\geckodriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(url)
            self.principal = self.driver.window_handles[0]
            self.windows = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver
    '''
    ##################################################################
    ###################### - LOCATOR ELEMENTS - ######################
    ##################################################################
    # Función para realizar la búsqueda de los elementos con los que vamos a interactuar en el Test
    ###################### - XPATH - ######################
    # DEPRECATED
    def xpath_element(self, xpath):
        elements = self.driver.find_element(By.XPATH, xpath)
        print("XPATH Elements: Se ha interactuado con el elemento " + xpath)
        return elements

    # Función para realizar la búsqueda de los elementos con espera y captura de errores
    # DEPRECATED
    def _xpath_element(self, xpath):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            elements = self.driver.find_element_by_xpath(xpath)
            print(u"Esperar elemento: Se visualiza el elemento " + xpath)
            return elements

        except TimeoutException:
            print(u"Esperar elemento: Elemento no presente " + xpath)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar elemento: Elemento no presente " + xpath)
            Functions.tearDown(self)

    ###################### - ID - ######################
    # DEPRECATED
    def id_element(self, id):
        elements = self.driver.find_element(By.ID, id)
        print("ID Elements: Se ha interactuado con el elemento " + id)
        return elements

    # Función para realizar la búsqueda de los elementos con espera y captura de errores
    # DEPRECATED
    def _id_element(self, id):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.ID, id)))
            elements = self.driver.find_element_by_id(id)
            print(u"Esperar elemento: Se visualiza el elemento " + id)
            return elements

        except TimeoutException:
            print(u"Esperar elemento: Elemento no presente " + id)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar elemento: Elemento no presente " + id)
            Functions.tearDown(self)

    ###################### - NAME - ######################
    # DEPRECATED
    def name_element(self, name):
        elements = self.driver.find_element(By.NAME, name)
        print("NAME Elements: Se ha interactuado con el elemento " + name)
        return elements

    # Función para realizar la búsqueda de los elementos con espera y captura de errores
    # DEPRECATED
    def _name_element(self, name):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.NAME, name)))
            elements = self.driver.find_element_by_name(name)
            print(u"Esperar elemento: Se visualiza el elemento " + name)
            return elements

        except TimeoutException:
            print(u"Esperar elemento: Elemento no presente " + name)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar elemento: Elemento no presente " + name)
            Functions.tearDown(self)

    ###################### - PARTIAL LINK - ######################
    # DEPRECATED
    def partial_link_element(self, partial_link):
        elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link)
        print("PARTIAL LINK Elements: Se ha interactuado con el elemento " + partial_link)
        return elements

    # Función para realizar la búsqueda de los elementos con espera y captura de errores
    # DEPRECATED
    def _partial_link_element(self, partial_link):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, partial_link)))
            elements = self.driver.find_element_by_partial_link_text(partial_link)
            print(u"Esperar elemento: Se visualiza el elemento " + partial_link)
            return elements

        except TimeoutException:
            print(u"Esperar elemento: Elemento no presente " + partial_link)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar elemento: Elemento no presente " + partial_link)
            Functions.tearDown(self)
    '''
    ##################################################################
    ######################## - JSON HANDLES - ########################
    ##################################################################
    '''# Función para iniciar a NONE los valores de la entidad del JSON
    def __init__(self):
        self.json_GetFieldBy = None
        self.json_ValueToFind = None
    '''

    # Función para leer el fichero JSON del directorio "..\pages\"
    def get_json_file(self, file):

        json_path = Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r", encoding='utf-8') as read_file:
                self.json_strings = json.loads(read_file.read())
                print("Función get_json_file: Directorio JSON file es " + json_path)
                return self.json_strings

        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"Función get_json_file: No se encontrá el fichero " + file)
            Functions.tearDown(self)

    # Función para leer las entidades que se incluyen en el fichero JSON
    def get_entity(self, entity):
        if self.json_strings is False:
            print("Función get_entity: Define el DOM (Document Object Model - JSON) para la prueba")
        else:
            try:
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                return True

            except KeyError:
                pytest.skip("Función get_entity: No se ha encontrado la key a la que se hace referencia en la " + entity)
                Functions.tearDown()
                return None

    ##################################################################
    #################### - BEHAVIOR DRIVEN TEST - ####################
    ##################################################################
    # Función para traer los elementos de cada entidad
    def get_elements(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    '''if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)'''
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)

                print("Función get_elements: Elemento obtenido es " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("Función get_elements: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("Función get_elements: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    # Función para obtener el texto de un objeto
    def get_text(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    '''if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)'''
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)

                print("Función get_text: Elemento obtenido es " + self.json_ValueToFind)
                print("Función get_text: El valor del texto obtenido es " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("Función get_text: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("Función get_text: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    # Función para interactuar con elementos tipo Select o DropDown (Lista desplegable)
    def get_select_elements(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element(By.XPATH, self.json_ValueToFind))

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element(By.ID, self.json_ValueToFind))

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element(By.NAME, self.json_ValueToFind))

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind))

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    select = Select(self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind))

                print("Función get_select_elements: Elemento select obtenido es " + self.json_ValueToFind)
                return select

            except NoSuchElementException:
                print("Función get_select_elements: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("Función get_select_elements: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    ######################## - SELECT FIELD - ########################
    # Función para interactuar con elementos tipo Select o DropDown y seleccionar el texto
    def select_by_text(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

    # Función para interactuar con elementos tipo Select o DropDown y seleccionar el valor
    def select_by_value(self, entity, value):
        Functions.get_select_elements(self, entity).select_by_value(value)

    ##################################################################
    ######################## - SWITCH FRAME - ########################
    ##################################################################
    # Función para acceder a un iFRAME
    def switch_to_iframe(self, locator):
        iframe = Functions.get_elements(self, locator)
        self.driver.switch_to.frame(iframe)
        print(f"Se ha realizado el switch al frame " + locator)

    # Función para volver al PARENT FRAME
    def switch_to_parentFrame(self):
        self.driver.switch_to.parent_frame()

    ##################################################################
    ####################### - SWITCH WINDOWS - #######################
    ##################################################################
    # Función que sirve para cambiar de ventana/pestaña
    def switch_to_windows_name(self, window):
        if window in self.windows:
            self.driver.switch_to.window(self.windows[window])
            Functions.page_has_loaded(self)
            print("Volviendo a la ventana " + window + ": " + self.windows[window])
        else:
            self.nWindows = len(self.driver.window_handles) - 1
            self.windows[window] = self.driver.window_handles[int(self.nWindows)]
            self.driver.switch_to.window(self.windows[window])
            self.driver.maximize_window()
            print(self.windows)
            print("Estamos en la ventana " + window + ": " + self.windows[window])
            Functions.page_has_loaded(self)

    ##################################################################
    ######################### - SEND  KEYS - #########################
    ##################################################################
    # Función para introducir datos en un INPUT
    def send_key_text(self, entity, text):
        ##Functions.get_elements(self, entity).clear()
        Functions.get_elements(self, entity).send_keys(Keys.CONTROL, "a")
        Functions.get_elements(self, entity).send_keys(Keys.DELETE)
        Functions.get_elements(self, entity).send_keys(text)

    # Función para introducir KEYS del teclado en una APP - CREAR STEP
    def send_specific_keys(self, element, key):
        if key == 'Enter':
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        if key == 'Tab':
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        if key == 'Space':
            Functions.get_elements(self, element).send_keys(Keys.SPACE)
        time.sleep(3)

    ##################################################################
    ######################### - JAVASCRIPT - #########################
    ##################################################################
    # Función que sirve para comprobar que una APP o web page está cargada
    def page_has_loaded(self):
        driver = self.driver
        print("Verificando que la {} página ha sido cargada.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se ha completado la carga"

    # Función que sirve para abrir una nueva pestaña o ventana
    def new_window(self, url):
        self.driver.execute_script(f'''window.open("{url}","_blank");''')
        Functions.page_has_loaded(self)

    # Función que sirve para hacer CLICK sobre un elemento
    def js_click(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    element = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", element)
                    print(u"Se ha realizado click a: " + locator)
                    return True

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    element = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", element)
                    print(u"Se ha realizado click a: " + locator)
                    return True

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    element = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", element)
                    print(u"Se ha realizado click a: " + locator)
                    return True

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", element)
                    print(u"Se ha realizado click a: " + locator)
                    return True

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    element = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", element)
                    print(u"Se ha realizado click a: " + locator)
                    return True

            except TimeoutException:
                print("Función js_click: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    # Función que sirve para realizar SCROLLING a un elemento
    def scroll_to(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    element = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    print(u"Se ha realizado scroll a: " + locator)
                    return True

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    element = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    print(u"Se ha realizado scroll a: " + locator)
                    return True

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    element = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    print(u"Se ha realizado scroll a: " + locator)
                    return True

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    print(u"Se ha realizado scroll a: " + locator)
                    return True

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    element = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    print(u"Se ha realizado scroll a: " + locator)
                    return True

            except TimeoutException:
                print("Función scroll_to: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    ##################################################################
    ####################### - ACTION  CHAINS - #######################
    ##################################################################
    # Función que sirve para poner el MOUSE sobre un elemento
    def mouse_over(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    element = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(element)
                    action.click(element)
                    action.perform()
                    print(u"Función mouse_over: Se ha movido el mouse y realizado click al elemento: " + locator)
                    return True

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    element = self.driver.find_element(By.ID, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(element)
                    action.click(element)
                    action.perform()
                    print(u"Función mouse_over: Se ha movido el mouse y realizado click al elemento: " + element)
                    return True

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    element = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(element)
                    action.click(element)
                    action.perform()
                    print(u"Función mouse_over: Se ha movido el mouse y realizado click al elemento: " + element)
                    return True

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(element)
                    action.click(element)
                    action.perform()
                    print(u"Función mouse_over: Se ha movido el mouse y realizado click al elemento: " + element)
                    return True

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    element = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(element)
                    action.click(element)
                    action.perform()
                    print(u"Función mouse_over: Se ha movido el mouse y realizado click al elemento: " + element)
                    return True

            except TimeoutException:
                print("Función mouse_over: No se ha encontrado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    ##################################################################
    ####################### - WAIT  ELEMENTS - #######################
    ##################################################################
    # Función para esperar a un elemento (por n condiciones)
    def wait_element(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    '''if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)'''
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Función wait_element: Se ha visualizado el elemento " + locator)
                    return True

                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Función wait_element: Se ha visualizado el elemento " + locator)
                    return True

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Función wait_element: Se ha visualizado el elemento " + locator)
                    return True

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Función wait_element: Se ha visualizado el elemento " + locator)
                    return True

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"Función wait_element: Se ha visualizado el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("Función wait_element: No se ha visualizado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("Función wait_element: No se ha visualizado el elemento " + self.json_ValueToFind)
                Functions.tearDown(self)

    # Función que sirve para esperar un tiempo predeterminado (similar a time)
    def wait_time(self, timeLoad=8):
        print("Espera: Iniciamos en (" + str(timeLoad) + ")")
        try:
            totalWait = 0
            while (totalWait < timeLoad):
                print("Cargando ... intento: " + str(totalWait))
                time.sleep(1)
                totalWait = totalWait + 1
        finally:
            print("Función wait_time: Carga Finalizada correctamente ... ")

    ##################################################################
    ###################### - ALERTS / POP UPS - ######################
    ##################################################################
    # Función que sirve para interaccionar con Alert Windows o PopUps emergentes
    def alert_windows(self, accept="accept"):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.alert_is_present(), print("Esperando alerta ..."))

            alert = self.driver.switch_to.alert

            print(alert.text)

            if accept.lower() == "accept":
                alert.accept()
                print("Click in Accept")
            else:
                alert.dismiss()
                print("Click in Dismiss")

        except NoAlertPresentException:
            print("Alerta no presente")
        except NoSuchWindowException:
            print("Alerta no presente")
        except TimeoutException:
            print("Alerta no presente")

    ##################################################################
    #################### - ASSERTIONS && CHECKS - ####################
    ##################################################################
    # Función que sirve para realizar ASSERT sobre un texto determinado
    def assert_text(self, locator, text):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            # XPATH ELEMENT
            if self.json_GetFieldBy.lower() == "xpath":
                ObjText = self.driver.find_element(By.XPATH, self.json_ValueToFind).text
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))

            # ID ELEMENT
            if self.json_GetFieldBy.lower() == "id":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.ID, self.json_ValueToFind).text

            # NAME ELEMENT
            if self.json_GetFieldBy.lower() == "name":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.NAME, self.json_ValueToFind).text

            # PARTIAL LINK TEXT ELEMENT
            if self.json_GetFieldBy.lower() == "link":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind).text

            # CSS SELECTOR ELEMENT
            if self.json_GetFieldBy.lower() == "css":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind).text

        print("Función assert_text: El valor del texto mostrado de la entidad " + locator + " es "
              + ObjText + " y el valor esperado " + text)

        assert text == ObjText, "El texto esperado no es correcto"

    # Función que sirve para verificar si un elemento está presente (devuelve True o False)
    def check_element(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        timeout = 10

        if Get_Entity is None:
            print("No se ha encontrado el valor en el JSON file definido")

        else:
            try:
                # XPATH ELEMENT
                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, timeout)
                    wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Función check_element: Se ha comprobado la presencia del elemento " + locator)
                    return True
                # ID ELEMENT
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, timeout)
                    wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Función check_element: Se ha comprobado la presencia del elemento " + locator)
                    return True

                # NAME ELEMENT
                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, timeout)
                    wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Función check_element: Se ha comprobado la presencia del elemento " + locator)
                    return True

                # PARTIAL LINK TEXT ELEMENT
                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, timeout)
                    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Función check_element: Se ha comprobado la presencia del elemento " + locator)
                    return True

                # CSS SELECTOR ELEMENT
                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, timeout)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"Función check_element: Se ha comprobado la presencia del elemento " + locator)
                    return True

            except TimeoutException:
                print("Función check_element: No se ha podido comprobar la presencia del elemento " +
                      self.json_ValueToFind)
                return False

    ##################################################################
    ######################## - DATA SCENARY - ########################
    ##################################################################
    # Diccionarios datos Python
    # Función que sirve para crear la variable de Scenario
    def create_variable_scenary(self, key, value):
        Scenary[key] = value
        print(Scenary)
        print("Función create_variable_scenary: Se ha almacenado la key " + key + ": " + value)

    # Función que sirve para guardar la variable de Scenario
    def save_variable_scenary(self, element, variable):
        Scenary[variable] = Functions.get_text(self, element)
        print(Scenary)
        print("Función save_variable_scenary: Se ha almacenado el valor " + variable + ": " + Scenary[variable])

    # Función que sirve para traer la variable de Scenario
    def get_variable_scenary(self, variable):
        self.variable = Scenary[variable]
        print(f"Función get_variable_scenary: {self.variable}")
        return self.variable

    # Función que sirve para comparar 2 variables de Scenario
    def compare_with_variable_scenary(self, element, variable):
        variable_scenary = str(Scenary[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print(_exist)
        print(f"Función compare_with_variable_scenary: Comparamos los valores... verificar que si {variable_scenary}"
              f" esta presente en {element_text}: {_exist}")
        assert _exist == True, f"{variable_scenary} != {element_text}"

    # Función que sirve para manejar fechas. Cambiar fechas para pruebas en el pasado
    def textDateEnvironmentReplace(self, text):
        if text == 'today':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'last month':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormat)

        return text

    ##################################################################
    ######################### - DATA EXCEL - #########################
    ##################################################################
    # Función para leer datos de una Hoja EXCEL
    def read_cell(self, cell):
        workBook = openpyxl.load_workbook(Inicializar.Excel)
        sheet = workBook["DataSpotify"] # Nombre de la sheet de la excel de datos
        value = str(sheet[cell].value)
        print(u"-------------------------------------------")
        print(u"WorkBook utilizado es: " + Inicializar.Excel)
        print(u"Valor de la celda es: " + value)
        print(u"-------------------------------------------")
        return value

    # Función para escribir datos en una Hoja EXCEL
    def write_cell(self, cell: object, value):
        workBook = openpyxl.load_workbook(Inicializar.Excel)
        sheet = workBook["DataSpotify"] # Nombre de la sheet de la excel de datos
        sheet[cell] = value
        workBook.save(Inicializar.Excel)
        print(u"--------------------------------------------------------------------")
        print(u"WorkBook utilizado es: " + Inicializar.Excel)
        print(u"Se ha escrito en la celda " + str(cell) + u" el valor: " + str(value))
        print(u"--------------------------------------------------------------------")
        return value

    #----------------------------------------------------------------#
    # ##### ##### ##### #####  - DATABASE -  # ##### ##### ##### #####
    #----------------------------------------------------------------#
    # Función que sirve para realizar la conexión a una DATABASE externa (Ejemplo PostgreSQL)
    '''
    def pyodbc_conn(self, _host=Inicializar.DB_HOST, _port=Inicializar.DB_PORT, _dbname=Inicializar.DB_DATABASE,
                         _user=Inicializar.DB_USER, _pass=Inicializar.DB_PASS):
        #print(pyodbc.drivers())
        try:
            config = dict(server=_host, port=_port, database=_dbname, username=_user, password=_pass)

            conn_str = ('SERVER={server};' + 'PORT={port};' + 'DATABASE={database};' + 'UID={username};' + \
                            'PWD={passwprd};')

            conn = pyodbc.connect(r'DRIVER={PostgreSQL ANSI};' + conn_str.format(**config))

            self.cursor = conn.cursor()
            print("Always connected")

            return self.cursor

        except (pyodbc.OperationalError) as error:
            self.cursor = None
            pytest.skip("Error en connection strings: " + str(error))

    # Función que sirve para realizar uns QUERY sobre una DATABASE externa (Ejemplo PostgreSQL)
    def pyodbc_query(self, _query):
        self.cursor = Functions.pyodbc_conn(self)

        if self.cursor is not None:
            try:
                self.cursor.execute(_query)
                self.result = self.cursor.fetchall()

                for row in self.result:
                    print(row.items())

            except (pyodbc.Error) as error:
                print("Error en la consulta", error)

            finally:
                if (self.cursor):
                    self.cursor.close()
                    print("Función pyodbc_query: Se ha cerrado la conexión")
    '''

    ##################################################################
    ######################### - SCREENSHOT - #########################
    ##################################################################
    # Función para traer la hora actual
    def hora_Actual(self):
        self.hora = time.strftime(Inicializar.HourFormat)  # Formato HH:MM:SS
        return self.hora

    # Función que sirve para crear el PATH donde se dejan las Capturas de Pantalla - Screenshot
    def create_path(self):
        dia = time.strftime(Inicializar.DateFormat) # Formato YYYY/MM/DD

        GeneralPath = Inicializar.ScreenshotPath
        DriverTest = Inicializar.Browser
        TestCase = self.__class__.__name__ # Sirve para traerse el nombre del caso de prueba
        horaAct = horaGlobal
        x = re.search('Context', TestCase)

        if (x):
            path = f"{GeneralPath}/{dia}/{DriverTest}/{horaAct}/"
        else:
            path = f"{GeneralPath}/{dia}/{TestCase}/{DriverTest}/{horaAct}/"

        # Si no existe el PATH, se crea con la siguiente instrucción
        if not os.path.exists(path):
            os.makedirs(path)

        return path

    # Función que sirve para realizar la captura de la pantalla
    def screenshot(self, TestCase="screenshot"):
        path = Functions.create_path(self)
        img = f'{path}{TestCase}_(' + str(Functions.hora_Actual(self)) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)

        return img

    # Función que sirve para realizar la captura de pantalla y usarla en el report de ALLURE
    def screenshot_allure(self, description):
        allure.attach(self.driver.get_screenshot_as_png(), description, attachment_type=allure.attachment_type.PNG)

    ##################################################################
    ######################### - TEAR  DOWN - #########################
    ##################################################################
    # Función para definir el cierre del navegador al terminar la prueba
    def tearDown(self):
        print("El navegador se cerrará ahora")
        self.driver.quit()

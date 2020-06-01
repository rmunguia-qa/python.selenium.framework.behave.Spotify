# -*- coding: utf-8 -*-

# Importando librería behave
from behave import *

# Importando librería pytest
import pytest

# Importando def Functions como "Selenium"
from src.functions.Functions import Functions as Selenium

# Use matcher ("Regular Expresions")
use_step_matcher("re")

# Definición de la clase de Steps
class StepsDefinitions():

    @given("Abrir la APP (.*) con el navegador (.*)")
    def step_impl(self, url, browser):
        Selenium.open_browser(self, url=url, browser=browser)
        Selenium.page_has_loaded(self)

    @step("Cargar el DOM de la APP: (.*)")
    def step_impl(self, DOM):
        Selenium.get_json_file(self, DOM)

    @given("Introducir el valor (.*) en el campo (.*)")
    def step_impl(self, text, locator):
        Selenium.wait_element(self, locator)
        Selenium.send_key_text(self, locator, text)

    @step("Hacer click sobre el botón (.*)")
    def step_impl(self, locator):
        Selenium.js_click(self, locator)

    @then('Verificar el error (.*) con el texto "(.*)"')
    def step_impl(self, locator, text):
        Selenium.assert_text(self, locator, text)

    @step("Informar el valor (.*) en el campo (.*)")
    def step_impl(self, text, locator):
        Selenium.send_key_text(self, locator, text)

    @step("Seleccionar el valor (.*) en el campo (.*)")
    def step_impl(self, text, entity):
        Selenium.select_by_text(self, entity, text)

    @step("Seleccionar la opción (.*) en el campo (.*)")
    def step_impl(self, value, entity):
        Selenium.select_by_value(self, entity, value)

    @step("Hacer click sobre la opción (.*)")
    def step_impl(self, locator):
        Selenium.js_click(self, locator)

    @then("Cerrar la APP")
    def step_impl(self):
        Selenium.tearDown(self)

    @given("Eliminar el mensaje de (.*)")
    def step_impl(self, locator):
        Selenium.mouse_over(self, locator)

    @step("Esperar (.*) segundos")
    def step_impl(self, timeLoad):
        timeLoad = int(timeLoad)
        Selenium.wait_time(self, timeLoad)

    @step("Hacer click sobre la imagen (.*)")
    def step_impl(self, locator):
        Selenium.js_click(self, locator)

    @then("Esperar que se haya cargado la página y volver al registro")
    def step_impl(self):
        Selenium.page_has_loaded(self)
        self.driver.back()
        print("Se ha vuelto al registro con éxito")

    @then("Cambiar a la nueva ventana (.*)")
    def step_impl(self, window):
        Selenium.switch_to_windows_name(self, window)
        Selenium.page_has_loaded(self)

    @step("Cerrar el driver y hacer foco en la ventana (.*)")
    def step_impl(self, window):
        self.driver.close()
        Selenium.switch_to_windows_name(self, window)

    @step('Verificar el (.*) con el texto "(.*)"')
    def step_impl(self, locator, text):
        Selenium.assert_text(self, locator, text)

    @step("Hacer click sobre el Check box (.*)")
    def step_impl(self, locator):
        Selenium.js_click(self, locator)

    @step('Hacer click sobre el link "(.*)"')
    def step_impl(self, locator):
        Selenium.js_click(self, locator)

    @step("Hacer click sobre el link (.*)")
    def step_impl(self, entity):
        Selenium.get_elements(self, entity).click()

    @then("Hacer screenshot (.*)")
    def step_impl(self, TestCase):
        Selenium.screenshot(self, TestCase)

    @step("Esperar que el campo (.*) se haya cargado y sea clickable")
    def step_impl(self, locator):
        Selenium.wait_element(self, locator)
        Selenium.check_element(self, locator)

    @then("Hacer skip de la prueba")
    def step_impl(self):
        Selenium.tearDown(self)
        pytest.skip("Eliminar de la prueba automática el paso 3")

    @given("Verificar la presencia de la imagen (.*)")
    def step_impl(self, locator):
        Selenium.check_element(self, locator)

    @given("Verificar la lista de (.*) disponible y pulsar (.*)")
    def step_impl(self, locator1, locator2):
        Selenium.mouse_over(self, locator1)
        Selenium.check_element(self, locator2)
        Selenium.js_click(self, locator2)
# -*- coding: utf-8 -*-
# Created by MuNGuia10 at 17/04/2020

@Spotify
Feature: Funciones básicas de Selenium con BDD - Registro Spotify
  # Funciones básicas de Selenium con BDD - Registro Spotify

  @SpotifyControlErrores
  Scenario: Spotify Register - Field Email Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador CHROME
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor   en el campo Email
    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_Email1 con el texto "Es necesario que indiques tu correo electrónico."

    Given Introducir el valor rmunguia10@ en el campo Email
    Then Verificar el error Err_Email2 con el texto "Este correo electrónico no es válido. Asegúrate de que tenga un formato como este: ejemplo@email.com"

    Given Introducir el valor rmunguia10@gmail.com en el campo Email
    Then Verificar el error Err_Email3 con el texto "Este correo electrónico ya está conectado a una cuenta. Inicia sesión."

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Male
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP


  @SpotifyControlErrores
  Scenario: Spotify Register - Field EmailConfirm Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador EDGE
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email

    Given Introducir el valor   en el campo EmailConfirm
    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_ConfEmail1 con el texto "Es necesario que confirmes tu correo electrónico."

    Given Introducir el valor rmunguia10@gmail.co en el campo EmailConfirm
    Then Verificar el error Err_ConfEmail2 con el texto "Las direcciones de correo electrónico no coinciden."

    Given Introducir el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Female
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field Password Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador FIREFOX
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm

    Given Introducir el valor  en el campo Password
    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_Password1 con el texto "Es necesario que indiques una contraseña."

    Given Introducir el valor Udemy en el campo Password
    Then Verificar el error Err_Password2 con el texto "Tu contraseña es demasiado corta."

    Given Introducir el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Binary
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field Name Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador CHROME
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password

    Given Introducir el valor  en el campo Name
    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_Name con el texto "Indica un nombre para tu perfil."

    Given Introducir el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Male
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field BirthDay Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador EDGE
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name

    Given Introducir el valor   en el campo BirthDay
    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_BirthDateDay con el texto "Indica un día válido del mes."

    Given Introducir el valor 0 en el campo BirthDay
    Then Verificar el error Err_BirthDateDay con el texto "Indica un día válido del mes."

    Given Introducir el valor 32 en el campo BirthDay
    Then Verificar el error Err_BirthDateDay con el texto "Indica un día válido del mes."

    Given Introducir el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Binary
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field BirthMonth Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador FIREFOX
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay

    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_BirthDateMonth con el texto "Selecciona tu mes de nacimiento."

    Given Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Male
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field BirthYear Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador CHROME
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth

    Given Introducir el valor   en el campo BirthYear
    And Hacer click sobre el botón RegisterButton
    Then Verificar el error Err_BirthDateYear1 con el texto "Indica un año válido."

    Given Introducir el valor 2007 en el campo BirthYear
    Then Verificar el error Err_BirthDateYear2 con el texto "Lo sentimos, pero no cumples los requisitos de edad de Spotify."

    Given Introducir el valor 1986 en el campo BirthYear

    Then Hacer click sobre la opción Female
    And Hacer click sobre el botón RegisterButton
    And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field Gender Errors
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador EDGE
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear
    And Hacer click sobre el botón RegisterButton

    Then Verificar el error Err_Gender con el texto "Selecciona tu género."
	And Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyControlErrores
  Scenario: Spotify Register - Field Captcha Error
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador FIREFOX
    And Cargar el DOM de la APP: spotify_register

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Informar el valor Udemy2020 en el campo Password
    And Informar el valor Rubén Munguía en el campo Name
    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear
    And Hacer click sobre la opción Binary
    And Hacer click sobre el botón RegisterButton

    Then Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    Then Cerrar la APP

  @SpotifyRegistro
  Scenario: Spotify Full Register
    Given Abrir la APP https://www.spotify.com/es/signup/ con el navegador CHROME
    And Cargar el DOM de la APP: spotify_register

    Given Eliminar el mensaje de Cookies
    And Hacer click sobre la imagen Logo
    And Esperar 2 segundos
    And Verificar el SpotifyText con el texto "Música para todos."
    And Esperar 2 segundos
    Then Esperar que se haya cargado la página y volver al registro
    And Esperar 2 segundos

    And Verificar el TitleText con el texto "Regístrate gratis para escuchar."

    Given Hacer click sobre el botón Register_FB
    Then Cambiar a la nueva ventana "FaceBook"
    And Esperar 3 segundos
    And Cerrar el driver y hacer foco en la ventana "Principal"
    And Verificar el TitleTextSub con el texto "Registrarte con tu correo electrónico"

    Given Introducir el valor rmunguia77@gmail.com en el campo Email
    And Verificar el EmailText con el texto "¿Cuál es tu correo electrónico?"

    And Informar el valor rmunguia77@gmail.com en el campo EmailConfirm
    And Verificar el EmailConfirmText con el texto "Confirma el correo electrónico"

    And Informar el valor Udemy2020 en el campo Password
    And Verificar el PasswordText con el texto "Crea una contraseña"

    And Informar el valor Rubén Munguía en el campo Name
    And Verificar el NameText con el texto "¿Cómo quieres que te llamemos?"

    And Verificar el DateBirthText con el texto "¿Cuál es tu fecha de nacimiento?"

    And Informar el valor 3 en el campo BirthDay
    And Seleccionar el valor Enero en el campo BirthMonth
    And Informar el valor 1986 en el campo BirthYear

    And Verificar el GenderText con el texto "¿Cuál es tu género?"

    And Hacer click sobre la opción Male
    And Verificar el MaleText con el texto "Hombre"

    And Hacer click sobre la opción Female
    And Verificar el FemaleText con el texto "Mujer"

    And Hacer click sobre la opción Binary
    And Verificar el BinaryText con el texto "No binario"

    And Verificar el MarketingText con el texto "Compartir mis datos de registro con los proveedores de contenidos de Spotify para fines de marketing. Ten en cuenta que tus datos pueden ser transferidos a un país de fuera del EEE, tal y como se recoge en nuestra Política de Privacidad."
    And Hacer click sobre el Check box MarketingCheck

    Given Hacer click sobre el link "TermsLink"
    Then Cambiar a la nueva ventana "Terms"
    And Esperar 3 segundos
    And Verificar el TermsText con el texto "Términos y Condiciones de Uso de Spotify"
    And Cerrar el driver y hacer foco en la ventana "Principal"

    Given Hacer click sobre el link "PolicyLink"
    Then Cambiar a la nueva ventana "Policy"
    And Esperar 3 segundos
    And Verificar el PolicyText con el texto "Política de Privacidad de Spotify"
    And Cerrar el driver y hacer foco en la ventana "Principal"

    And Hacer click sobre el botón RegisterButton

    Then Verificar el error Err_Captcha con el texto "Confirma que no eres un robot."

    And Verificar el AccountText con el texto "¿Ya tienes cuenta? Inicia sesión."
    And Hacer click sobre el link "IntroLink"

    Then Hacer screenshot Spotify_Full

    Then Cerrar la APP
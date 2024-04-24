import sender_stand_request
import data


# Función para obtener el cuerpo de la solicitud del kit de producto
def get_kit_body(kit_name, auth_token):
    # Crear una copia de los encabezados para no modificar el original
    header_copy = data.header.copy()
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit_body["name"] = kit_name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_kit_body, header_copy


# Función para obtener el token de autenticación de un nuevo usuario
def get_new_user_token():
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable user_response
    response_new_user = sender_stand_request.post_new_user(data.user_body)
    # Extrae el auth_token de registro de nuevo usuario
    user_token = response_new_user.json().get('authToken')
    return user_token


# Función para afirmar positivamente la creación de un kit de producto
def positive_assert(kit_name, auth_token):
    # Obtener el cuerpo de la solicitud y los encabezados actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Verificar que el campo 'name' en la respuesta coincide con el enviado
    assert kit_response.json()["name"] == kit_name


def negative_assert_no_name(kit_name, auth_token):
    # Obtener el cuerpo de la solicitud y los encabezados actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    # El resultado se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "No se enviaron todos los parámetros requeridos"


def negative_assert_symbol(kit_name, auth_token):
    # Obtener el cuerpo de la solicitud y los encabezados actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    # El resultado se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                             "Los nombres solo pueden contener caracteres latinos,  " \
                                             "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


# Prueba 1.
def test_1_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("a", auth_token)


# Prueba 2.
def test_2_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC",
        auth_token)


def test_3_not_create_kit_0_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    negative_assert_no_name("", auth_token)


def test_4_not_create_kit_512_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    negative_assert_symbol(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",
        auth_token)


def test_5_create_kit_has_special_symbol_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("\"№%@\",", auth_token)


def test_6_create_kit_has_space_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(" A Aaa ", auth_token)


def test_7_create_kit_has_number_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("123", auth_token)


def test_8_create_kit_no_string_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_symbol({}, auth_token)


def test_9_create_kit_has_dic_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_symbol({"name": 123}, auth_token)

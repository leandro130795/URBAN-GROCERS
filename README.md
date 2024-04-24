# Proyecto Urban Grocers 

en este proyecto llamado urban grocers, se trabajo con APIS, automatizando pruebas en base a un checklist y ejecutando dichas pruebas para obtener las respuestas de las solicitudes y asi poder visualizar que el software tenga el menor numero de errores para su funcionalidad.



#configuration:

Este código define tres variables en Python:

URL_SERVICE: Esta variable almacena la URL base del servicio web al que el código realizará solicitudes. En este caso, la URL parece ser "https://cnt-73cad980-b824-4dcc-a5ff-1f812c3186a3.containerhub.tripleten-services.com". Es importante destacar que esta es la URL base y otras rutas de la API se concatenarán a esta URL para formar las URL completas para diferentes endpoints.
CREATE_USER_PATH: Esta variable almacena la ruta de la API para crear un nuevo usuario en el servicio web. En este caso, parece ser "/api/v1/users". Esta ruta se unirá a la URL_SERVICE para formar la URL completa para el endpoint de creación de usuarios.
KITS_PATH: Esta variable almacena la ruta de la API para crear un nuevo kit de producto en el servicio web. En este caso, parece ser "/api/v1/kits". Al igual que con CREATE_USER_PATH, esta ruta se unirá a la URL_SERVICE para formar la URL completa para el endpoint de creación de kits de productos.
En resumen, estas variables proporcionan las URL y las rutas necesarias para acceder a los diferentes endpoints del servicio web al que el código se conectará.


#data:

Este código define varias variables en Python que contienen datos que probablemente se utilizarán en las solicitudes al servicio web:

header: Esta variable es un diccionario que define los encabezados de la solicitud HTTP. En este caso, solo contiene un encabezado "Content-Type" con el valor "application/json", lo que indica que el cuerpo de la solicitud será JSON.
user_body: Este diccionario contiene los detalles de un usuario, como el nombre ("firstName"), el número de teléfono ("phone") y la dirección ("address"). Estos datos probablemente se utilizarán para crear un nuevo usuario en el servicio web.
kit_body: Este diccionario contiene los detalles de un kit de producto, en este caso, solo el nombre ("name"). Los demás detalles del kit podrían añadirse aquí, como la descripción, el precio, etc.
token: Este diccionario contiene un token de autenticación ("authToken"). Este token probablemente se utilizará para autenticar las solicitudes al servicio web, permitiendo al servidor verificar la identidad del cliente y autorizar sus acciones.
En resumen, estas variables contienen datos necesarios para realizar solicitudes al servicio web, como los detalles del usuario que se creará, los detalles del kit de producto que se agregará y el token de autenticación necesario para acceder a recursos protegidos.


#sender_stand_request:

Este código Python se encarga de realizar dos solicitudes HTTP POST a un servicio web utilizando la biblioteca requests. Aquí está la explicación línea por línea:
Se importan los módulos necesarios: requests para realizar solicitudes HTTP, configuration para obtener las configuraciones del servicio, y data para acceder a los datos necesarios para las solicitudes.
Se define una función llamada post_new_user que toma un argumento body, que probablemente contenga los detalles del nuevo usuario a crear. La función realiza una solicitud POST al servicio web utilizando la URL y la ruta de creación de usuario proporcionadas por configuration. El cuerpo de la solicitud se establece como JSON utilizando el argumento json=body, y los encabezados se toman del módulo data.
Se define una función llamada post_new_client_kit que toma dos argumentos: bodykit, que probablemente contenga los detalles del nuevo kit de producto, y token, que es un token de autorización. La función realiza una solicitud POST al servicio web utilizando la URL y la ruta de creación de kits de producto proporcionadas por configuration. El cuerpo de la solicitud se establece como JSON utilizando el argumento json=bodykit, y se agregan los encabezados de la solicitud, que incluyen el tipo de contenido y el token de autorización.
Se realiza una llamada a la función post_new_client_kit con los datos del kit (data.kit_body) y el token de autenticación (data.token). La respuesta del servidor se almacena en la variable response.
En resumen, este código envía dos solicitudes HTTP POST al servicio web: una para crear un nuevo usuario y otra para crear un nuevo kit de producto, utilizando las configuraciones y los datos proporcionados en los módulos configuration y data.


#create_kit_name_kit_test.py:

Este código Python parece ser un conjunto de pruebas (tests) unitarias para probar la funcionalidad de crear kits de producto en un servicio web. Aquí está la explicación línea por línea:
Importa los módulos necesarios. sender_stand_request probablemente contiene funciones para enviar solicitudes HTTP al servicio web, y data probablemente contiene datos necesarios para las pruebas.
Define una función get_kit_body que se utiliza para obtener el cuerpo de la solicitud para crear un nuevo kit de producto. Toma el nombre del kit y el token de autenticación como parámetros. Actualiza el nombre del kit en el cuerpo de la solicitud con el nombre proporcionado y devuelve el cuerpo de la solicitud y una copia de los encabezados.
Define una función get_new_user_token que se utiliza para obtener un token de autenticación de un nuevo usuario. Realiza una solicitud para crear un nuevo usuario utilizando la función post_new_user del módulo sender_stand_request, y luego extrae y devuelve el token de autenticación del cuerpo de la respuesta.
Define una función positive_assert que se utiliza para afirmar positivamente la creación de un kit de producto. Utiliza la función get_kit_body para obtener el cuerpo de la solicitud y los encabezados actualizados. Luego, realiza una solicitud para crear un nuevo kit utilizando la función post_new_client_kit del módulo sender_stand_request. Verifica que la respuesta tenga un código de estado 201 (indicando éxito) y que el nombre del kit en la respuesta coincida con el nombre proporcionado.
Define una función negative_assert_no_name que se utiliza para afirmar negativamente la creación de un kit de producto cuando no se proporciona un nombre. Verifica que la respuesta tenga un código de estado 400 (indicando un error de solicitud) y que el cuerpo de la respuesta contenga un mensaje adecuado.
Las siguientes funciones (negative_assert_symbol, test_1_create_kit_1_letter_in_name_get_success_response, etc.) parecen ser pruebas unitarias específicas que prueban diferentes casos de uso para la creación de kits de productos y verifican si las respuestas del servidor son las esperadas en cada caso. Estas pruebas se ejecutarán para verificar si la funcionalidad de crear kits de producto en el servicio web funciona como se espera en diferentes escenarios.

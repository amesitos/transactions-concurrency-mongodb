import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from getpass import getpass

def conectar_atlas():

    """
    Solicita al usuario su cadena de conexión (con <db_password>)
    y su contraseña de forma segura. Luego construye la URI final,
    crea el cliente y prueba la conexión con un ping.

    Retorna:
        client (MongoClient): cliente conectado si la conexión es exitosa.
        None: si ocurre algún error durante la conexión.
    """

    # 1. Solicitar URI con marcador <db_password>
    print("Por favor, ingresa tu cadena de conexión de MongoDB Atlas:")
    uri_template = input()

    # 2. Solicitar contraseña de forma segura (no se muestra)
    print("Ahora, ingresa tu contraseña de MongoDB Atlas:")
    password = getpass()

    # 3. Construir la URI final
    uri = uri_template.replace("<db_password>", password)

    # 4. Crear cliente
    client = MongoClient(uri, server_api=ServerApi('1'))

    # 5. Probar conexión
    try:
        client.admin.command("ping")
        print("\n¡Ping exitoso! Conexión establecida con MongoDB Atlas.")
        return client

    except Exception as e:
        print("\n❌ Error de conexión:")
        print(e)
        return None

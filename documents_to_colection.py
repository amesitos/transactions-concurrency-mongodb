
def insertar_documentos(collection):
    """
    Inserta una lista de documentos predefinidos en la colección indicada.
    
    Parámetros:
        collection (Collection): La colección donde se insertarán los documentos.
    
    Retorna:
        inserted_ids (list): Lista con los IDs generados.
    """

    documentos = [
        {
            "nombre": "María González",
            "edad": 25,
            "ciudad": "Buenos Aires",
            "intereses": ["fotografía", "viajes", "café"]
        },
        {
            "nombre": "Luis Fernández",
            "edad": 29,
            "ciudad": "Quito",
            "intereses": ["cine", "senderismo", "música clásica"]
        },
        {
            "nombre": "Carla Ruiz",
            "edad": 35,
            "ciudad": "Santiago",
            "intereses": ["emprendimiento", "cocina", "lectura"]
        },
        {
            "nombre": "Daniel Soto",
            "edad": 42,
            "ciudad": "CDMX",
            "intereses": ["fútbol", "historia", "tecnología"]
        },
        {
            "nombre": "Ana López",
            "edad": 20,
            "ciudad": "Lima",
            "intereses": ["anime", "dibujo digital", "gaming"]
        }
    ]

    resultado = collection.insert_many(documentos)
    print("Documentos insertados con IDs:")
    print(resultado.inserted_ids)

    return resultado.inserted_ids

import h5py

# Ruta al archivo .h5
file_path = 'my_model.h5'

# Abrir el archivo .h5
with h5py.File(file_path, 'r') as f:
    # Imprimir la estructura del archivo .h5
    print("Estructura del archivo:")
    print("----------------------")
    print(f)
    print()

    # Recorrer los grupos y conjuntos de datos en el archivo
    def print_h5_item(name, obj):
        print(name)
        print("    Tipo:", type(obj))
        if isinstance(obj, h5py.Group):
            print("    Contenido:", list(obj.keys()))
        elif isinstance(obj, h5py.Dataset):
            print("    Forma:", obj.shape)
            print("    Tipo de datos:", obj.dtype)
    f.visititems(print_h5_item)

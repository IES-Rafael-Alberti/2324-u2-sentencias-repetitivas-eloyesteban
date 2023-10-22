from src.ejercicio9 import verificar_contraseña

def test_verificar_contraseña():
    assert verificar_contraseña("contraseña") == "Contraseña correcta"
    
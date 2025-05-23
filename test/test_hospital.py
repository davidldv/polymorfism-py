from controller.hospital_controller import HospitalController
from model.hospital import Hospital

def test_creacion():
    c = HospitalController()
    h = Hospital("San José", "Calle 10 #5-20")
    c.crear(h)
    assert c.obtener_por_id("San José") == h

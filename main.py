from clases.herencia1.taxi import Taxi
from clases.herencia1.auto_particular import AutoParticular

def main():
    coche = Taxi("123-3","la ferrari",3500,"384-a")
    print("************")
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()

    ap= AutoParticular("123","santiago",19,"bmw","blanco","234-A")
    print(ap)
    
    ap.subirseAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajandoAuto()

if __name__=='__main__':
    main()
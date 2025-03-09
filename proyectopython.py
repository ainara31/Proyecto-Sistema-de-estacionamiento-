import time  
import datetime  
import logging  

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calcular_monto():
    PRECIO_POR_HORA = 20

    while True:
        print("\nMonto por hora: $20")
        try:
            entrada = int(input("Hora de ingreso (Formato 24h, solo la hora): "))
            salida = int(input("Hora de salida (Formato 24h, solo la hora): "))

            if salida < entrada:
                print("⚠ Error: La hora de salida no puede ser menor que la de ingreso.")
                logging.warning("Intento con hora de salida menor a la de ingreso.")
                continue

            precio = (salida - entrada) * PRECIO_POR_HORA
            print(f"💰 El monto a pagar es de: ${precio}\n")

        
            logging.info(f"Cálculo realizado: Entrada {entrada}h, Salida {salida}h, Monto ${precio}")

        except ValueError:
            print("❌ Error: Ingrese solo números enteros válidos.")
            logging.error("Error de entrada: Se ingresó un valor no numérico.")
            continue

        finalizar = input("Para finalizar, escriba '2'. Para continuar, presione Enter: ")
        if finalizar.strip() == '2':
            print("👋 Espero haberte ayudado. ¡Hasta luego!")
            time.sleep(1)
            break

if __name__ == "__main__":
    calcular_monto()
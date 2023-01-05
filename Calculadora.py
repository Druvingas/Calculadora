
def entradaDatos():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    datoCorrecto = True

    while(datoCorrecto):    
        operacion = input("Ingrese la operación a realizar: (+,-,*,/)")

        if operacion == "+":
            resultado = suma(numero1,numero2)
            datoCorrecto = False
        
        elif operacion == "-":
            resultado = resta(numero1,numero2)
            datoCorrecto = False

        elif operacion == "*":
            resultado = mult(numero1,numero2)
            datoCorrecto = False
        
        elif operacion == "/":
            resultado = div(numero1,numero2)
            datoCorrecto = False
        
        else:
            print("operacion no valida")

        if datoCorrecto == False:
            print(resultado)
        

def suma(numero1,numero2):
    return numero1 + numero2

def resta(numero1,numero2):
    return numero1 - numero2

def mult(numero1,numero2):
    return numero1 * numero2

def div(numero1,numero2):
    if numero1 == 0 or numero2 == 0:
        print("Ingrese un número diferente a cero")
    
    else:
        return numero1 / numero2






if __name__=="__main__":
    entradaDatos()    
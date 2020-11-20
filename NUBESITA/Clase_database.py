import mysql.connector
from cliente import Cliente


class Database:
        
        def __init__(self):
                super(Database, self).__init__()
                self.cnn = mysql.connector.connect(host="localhost", user="root", passwd = "soniteamo", database = "sistemas_distribuidos")
                
        def pedirNumeroEntero(self):
                correcto=False
                num=0

                while(not correcto):
                    try:
                        num = int(input("Introduce un numero entero: "))
                        correcto=True
                    except ValueError:
                        print('Error, introduce un numero entero')
                     
                return num

        def registroCliente(self):
                print()
                print("**************BIENVENIDO AL REGISTRO***************")
                print()
                nombre = input("Nombres: ")
                apellido = input("Apellidos: ")
                usuario = input ("login : ")
                password = input ("Password : ")
                edad = input ("Edad : ")
                genero = input ("genero : ")

                variable = Database()
                variable.insertar_cliente(nombre, apellido, usuario, password, edad, genero)

        def inicioSesion(self):
                print()
                print("**************BIENVENIDO AL INICIO DE SESION***************")
                print()
                bandera=False
                usuario = (input ("User : "),)
                password = (input ("Password : "),)
                cur = self.cnn.cursor()
                cur.execute("SELECT User FROM clientes")
                datosos = cur.fetchall()
                cur.execute("SELECT Password FROM clientes")
                datososcontra = cur.fetchall()
                for i in range(0,len(datosos)):
                        if usuario == datosos[i] and password == datososcontra[i]:
                                bandera=True
                                c = Cliente()
                                c.owner = str(usuario)
                                print("BIENVENIDO " + c.owner )
                                c.wait_message()
                        else:
                                if i == (len(datosos)-1) and bandera==False:
                                        print("DATOS INCORRECTOS")
                                
                        
        def insertar_cliente(self,Nombres, Apellidos, User, Password, Edad, Genero):
                cur = self.cnn.cursor()
                sql='''INSERT INTO clientes (Nombres, Apellidos, User, Password, Edad, Genero) 
                VALUES('{}', '{}', '{}', '{}','{}','{}')'''.format(Nombres, Apellidos, User, Password, Edad, Genero)
                cur.execute(sql)
                self.cnn.commit()    
                cur.close()
                print("El registro fue exitoso")

                
        def desmenusadito(self):
                        
                salir = False
                opcion = 0
         
                while not salir:
                         
                        print ("1. Registrarse")
                        print ("2. Iniciar Sesion")
                        print ("3. Salir")
                             
                        print ("Elige una opcion")
                        
                        op = Database() 
                        opcion = op.pedirNumeroEntero()
                         
                        if opcion == 1:
                            print()
                            op.registroCliente()
                            print()
                        elif opcion == 2:
                            print()
                            op.inicioSesion()
                            print()
                        elif opcion == 3:
                            salir = True
                        else:
                            print ("Introduce un numero entre 1 y 3")
                print()         
                print ("Fin")

if __name__ == "__main__":
        d = Database()
        d.desmenusadito()

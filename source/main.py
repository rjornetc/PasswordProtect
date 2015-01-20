from password import Password
import database as Database
from Crypto import Random
import os
import os.path


def main():

	if not os.path.exists("./iv.dat"):
		iv = file("iv.dat","w")
		iv.write(Random.get_random_bytes(8))
		iv.close()


	while True:		
		print "1. Encriptar contrasena y guardar en BBDD"
		print "2. Desencriptar contrasena de la BBDD"
		print "0. Salir"
		print
		print "Selecciona una accion: "
		seleccion = input("> ")

		if seleccion == 0:
			break
		elif seleccion == 1:
			with open ("iv.dat","r") as myfile:
				bb=myfile.read()
			servicio = raw_input("Servicio: ")
			usuario = raw_input("Usuario del servicio: ")			
			passwd = raw_input("Contrasena: ")
			print servicio, usuario, passwd, "es correcto? (y/n) "
			check = raw_input("> ")
			if check == "y" or check == "Y" or check == "yes" or check == "Yes" or check == "YES":
				pass
			elif check == "n" or check == "N" or check == "No" or check == "no" or check == "NO":
				print
				print
				main()
			else:
				print "Introduce una opcion valida"
				print
				print
				main()
			passwd1 = Password(usuario,servicio,passwd)
			print "Encriptando..."
			print passwd1.encrypt(bb)
			print "Creando registro en la base de datos..."
			query = "INSERT INTO passwords (User,Password,Service) VALUES ('{}','{}','{}')".format(usuario,passwd1.encrypt(bb),servicio)
			Database.run_query(query)
			print
			print
		elif seleccion == 2:
			with open ("iv.dat","r") as myfile:
				bb=myfile.read()
			servicio = raw_input("Servicio: ")
			usuario = raw_input("Usuario del servicio: ")
			query = "SELECT Password FROM passwords WHERE User='{}' AND Service='{}';".format(usuario,servicio)			
			resultado = Database.run_query(query)
			print resultado
			Database.run_query(query)
			if resultado == None:
				print "No se ha encontrado nada en la base de datos"								
			else:
				for passwd in resultado:
					if len(usuario) < 16:
						usuario += ' ' * (16-len(usuario))
					passwd2 = Password(usuario,servicio,passwd[0])
					passwdf = passwd2.decrypt(bb)
				print "Contasena: " , passwdf
			print
			print

if __name__ == '__main__':
	print "**********PassProtect**********"
	print
	main()




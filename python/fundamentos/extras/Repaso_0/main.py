from usuario import Usuario

while True:

    print("\n==============================")
    print("     SISTEMA DE USUARIOS")
    print("==============================")
    print("1. Iniciar sesión")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        u = Usuario()

        datos = u.iniciar_sesion(usuario, password)

        if datos is None:
            print("\nUsuario o contraseña incorrectos.\n")

        else:

            id_usuario = datos[0]
            nombre = datos[1]
            tipo = datos[3]

            # ===========================
            # MENÚ ADMINISTRADOR
            # ===========================

            if tipo == "ADMIN":

                while True:

                    print("\n==============================")
                    print("Bienvenido Administrador:", nombre)
                    print("==============================")
                    print("1. Registrar usuario")
                    print("2. Listar usuarios")
                    print("3. Buscar usuario")
                    print("4. Modificar usuario")
                    print("5. Eliminar usuario")
                    print("6. Cerrar sesión")

                    op = input("Seleccione una opción: ")

                    if op == "1":

                        nuevo_usuario = input("Usuario: ")
                        nueva_password = input("Contraseña: ")

                        print("1. ADMIN")
                        print("2. USER")

                        tipo_usuario = int(input("Tipo: "))

                        nuevo = Usuario(
                            usuario=nuevo_usuario,
                            password=nueva_password,
                            tipo=tipo_usuario
                        )

                        nuevo.crear_usuario()

                        print("\nUsuario registrado correctamente.")

                    elif op == "2":

                        lista = u.listar_usuarios()

                        print("\n------------------------------")
                        print("ID\tUSUARIO\tTIPO")
                        print("------------------------------")

                        for fila in lista:
                            print(f"{fila[0]}\t{fila[1]}\t{fila[2]}")

                    elif op == "3":

                        id_buscar = int(input("Ingrese el ID del usuario: "))

                        dato = u.buscar_usuario(id_buscar)

                        if dato:

                            print("\n===== DATOS DEL USUARIO =====")
                            print("ID:", dato[0])
                            print("Usuario:", dato[1])
                            print("Contraseña:", dato[2])
                            print("Tipo:", dato[3])

                        else:

                            print("\nUsuario no encontrado.")

                    elif op == "4":

                        id_modificar = int(input("ID del usuario: "))

                        usuario_nuevo = input("Nuevo usuario: ")
                        password_nueva = input("Nueva contraseña: ")

                        print("1. ADMIN")
                        print("2. USER")

                        tipo_nuevo = int(input("Nuevo tipo: "))

                        modificar = Usuario(
                            id=id_modificar,
                            usuario=usuario_nuevo,
                            password=password_nueva,
                            tipo=tipo_nuevo
                        )

                        modificar.modificar_usuario()

                        print("\nUsuario modificado correctamente.")

                    elif op == "5":

                        id_eliminar = int(input("ID del usuario a eliminar: "))

                        u.eliminar_usuario(id_eliminar)

                        print("\nUsuario eliminado correctamente.")

                    elif op == "6":

                        print("\nSesión cerrada.")
                        break

                    else:

                        print("\nOpción inválida.")

            # ===========================
            # MENÚ USUARIO
            # ===========================

            else:

                while True:

                    print("\n==============================")
                    print("Bienvenido:", nombre)
                    print("Tipo de usuario: USER")
                    print("==============================")
                    print("1. Cerrar sesión")

                    op = input("Seleccione una opción: ")

                    if op == "1":

                        print("\nSesión cerrada.")
                        break

                    else:

                        print("\nOpción inválida.")

    elif opcion == "2":

        print("\nPrograma finalizado.")
        break

    else:

        print("\nOpción inválida.")
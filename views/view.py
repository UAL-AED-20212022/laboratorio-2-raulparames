from controllers.controller import *


def run():
    try:
        while True:
            scan = input().split()
            match scan[0].upper():
                case "RPI":
                    inserir_inicio(scan, lista)
                case "RPF":
                    inserir_fim(scan)
                case "RPDE":
                    inserir_depois(scan)
                case "RPAE":
                    inserir_antes(scan)
                case "RPII":
                    inserir_indice(scan)
                case "VNE":
                    print(f"O número de elementos são {verificar_numero()}")
                case "VP":
                    if not verificar_pais(scan) or verificar_pais(scan) is None:
                        print(f"O país {scan[1]} não se encontra na lista.")
                    else:
                        print(f"O país {scan[1]} encontra-se na lista.")
                case "EPE":
                    x = eliminar_inicio()
                    print(f"O país {x} foi eliminado da lista")
                case "EUE":
                    x = eliminar_fim()
                    print(f"O país {x} foi eliminado da lista")
                case "EP":
                    eliminar_pais(scan)
                    if not verificar_pais(scan) or verificar_pais(scan) is None:
                        print(f"O país {scan[1]} não se encontra na lista.")
                    else:
                        print(f"O país {scan[1]} foi eliminado da lista")
                case _:
                    pass

    except:
        pass

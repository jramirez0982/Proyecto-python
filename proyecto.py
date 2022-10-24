#programa de registro academico para matricular estudiantes,cursos,con nota,final y estatus de aprobado 

lista_alumnos = ('DIEGO','SOFIA','JUAN','OMAIRA','JOSEPH','LUNA')
lista_cursos = ('PHP','PYTHON','JAVA','BLOCKCHAIN','SQL','INGLES','HABILIDADES BLANDAS')
lista_creditos= (5 , 5, 5, 6, 5, 3, 2)

def matricula(alumnos,cursos,creditos):

    contador = 0
    while contador <3:
        nombre=input('¿cual es tu nombre?:')
        if nombre in alumnos:
            print('BIENVENIDO A SU PROCESO DE MATRICULA')
            
            lista_grande =[]
            indice = 0
            for i in cursos :
                print(indice, i)
                indice += 1
            
            flag = True
            while flag :
                codigo_curso =int(input(f'Eliga el curso que desea matricular'))
                lista_grande.append([cursos[codigo_curso], creditos[codigo_curso]])
                mas = input('DESEA MATRICULAR OTRA MATERIA? S/N')
                if mas =='N' :
                    flag = False

            break        
        else:
            print('su nombre no esta en la lista')  
            contador +=1
    registro = {nombre : lista_grande}
    return registro
print(matricula(lista_alumnos,lista_cursos,lista_creditos)) 

# { nombre : [[curso1, creditos1, nota1] , [curso2, creditos2, nota2]]}
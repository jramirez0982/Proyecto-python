#programa de registro academico para matricular estudiantes,cursos,con nota,final y estatus de aprobado 
#from filecmp import DEFAULT_IGNORES


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
    #{ nombre : [[curso1, creditos1, nota1] , [curso2, creditos2, nota2]]}

    return registro

def subir_notas(registros_acad=dict, cursos=list): #Enfasis en que se va a recibir un diccionario
    # FUNCTION - UPLOAD STUDENT'S CALIIFICATION
    # QUITAR LA VALIDACION DEL CURSO
    c = 0
    for i in cursos :
        print(c,i)
        c+=1
    curso = input('ELIJA EL CURSO PARA HACER CARGUE DE NOTAS   ')
    if curso in cursos :
        for k,v in registros_acad.items() :
            for i in v :
                if i[0] == curso :
                    nota = float(input(f'Ingrese la nora final de {i[0]} del estudiante {k}   '))
                    i.append(nota)
                else :
                    pass
    else :
        print('EL CURSO NO ESTA EN LA BASE DE DATOS')
    return registros_acad
    print(registros_acad)
            
def promedio(registros_acad = dict) :
    #Calculate the media between the matters note
    # promedio = sumatoria(creditos*nota)/(sumatoria creditos)
    for k,v in registros_acad.items() :
        sum_cxn = 0 # sumatoria de credito por nota
        sum_cred = 0 # suma el total de credito
        for i in v :
            sum_cxn += i[1]*i[2]
            sum_cred += i[1]
    prom = sum_cxn/sum_cred
    print(f'{k}' - {prom})



#registros = matricula(lista_alumnos,lista_cursos,lista_creditos)
#print(registros)               
#subir_notas(registros,lista_cursos)   



promedio(subir_notas(matricula(lista_alumnos,lista_cursos,lista_creditos),lista_cursos)) 

# Programa de registro academico para matricular estudiantes, cursos, con nota, final y estatus de aprobado
# { nombre1 : [ [curso1, creditos1, nota1], [curso2, creditos2, nota2] ] }
from importlib.machinery import SourceFileLoader
#comentario


list()

lista_alumnos = ('DIEGO' ,  'JUAN' , 'OMAIRA' , 'SOFIA' , 'JOSEPH' , 'LUNA')
lista_cursos = ("PHP", "JAVA", "PYTHON", "HTML", "INGLES", "HABILIDADES BLANDAS", "SQL")
lista_creditos = (5, 5, 5, 4, 3, 2, 4)

def matricula(alumnos, cursos, creditos):
    contador = 0
    while contador<3:
        nombre=input('¿Cuál es tu nombre?:   ')
        if nombre in alumnos: 
            print('Bienvenido a su proceso de matrícula')
            lista_grande = []
            indice = 0
            for i in cursos :
                print(indice, i)
                indice += 1
            flag = True
            while flag :
                codigo_curso = int(input(f'Eliga el curso que va a matricular   '))
                lista_grande.append([cursos[codigo_curso], creditos[codigo_curso]])
                mas = input('DESEA MATRICULAR OTRA MATERIA? S/N   ')
                if mas == 'N' :
                    flag = False          
            break    
        else:
            print('Su nombre no está en la lista')
            contador += 1
    registro = {nombre : lista_grande} 
    return registro

def subir_notas(registros_acad=dict, cursos=list):
    for k,v in registros_acad.items():
        for i in v :
            nota = float(input(f'Ingrese la nota final de {i[0]} del estudiante {k}'))
            i.append(nota)
    else :
        print('ESE CURSO NO ESTÁ EN LA BASE DE DATOS')
    print(registros_acad)
    return registros_acad

def promedio(registros_acad=dict) :
    # promedio = sumatoria(creditos*nota)/sumatoria(creditos)
    lista_notas = {}
    for k,v in registros_acad.items() :
        sum_cxn = 0
        sum_cred = 0
        for i in v :
            print(i)
            sum_cxn += i[1] * i[2]
            sum_cred += i[1]
        prom = sum_cxn/sum_cred
        #print(f'{k} - {prom}')
        listado = {k : prom}
        lista_notas.update(listado)
    print(lista_notas)
    return lista_notas  

#promedio(subir_notas(matricula(lista_alumnos, lista_cursos, lista_creditos),lista_cursos))
print("")
print('**************************************************')
print('*********BIENVENIDOS A GESTION ACADEMICA**********')
print('**************************************************')

lista_matriculados = {}
while True :
    matriculados = matricula(lista_alumnos, lista_cursos, lista_creditos)
    lista_matriculados.update(matriculados)
    a = input('desea matricular otro estudiante S/N  ')
    if a == 'N' :
        break

print(lista_matriculados)

registros = subir_notas(lista_matriculados)

notas = promedio(registros)
print('******************************************************************')
print(notas)
print('***********************************************')
for name, calif in notas.items() :
        if calif >= 3.5 :
            print(f'el estudiante {name} Aprobó')
        else :
            print(f'el estudiante {name} reprobó')

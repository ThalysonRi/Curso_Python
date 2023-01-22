
#Definir valor a variável
x=1 #int
x="CFB Cursos" #string
x=15.6 #float
x=False #bool
n1=5;n2=2;x=complex(1J)


x=["Carro","Avião","Navio",1,58.3,True] #List / Array
x=("Carro","Avião","Navio",1,58.3,True) #Tupla
x[0]="Bicicleta"

#Utilizo a função print para String, mas, devido a variável "x" ser um inteiro, para pode criar um concatenar entre as strings "valor" e o valor de "x".
print("Valor: " + str(x[4]))

#É utilizado a função Type para mostrar o tipo da variável e utilizado a função "str" para poder imprimir essa informação dentro da função "print", pois, a função print aceita apenas strings.
print("Tipo: " +str(type(x)))




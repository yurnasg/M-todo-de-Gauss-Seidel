import numpy as np

A=np.matrix(input("Digite a Matriz A: "))
b=np.transpose(np.matrix(input("Digite os valores: ")))
interacoes=int(input("Digite o número de iterações: "))

'''D=np.diag(np.diag(A))

U=np.triu(A)

L=np.tril(A)

x(k+1)=(D+L)**(-1)*(-U*x(k)+b)'''

'''//create a function that returns the solution of the system of equations A*x=b using the Gauss Seil Method with the given number of iterations.'''


def gauss_seidel(A,b,interacoes):
    n=len(A)
    x=np.zeros(n)
    for i in range(interacoes):
        for j in range(n):
            soma=0
            for k in range(n):
                if k!=j:
                    soma+=A[j,k]*x[k]
            x[j]=(b[j]-soma)/A[j,j]
    return x


x=gauss_seidel(A,b,interacoes)
print("A solução é: ",x)

import numpy as np

def substituicao_regressiva(U, b):
    """
    Resolve o sistema de equações lineares Ux = b usando substituição regressiva.

    Parâmetros:
        U (numpy.ndarray): Matriz triangular superior (n x n).
        b (numpy.ndarray): Vetor coluna (n x 1).

    Retorna:
        numpy.ndarray: Vetor solução x.

    Levanta:
        ValueError: Se a matriz não for triangular superior ou possuir elementos nulos na diagonal.
    """
    # Verifica se U é uma matriz quadrada
    n, m = U.shape
    if n != m:
        raise ValueError("A matriz U deve ser quadrada.")

    # Verifica se b tem tamanho compatível
    if b.shape[0] != n or len(b.shape) != 1:
        raise ValueError("O vetor b deve ter o mesmo número de linhas que U.")

    # Verifica elementos na diagonal de U
    if np.any(np.diag(U) == 0):
        raise ValueError("A matriz U possui elementos nulos na diagonal.")

    # Inicializa o vetor solução
    x = np.zeros_like(b, dtype=float)

    # Substituição regressiva
    for i in range(n - 1, -1, -1):
        soma = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - soma) / U[i, i]

    return x

# Exemplo de uso
if __name__ == "__main__":
    # Define a matriz triangular superior e o vetor b
    U = np.array([[2, 3, 1],
                  [0, 5, 4],
                  [0, 0, 6]], dtype=float)
    b = np.array([5, 12, 18], dtype=float)

    try:
        x = substituicao_regressiva(U, b)
        print("Solução:", x)
    except ValueError as e:
        print("Erro:", e)

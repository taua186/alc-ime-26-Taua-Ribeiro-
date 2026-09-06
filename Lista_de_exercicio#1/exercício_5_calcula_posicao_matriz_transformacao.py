import math

def calcula_posicao(L1, L2, theta1, theta2):
    """
    Calcula a posição do efetuador final (\\hat{X}_U, \\hat{Y}_U).

    Parâmetros:
        L1 (float): Comprimento do elo 1 (em cm).
        L2 (float): Comprimento do elo 2 (em cm).
        theta1 (float): Ângulo da junta 1 (em graus).
        theta2 (float): Ângulo da junta 2 (em graus).

    Retorna:
        tuple: Coordenadas (\\hat{X}_U, \\hat{Y}_U) em cm com precisão de 1 casa decimal.
    """
    # Converter os ângulos para radianos
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)

    # Calcular as coordenadas do efetuador final
    XU = L1 * math.cos(theta1_rad) + L2 * math.cos(theta1_rad + theta2_rad)
    YU = L1 * math.sin(theta1_rad) + L2 * math.sin(theta1_rad + theta2_rad)

    # Retornar os valores arredondados para 1 casa decimal
    return round(XU, 1), round(YU, 1)

def calcula_matriz_transformacao(L1, L2, theta1, theta2):
    """
    Calcula a matriz de transformação homogênea T.

    Parâmetros:
        L1 (float): Comprimento do elo 1 (em cm).
        L2 (float): Comprimento do elo 2 (em cm).
        theta1 (float): Ângulo da junta 1 (em graus).
        theta2 (float): Ângulo da junta 2 (em graus).

    Retorna:
        list: Matriz de transformação homogênea 3x3.
    """
    # Calcular a posição do efetuador final
    XU, YU = calcula_posicao(L1, L2, theta1, theta2)

    # Converter os ângulos para radianos
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)

    # Calcular o ângulo total
    theta_total = theta1_rad + theta2_rad

    # Construir a matriz de transformação homogênea
    T = [
        [round(math.cos(theta_total), 3), round(-math.sin(theta_total), 3), XU],
        [round(math.sin(theta_total), 3), round(math.cos(theta_total), 3), YU],
        [0, 0, 1]
    ]

    return T

# Testes com os valores fornecidos na questão
L1 = 20.0  # cm
L2 = 15.0  # cm

theta1 = 45  # graus
theta2 = 30  # graus

# Calcular a posição
posicao = calcula_posicao(L1, L2, theta1, theta2)
print("Posição do efetuador final:", posicao)

# Calcular a matriz de transformação
matriz_transformacao = calcula_matriz_transformacao(L1, L2, theta1, theta2)
print("Matriz de transformação homogênea:")
for linha in matriz_transformacao:
    print(linha)

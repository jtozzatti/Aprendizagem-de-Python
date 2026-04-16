import time

# 1. Definimos o decorator
def cronometro(funcao_original):
    def wrapper():
        print("--- Iniciando cronometragem ---")
        inicio = time.time()
        
        funcao_original() # Aqui executamos a sua função
        
        fim = time.time()
        print(f"--- Tempo total: {fim - inicio:.4f} segundos ---")
    return wrapper

# 2. Usamos o decorator com o '@'
@cronometro
def carregar_dados():
    print("Carregando banco de dados pesado...")
    time.sleep(2) # Simulando um atraso de 2 segundos
    print("Dados carregados!")

# 3. Chamamos a função normalmente
carregar_dados()
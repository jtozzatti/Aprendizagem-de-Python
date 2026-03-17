#em resumo sem encher linguiça sao maneiras de reconhecer e corrigir o erro sem, quebrar o programa

#try tenta executar o código
#except captura o erro se acontecer

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")

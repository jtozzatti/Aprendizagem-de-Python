alunos = {
    "Joao": {"ano": "7", "media": 10},
    "Pedro": {"ano": "7", "media": 9},
    "Gabriel": {"ano": "8", "media": 9.3},
    "Leonardo": {"ano": "1 medio", "media": 7.5}
}

#Muda valor
alunos["Joao"]["media"] = 8.5

print(alunos.get("Joao"))

#Adiciona
alunos["Gabriel"] = {"ano": "8", "media": 9.3}

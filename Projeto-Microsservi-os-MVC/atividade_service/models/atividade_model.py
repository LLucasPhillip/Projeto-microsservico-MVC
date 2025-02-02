atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar', 'nota': 8},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]

class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound("Atividade não encontrada")

def criar_atividade(id_disciplina, enunciado, respostas):
    for resposta in respostas:
        if 'nota' not in resposta:
            resposta['nota'] = 0
    id_atividade = len(atividades) + 1
    nova_atividade = {
        'id_atividade': id_atividade,
        'id_disciplina': id_disciplina,
        'enunciado': enunciado,
        'respostas': respostas
    }
    atividades.append(nova_atividade)
    return nova_atividade

def atualizar_atividade(id_atividade, id_disciplina, enunciado, respostas):
    try:
        atividade = obter_atividade(id_atividade)
        atividade['id_disciplina'] = id_disciplina
        atividade['enunciado'] = enunciado
        for resposta in respostas:
            if 'nota' not in resposta:
                resposta['nota'] = 0
        atividade['respostas'] = respostas
        return atividade
    except AtividadeNotFound as e:
        raise AtividadeNotFound(f"Não foi possível atualizar. {str(e)}")

def excluir_atividade(id_atividade):
    global atividades
    atividades = [atividade for atividade in atividades if atividade['id_atividade'] != id_atividade]
    return {'mensagem': 'Atividade excluída com sucesso'}
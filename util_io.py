import json
import difflib
import os

def salvar_resposta_ia_binario(caminho_arquivo, dados, tipo_resposta =""):
    nome_com_extensao = os.path.basename(caminho_arquivo)
    nome_arquivo_sem_extensao = os.path.splitext(nome_com_extensao)[0]
    
    caminho_novo_texto_commit = f"respostas/{tipo_resposta}-{nome_arquivo_sem_extensao}.py"
    
    os.makedirs('respostas', exist_ok=True)

    with open(caminho_novo_texto_commit, 'wb') as arquivo:
        arquivo.write(dados)

def salvar_resposta_ia(caminho_arquivo, dados, tipo_resposta=""):
  nome_com_extensao = os.path.basename(caminho_arquivo)
  nome_arquivo_sem_extensao = os.path.splitext(nome_com_extensao)[0]
  
  caminho_novo_texto = f"respostas/{tipo_resposta}-{nome_arquivo_sem_extensao}.txt"
  
  os.makedirs('respostas', exist_ok=True)

  with open(caminho_novo_texto, 'w', encoding='utf-8') as arquivo:
      arquivo.write(dados)

def pegar_nome_arquivo_json(caminho_arquivo):
  nome_com_extensao = os.path.basename(caminho_arquivo)
  nome_arquivo_sem_extensao = os.path.splitext(nome_com_extensao)[0]
  return f"commits/{nome_arquivo_sem_extensao}.json"

def salvar_json(caminho_json, dados):
  with open(caminho_json, 'w', encoding='utf-8') as file:
      json.dump(dados, file, ensure_ascii=False, indent=4)

def ler_conteudo_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()
    
def calcular_diferencas(conteudo_anterior, conteudo_atual):
    diff = difflib.unified_diff(conteudo_anterior.splitlines(keepends=True),
                                conteudo_atual.splitlines(keepends=True),
                                fromfile='anterior', tofile='atual', lineterm='')
    return '\n'.join(diff)
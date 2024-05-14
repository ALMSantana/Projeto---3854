import json
import difflib
import os

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
from interface_chat import InterfaceChat
from assistente_commit import AssistenteCommit

def main():
  caminho_arquivo = "Projeto_Dados\\twitch_analytics\\data_analytics.py"
  assistente_commit = AssistenteCommit(caminho_arquivo=caminho_arquivo)
  assistente_chat = InterfaceChat(assistente_commit)
  lista_mensagens = assistente_chat.conversar("Você pode gerar uma sugestão de commit para o script data_analytics que estou enviando para você?")

  for uma_mensagem in lista_mensagens:
    print(f"\n{uma_mensagem.text.value}")

if __name__ == "__main__":
  main()
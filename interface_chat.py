from openai import OpenAI
from assistente_base import AssistenteBase
from assistente_commit import AssistenteCommit
from assistente_documentacao import AssistenteDocumentacao
from util_io import salvar_resposta_ia, salvar_resposta_ia_binario
import os

STATUS_COMPLETED = "completed"

class InterfaceChat():
  def __init__(self, assistente):
    self.chat : AssistenteBase = assistente
    self.mensagens = []
  
  def salvar_resposta(self):
    lista_respostas = []
    
    for mensagem in self.mensagens:
      if hasattr(mensagem, "text") and mensagem.text is not None:
        for annotation in mensagem.text.annotations:
          if hasattr(annotation, "file_path") and annotation.file_path is not None:
            file_id = annotation.file_path.file_id
            if file_id is not None:
              resposta_open_ai = self.chat.cliente.files.retrieve(file_id)
              arquivo_binario_dados = self.chat.cliente.files.content(resposta_open_ai.id)
              arquivo_dados = arquivo_binario_dados.read()

              salvar_resposta_ia_binario(self.chat.caminho_arquivo, arquivo_dados, "Codigo")
        lista_respostas.append(mensagem.text.value)

    dados_salvos = "".join(lista_respostas)

    if isinstance(self.chat, AssistenteCommit):
      salvar_resposta_ia(self.chat.caminho_arquivo, dados_salvos, "Commit")
    elif isinstance(self.chat, AssistenteDocumentacao):
      salvar_resposta_ia(self.chat.caminho_arquivo, dados_salvos, "Documentacao")

  def conversar(self, mensagem_usuario : str):
    self.chat.cliente.beta.threads.messages.create(
      thread_id=self.chat.thread.id,
      role="user",
      content=mensagem_usuario
    )

    run = self.chat.cliente.beta.threads.runs.create_and_poll(
      thread_id=self.chat.thread.id,
      assistant_id=self.chat.assistente.id
    )

    if run.status == STATUS_COMPLETED:
      self.mensagens = self.chat.cliente.beta.threads.messages.list(
        thread_id=self.chat.thread.id
      ).data[0].content

    self.salvar_resposta()

    return self.mensagens
  
  def apagar_assistente_completamente(self):
    self.chat.apagar_arquivo_openai()
    self.chat.apagar_thread()
    self.chat.apagar_assistente()
from openai import OpenAI
from assistente_base import AssistenteBase
import os

STATUS_COMPLETED = "completed"

class InterfaceChat():
  def __init__(self, assistente):
    self.chat : AssistenteBase = assistente
    self.mensagens = []
  
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

    return self.mensagens
  
  def apagar_assistente_completamente(self):
    self.chat.apagar_arquivo_openai(self.chat.id_arquivo)
    self.chat.apagar_thread(self.chat.thread.id)
    self.chat.apagar_assistente(self.chat.assistente.id)
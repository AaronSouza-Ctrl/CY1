#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Prova():

    def __init__(self):
        self.questoes = []
        self.respostas = []

    def mostra_Questoes(self):
        print(self.questoes)

    def mostra_Respostas(self):
        print(self.respostas)

    def armazena_Questao_Resposta(self, novaQuestao, novaResposta):
        self.questoes.append(novaQuestao)
        self.respostas.append(novaResposta)


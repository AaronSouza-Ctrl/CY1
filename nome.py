#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sobrenomeNaOrdem(nome, sobrenome1, sobrenome2):
    if len(sobrenome2) > len(sobrenome1):
        return '{} {} {}'.format(nome, sobrenome1, sobrenome2)
    else:
        return '{} {} {}'.format(nome, sobrenome2, sobrenome1)

print(sobrenomeNaOrdem('José', 'Dias', 'Saraiva'))
print(sobrenomeNaOrdem('José', 'Madureira', 'Silva'))
print(sobrenomeNaOrdem('Aaron Plínio', 'Aguiar', 'de Souza'))


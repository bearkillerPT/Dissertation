# Dissertation
This repo contains all the documents related to the making of my master thesis.

[See on Overleaf](https://www.overleaf.com/read/kgnwtrzpwtpt)

# Work reported:
## 31 OCT/22 - 30 NOV/22
it2s-mobile-app:
- Updated message format of OVSM
- Introduced the light sensor 
- Screen dedicated to sensors
- Message History (for denms)

it2s-json-broker:
- Fixed SAEMs intermediary UPER decoding of multiple applicationDataSams


## 30 SET/22 - 30 OCT/22
it2s-mobile-app: 
- Screen para visualização do estado dos sensores utilizados e devidas traduções 
- Fixes para as SVSMs - Adaptação total das mensagens para o novo formato imposto pelo jer_encoder 
- Adicionadas SAEMs e TPMs it2s-tms: - Código adaptado para receber e usar o novo formato imposto pelo jer_encoder

it2s-json-broker: 
- SAEMs e TPMs adicionadas 
- Removidos temp fixes 

## 31 JUL/22 - 30 SET/22

it2s-json-broker: 
- SAEMs e TPMs adicionadas
- Removidos temp fixes

it2s-mobile-app:
- Screen para visualização do estado dos sensores utilizados e devidas traduções
- Fixes para as SVSMs
- Adaptação total das mensagens para o novo formato imposto pelo jer_encoder
- Adicionadas SAEMs e TPMs 

it2s-tms:
- Código adaptado para receber e usar o novo formato imposto pelo jer_encoder

# Simple explanation about the packages involved:
## it2s-mobile-app
Repositório privado no gitlab do IT.
Aplicação móvel criada com React Native e Expo! É a parte principal do projeto.
## it2s-json-broker
Repositório privado no gitlab do IT.
Programa escrito em C com multithreading que consiste num compilador que traduz mensagens de uper/xml para json e é mantido por mim.
## it2s-tms
Este repositório é, agora, mantido por mim e é corresponde a este [site](https://ccam.av.it.pt). Foi criado por dois colegas do meu projeto de Engenharia Informática.
Repositório privado no gitlab do IT.

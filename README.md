# Telegram Auth Spam

Este é um script em Python que realiza requisições POST em loop para a API de autenticação do Telegram (`https://my.telegram.org/auth/send_password`). O script foi projetado para simular comportamento humano, com pausas variáveis e tratamento de erros como "Too Many Requests" ou "Sorry, too many tries".

**Atenção:** Este projeto é apenas para fins educacionais e de teste. O uso indevido pode violar os Termos de Serviço do Telegram ou leis locais. Use com responsabilidade.

## Funcionalidades
- Solicita um número de telefone do usuário.
- Envia requisições POST em loop com pausas aleatórias (5 a 15 segundos) para simular comportamento humano.
- Trata respostas do servidor:
  - Pausa de 10 minutos ao receber "Sorry, too many tries".
  - Pausa de 5 minutos ao receber erro 429 (Too Many Requests).
- Feedback claro no console sobre o status das requisições.

## Pré-requisitos
- Python 3.6 ou superior instalado.
- Biblioteca `requests` do Python.

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/pladix/SpamSms-Telegram.git
   cd SpamSms-Telegram

# Scanner de Rede com Ping Multithread em Python

Esse script faz um scanner básico na sua rede local, enviando pings para vários IPs dentro de uma faixa que você escolher.

## O que ele faz

- Pede para você digitar o IP base (ex: `192.168.1.`)
- Pede a quantidade de IPs que quer escanear (1 a 255)
- Faz ping em todos os IPs dessa faixa usando múltiplas threads pra acelerar o processo
- Mostra quais IPs responderam, o tempo do ping e o nome do host (se disponível)

## Requisitos

- Python 3.x instalado
- Rodar em Windows, Linux ou macOS (usa o comando `ping` do sistema)

## Como usar

1. Clone ou baixe o código
2. Abra o terminal e navegue até a pasta do script
3. Rode o script com:

```bash
python scan.py

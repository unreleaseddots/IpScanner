import subprocess
import platform
import socket
import time
from datetime import datetime
from threading import Thread

# Função que faz o ping no IP informado
def ping(ip):
    sistema = platform.system().lower()
    comando = ['ping', '-n', '1', ip] if 'windows' in sistema else ['ping', '-c', '1', ip]

    try:
        inicio = time.time()
        resposta = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        fim = time.time()
        tempo_resposta = round((fim - inicio) * 1000, 2)

        if resposta.returncode == 0:
            try:
                nome = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                nome = "desconhecido"
            horario = datetime.now().strftime("%H:%M:%S")
            print(f"[{horario}] {ip} respondeu em {tempo_resposta} ms - Nome: {nome}")
    except Exception as e:
        print(f"Erro ao pingar {ip}: {e}")

# Valida se o IP informado é válido e termina com ponto (ex: 192.168.1.)
def validar_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4 or partes[-1] != '':
        return False

    for parte in partes[:-1]:
        if not parte.isdigit():
            return False
        num = int(parte)
        if num < 0 or num > 255:
            return False
    return True

# Pede ao usuário para digitar o IP base até digitar corretamente
def ler_ip_base():
    while True:
        base_ip = input("Digite o IP base (ex: 192.168.1.): ").strip()
        if validar_ip(base_ip):
            return base_ip
        print("IP inválido! Use o formato: 192.168.1. (não esqueça do ponto no final)")

# Função principal que escaneia a rede com base no IP informado
def rede_scan():
    base_ip = ler_ip_base()

    while True:
        try:
            quantidade = int(input("Quantidade de IPs para escanear (1 a 255): "))
            if 1 <= quantidade <= 255:
                break
            else:
                print("Número fora do intervalo. IPs válidos vão de 1 até 255.")
        except ValueError:
            print("⚠️  Digite um número válido.")

    print(f"\n📡 Escaneando {quantidade} IP(s) a partir de {base_ip}1...\n")

    threads = []

    # Cria e inicia uma thread pra cada IP
    for i in range(1, quantidade + 1):
        ip = base_ip + str(i)
        t = Thread(target=ping, args=(ip,))
        t.start()
        threads.append(t)

    # Espera todas as threads terminarem
    for t in threads:
        t.join()

# Ponto de entrada do script
if __name__ == "__main__":
    rede_scan()

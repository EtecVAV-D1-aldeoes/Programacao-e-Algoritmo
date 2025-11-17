import random

perguntas = [
    {"id": 1, "pergunta": "Onde o projeto Arduino foi criado?",
     "alternativas": ["Estados Unidos", "Japão", "Itália", "Alemanha", "França"], "correta": "Itália"},

    {"id": 2, "pergunta": "Qual foi o principal objetivo inicial do Arduino?",
     "alternativas": ["Criar robôs industriais", "Facilitar o uso de eletrônica por iniciantes",
                      "Desenvolver computadores pessoais", "Controlar sistemas automotivos",
                      "Criar jogos de videogame"], "correta": "Facilitar o uso de eletrônica por iniciantes"},

    {"id": 3, "pergunta": "Em que ano surgiu o Arduino?",
     "alternativas": ["1995", "2005", "2015", "1988", "2020"], "correta": "2005"},

    {"id": 4, "pergunta": "O Arduino foi criado inicialmente para estudantes de qual área?",
     "alternativas": ["Medicina", "Artes e design", "Astronomia", "Direito", "Arquitetura"], "correta": "Artes e design"},

    {"id": 5, "pergunta": "Um dos criadores do Arduino foi:",
     "alternativas": ["Elon Musk", "Bill Gates", "Massimo Banzi", "Mark Zuckerberg", "Jeff Bezos"], "correta": "Massimo Banzi"},

    {"id": 6, "pergunta": "Qual é o modelo mais popular para iniciantes?",
     "alternativas": ["Arduino Mega", "Arduino Due", "Arduino Uno", "Arduino Nano Every", "Arduino Micro"], "correta": "Arduino Uno"},

    {"id": 7, "pergunta": "Qual placa possui maior quantidade de portas digitais?",
     "alternativas": ["Arduino Nano", "Arduino Pro Mini", "Arduino Mega", "Arduino LilyPad", "Arduino Leonardo"], "correta": "Arduino Mega"},

    {"id": 8, "pergunta": "Qual placa é mais indicada para projetos compactos?",
     "alternativas": ["Arduino Mega", "Arduino Uno", "Arduino Due", "Arduino Nano", "Arduino 101"], "correta": "Arduino Nano"},

    {"id": 9, "pergunta": "Qual placa é conhecida por ser costurável em tecidos?",
     "alternativas": ["Arduino Nano", "Arduino LilyPad", "Arduino Mega", "Arduino Micro", "Arduino Zero"], "correta": "Arduino LilyPad"},

    {"id": 10, "pergunta": "Qual placa possui processador ARM ao invés do ATmega?",
     "alternativas": ["Arduino Uno", "Arduino Nano", "Arduino Mega", "Arduino Due", "Arduino Pro Mini"], "correta": "Arduino Due"},

    {"id": 11, "pergunta": "Qual componente é considerado o cérebro do Arduino?",
     "alternativas": ["LED interno", "Resistor de pull-up", "Microcontrolador", "Cabo USB", "Regulador de tensão"], "correta": "Microcontrolador"},

    {"id": 12, "pergunta": "O regulador de tensão da placa serve para:",
     "alternativas": ["Ampliar sinais digitais", "Controlar portas PWM", "Estabilizar a alimentação elétrica",
                      "Programar o microcontrolador", "Converter sinal analógico para digital"], "correta": "Estabilizar a alimentação elétrica"},

    {"id": 13, "pergunta": "Qual componente permite gravar o código no Arduino via USB?",
     "alternativas": ["Processador ARM", "Conversor USB-Serial", "Resistores de proteção", "Botão de reset", "Diodo de segurança"],
     "correta": "Conversor USB-Serial"},

    {"id": 14, "pergunta": "Qual memória guarda o programa mesmo após desligar o Arduino?",
     "alternativas": ["RAM", "Cache", "ROM", "Flash", "Buffer"], "correta": "Flash"},

    {"id": 15, "pergunta": "Qual parte da arquitetura lê valores analógicos?",
     "alternativas": ["Conversor ADC", "PWM", "Porta Serial", "Oscilador", "Reset automático"], "correta": "Conversor ADC"},

    {"id": 16, "pergunta": "Portas com o símbolo '~' representam:",
     "alternativas": ["Entrada analógica", "Comunicação I2C", "Porta de alimentação", "Saída PWM", "Porta de reset"],
     "correta": "Saída PWM"},

    {"id": 17, "pergunta": "Os pinos analógicos no Arduino Uno são:",
     "alternativas": ["D0–D13", "RX–TX", "A0–A5", "P0–P7", "V0–V5"], "correta": "A0–A5"},

    {"id": 18, "pergunta": "Um pino digital pode assumir quais estados?",
     "alternativas": ["Alto, médio, baixo", "Apenas analógico", "Apenas positivos", "HIGH ou LOW", "Sinais contínuos"],
     "correta": "HIGH ou LOW"},

    {"id": 19, "pergunta": "A porta TX é usada para:",
     "alternativas": ["Medir tensão", "Enviar dados pela serial", "Gerar PWM", "Resetar a placa", "Ler sensores"],
     "correta": "Enviar dados pela serial"},

    {"id": 20, "pergunta": "O sinal PWM é utilizado para:",
     "alternativas": ["Ler sensores analógicos", "Gerar comunicação SPI", "Controlar intensidade ou velocidade",
                      "Enviar dados USB", "Medir corrente"], "correta": "Controlar intensidade ou velocidade"},

    {"id": 21, "pergunta": "Na comunicação Serial, qual parâmetro define os bits por segundo?",
     "alternativas": ["Clock interno", "Baud rate", "Paridade", "Stop bit", "Buffer"], "correta": "Baud rate"},

    {"id": 22, "pergunta": "A comunicação I2C utiliza quantos fios?",
     "alternativas": ["1", "2", "3", "4", "5"], "correta": "2"},

    {"id": 23, "pergunta": "O que descreve melhor a comunicação SPI?",
     "alternativas": ["Lenta e simples", "Apenas 1 fio", "Rápida com linhas separadas", "Sempre sem fio", "Somente para sensores"],
     "correta": "Rápida com linhas separadas"},

    {"id": 24, "pergunta": "O módulo Bluetooth HC-05 usa qual comunicação?",
     "alternativas": ["SPI", "USB", "Serial (TX/RX)", "I2C", "CAN"], "correta": "Serial (TX/RX)"},

    {"id": 25, "pergunta": "O Wi-Fi no Arduino é implementado por módulos como:",
     "alternativas": ["L298N", "ESP8266 ou ESP32", "HC-06", "LDR", "MPU6050"], "correta": "ESP8266 ou ESP32"},

    {"id": 26, "pergunta": "Qual prática aumenta a segurança?",
     "alternativas": ["Substituir fusíveis", "Mãos molhadas", "Usar resistores em LEDs",
                      "Ligar direto nos 12V", "Usar fio desencapado"], "correta": "Usar resistores em LEDs"},

    {"id": 27, "pergunta": "O que pode acontecer ao alimentar com tensão acima do recomendado?",
     "alternativas": ["Nada", "Reinicia", "Queima a placa", "Melhora o desempenho", "Desliga temporariamente"],
     "correta": "Queima a placa"},

    {"id": 28, "pergunta": "Função do resistor em série com botão?",
     "alternativas": ["Aumentar velocidade", "Estética", "Evitar curto e leituras instáveis",
                      "Aumentar tensão", "Reduzir brilho"], "correta": "Evitar curto e leituras instáveis"},

    {"id": 29, "pergunta": "Maneira segura de desligar circuito?",
     "alternativas": ["Puxar fio", "Desconectar pela fonte", "Bater na mesa", "Soprar", "Mexer com força"],
     "correta": "Desconectar pela fonte"},

    {"id": 30, "pergunta": "Por que organizar fios na protoboard?",
     "alternativas": ["Fica bonito", "Evita curto e confusão", "Aumenta velocidade",
                      "Economiza energia", "Ajuda no PWM"], "correta": "Evita curto e confusão"},

    {"id": 31, "pergunta": "Projeto típico com Bluetooth:",
     "alternativas": ["Irrigação automática", "Carrinho controlado por celular",
                      "Termômetro", "Luminária", "Relógio"], "correta": "Carrinho controlado por celular"},

    {"id": 32, "pergunta": "Uso típico de Wi-Fi no Arduino:",
     "alternativas": ["Piscar LEDs", "Controlar dispositivos via internet",
                      "Armazenar energia", "Medir apenas temperatura",
                      "Gerar PWM"], "correta": "Controlar dispositivos via internet"},

    {"id": 33, "pergunta": "Por que I2C é usado em sensores?",
     "alternativas": ["Evita curto", "Liga muitos dispositivos com poucos pinos",
                      "Só funciona com Wi-Fi", "Só funciona com bateria", "É mais rápido"],
     "correta": "Liga muitos dispositivos com poucos pinos"},

    {"id": 34, "pergunta": "Uso típico do SPI:",
     "alternativas": ["Cartões SD", "Motor simples", "Distância", "Rotação", "Luz"],
     "correta": "Cartões SD"},

    {"id": 35, "pergunta": "Aplicação de segurança com Arduino:",
     "alternativas": ["Fazer café", "Sensor PIR + alarme", "Tocar música HQ",
                      "Substituir sistemas profissionais", "Decorar"],
     "correta": "Sensor PIR + alarme"},

    {"id": 36, "pergunta": "A função setup() é executada:",
     "alternativas": ["Continuamente", "Apenas no início", "Com sensores",
                      "Quando chamada no loop()", "Quando aperta botão"],
     "correta": "Apenas no início"},

    {"id": 37, "pergunta": "A função loop():",
     "alternativas": ["Define constantes", "Executa 1 vez", "Repete continuamente",
                      "Carrega bibliotecas", "Inicia USB"], "correta": "Repete continuamente"},

    {"id": 38, "pergunta": "Estrutura mínima do Arduino:",
     "alternativas": ["setup()", "loop()", "setup() + loop()", "main()", "inic()"],
     "correta": "setup() + loop()"},

    {"id": 39, "pergunta": "Sensores complexos exigem:",
     "alternativas": ["Criar nova placa", "Bibliotecas", "Excluir setup()",
                      "Variáveis globais", "PWM"], "correta": "Bibliotecas"},

    {"id": 40, "pergunta": "#include <Servo.h> serve para:",
     "alternativas": ["Incluir biblioteca", "Variáveis locais", "Iniciar Arduino",
                      "Velocidade do servo", "PWM"], "correta": "Incluir biblioteca"},

    {"id": 41, "pergunta": "pinMode(13, OUTPUT) configura:",
     "alternativas": ["Analógico", "Entrada", "Ler valor", "Saída", "PWM"],
     "correta": "Saída"},

    {"id": 42, "pergunta": "digitalWrite(8, HIGH) faz:",
     "alternativas": ["Entrada analógica", "Nível alto", "Ler pino", "Desliga",
                      "PWM"], "correta": "Nível alto"},

    {"id": 43, "pergunta": "Função para ler valores analógicos:",
     "alternativas": ["digitalRead()", "analogRead()", "analogWrite()",
                      "pinMode()", "pwmRead()"], "correta": "analogRead()"},

    {"id": 44, "pergunta": "Serial.begin(9600) serve para:",
     "alternativas": ["Iniciar I2C", "Velocidade da serial", "Ler USB",
                      "Iniciar sensor", "PWM"], "correta": "Velocidade da serial"},

    {"id": 45, "pergunta": "delay(1000) faz o Arduino:",
     "alternativas": ["Pausar 1s", "Aumentar velocidade", "Reiniciar",
                      "Desativar periféricos", "Salvar memória"], "correta": "Pausar 1s"},

    {"id": 46, "pergunta": "HC-SR04 é usado para:",
     "alternativas": ["Temperatura", "Luz", "Distância", "Magnetismo", "Som"],
     "correta": "Distância"},

    {"id": 47, "pergunta": "Servo motor:",
     "alternativas": ["Gira livre", "Só 12V", "Sensor", "Controla posição com pulsos", "Só digital"],
     "correta": "Controla posição com pulsos"},

    {"id": 48, "pergunta": "L298N controla:",
     "alternativas": ["LEDs", "Temperatura", "Motores DC e de passo",
                      "LCD", "Bluetooth"], "correta": "Motores DC e de passo"},

    {"id": 49, "pergunta": "Ethernet Shield permite:",
     "alternativas": ["Controlar servos", "Medir RPM", "SD Card", "Rede e dados", "PWM"],
     "correta": "Rede e dados"},

    {"id": 50, "pergunta": "Um sensor LDR mede:",
     "alternativas": ["Luminosidade", "Pressão", "Som", "Vibração", "Umidade"],
     "correta": "Luminosidade"}
]


def jogar_quiz():
    pontuacao = 0
    print("\n===== QUIZ =====\n")

    perguntas_selecionadas = random.sample(perguntas, 20)
    for idx, p in enumerate(perguntas_selecionadas, start=1):

        print(f"{idx}){p['pergunta']}")

        alternativas = p["alternativas"][:]
        random.shuffle(alternativas)
        letras = ["A", "B", "C", "D", "E"]
        mapa = {letras[i]: alternativas[i] for i in range(5)}

        for letra, texto in mapa.items():
            if texto == p["correta"]:
                correta = letra
                break

        for letra in letras:
            print(f"{letra}) {mapa[letra]}")

        resp = input("Resposta (A/B/C/D/E): ").upper()

        if resp == correta:
            print("✔ Correto! (+0,5 ponto)\n")
            pontuacao += 0.5
        else:
            print(f"✘ Errado! A correta era {correta}\n")

    print(f"\nPontuação final: {pontuacao} pontos\n")


while True:
    jogar_quiz()
    if input("Jogar novamente? (S/N): ").upper() != "S":
        print("Obrigado por jogar! Até a próxima!")
        break

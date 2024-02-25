import re
import sys

class AutomatoFinitoDeterminista:
    def __init__(self):
        # Defina os estados do autômato
        self.estados = {'on', 'off', 'fim'}
        
        # Defina o alfabeto
        self.alfabeto = {'on', 'off', 'fim'}
        
        # Defina a função de transição
        self.transicoes = {
            'on': {'on': 'on', 'off': 'off', 'fim': 'fim'},
            'off': {'on': 'on', 'off': 'off', 'fim': 'fim'},
        }
        
        # Defina o estado inicial
        self.estado_inicial = 'on'
        
        # Defina os estados de aceitação
        self.estados_aceitacao = {'fim'}

    def processar_ficheiro(self, filename):
        estado_atual = self.estado_inicial
        soma = 0
        with open(filename, 'r', encoding='utf-8') as ficheiro:
            conteudo = ficheiro.read()
            palavras= (re.sub(r'[.!?]', ' ', conteudo)).split()
            #print(palavras)
            for palavra in palavras:
                if(re.match(r'on', palavra, re.I)):
                    #print(f'Change to on from {estado_atual}')
                    estado_atual = self.transicoes[estado_atual]['on']
                elif(re.match(r'off', palavra, re.I)):
                    #print(f'Change to off from {estado_atual}')
                    estado_atual = self.transicoes[estado_atual]['off']
                elif(re.match(r'^[\+-]?\d+$', palavra) and estado_atual == 'on'):
                    #print('add')
                    soma += int(palavra)
                elif(re.match(r'^=$', palavra)):
                    print(soma)
            estado_atual = 'fim'
            if(estado_atual in self.estados_aceitacao):
                return 1
            else: 
                return 0     
                    
def main(inp):
    
    afd = AutomatoFinitoDeterminista()
    if(afd.processar_ficheiro(inp[1])):
        print("Leitura concluída")
    else: print("Erro na leitura")
    
if __name__ == "__main__":
    main(sys.argv)

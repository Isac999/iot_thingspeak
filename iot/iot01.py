import urllib.request
import random
import time

#configurando API do APIkey
apiKey = "60XB4OYBJ4AHMN60"
#URL base do canal
URL = "https://api.thingspeak.com/update?api_key="+apiKey
#simulando entrada de dados (ex: sensor ambiente)
def gerar_dados() -> int:
  temperatura = random.randint(0, 45)
  umidade = random.randint(0,45)
  return temperatura, umidade
temp, umid = gerar_dados()
#concatenando o URL e as keys pra inserção dos dados nas fields (campos)
print(URL + "&field1={}&field2={}".format(temp, umid))
while True:
  try:
    temp, umid = gerar_dados()
    print('Temperatura: %s' %temp)
    print('Umidade: %s' %umid)
    conexao = urllib.request.urlopen(URL + "&field1={}&field2={}".format(temp, umid))
    conexao.close()
    print('----------------------')
    time.sleep(30)
  except:
      print('Erro')
      break
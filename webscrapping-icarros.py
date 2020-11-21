from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import re

PATH = "/usr/bin/chromedriver"
icarrosPage = webdriver.Chrome(PATH)

CatMarMod = []
def lerCSV():

    tabela = []

    with open("marcas_modelo.csv", "r") as arquivo_csv:

        leitor = csv.reader(arquivo_csv, delimiter=",")

        for coluna in leitor:
            tabela += coluna

    tabela.pop(0)
    tabela.pop(0)
    tabela.pop(0)

    return tabela
CatMarMod = lerCSV()



for i in range(len(CatMarMod)):
   try:
        categoria = CatMarMod.pop(0)
        marca = CatMarMod.pop(0)
        modelo = CatMarMod.pop(0)

        icarrosUrl = ('https://www.icarros.com.br/'+marca+'/'+modelo+'/2021/opiniao-do-dono') 
            
   except:
       pass

# icarrosUrl = ('https://www.icarros.com.br/'+marca+'/'+modelo+'/2021/opiniao-do-dono')
icarrosPage.get("https://www.icarros.com.br/chevrolet/onix/2021/opiniao-do-dono")


categoria = ""
marca = icarrosPage.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/h1/span[1]').text
#print(marca)

modelo = icarrosPage.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/h1/span[2]').text
#print(modelo)

ano = icarrosPage.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/h1/span[3]').text
#print(ano)

valor = icarrosPage.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/span').text
valor = int(re.sub('[^0-9]', '', valor))
#print(valor)

pontuacaoTotal = icarrosPage.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/section/div/span[1]').text
pontuacaoTotal = float(pontuacaoTotal.replace(',','.'))
#print(pontuacaoTotal)

ptConfortoAcabamento = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[1]/div[1]').text
ptConfortoAcabamento = float(ptConfortoAcabamento.replace(',','.'))
#print(ptConfortoAcabamento)

ptConsumo = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[2]/div[1]').text
ptConsumo = float(ptConsumo.replace(',','.'))
#print(ptConsumo)

ptCustoBeneficio = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[3]/div[1]').text
ptCustoBeneficio = float(ptCustoBeneficio.replace(',','.'))
#print(ptCustoBeneficio)

ptDesign = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[4]/div[1]').text
ptDesign = float(ptDesign.replace(',','.'))
#print(ptDesign)

ptDirigibilidade = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[5]/div[1]').text
ptDirigibilidade = float(ptDirigibilidade.replace(',','.'))
#print(ptDirigibilidade)

ptManutencao = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[6]/div[1]').text
ptManutencao = float(ptManutencao.replace(',','.'))
#print(ptManutencao)

ptPerfomance = icarrosPage.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/section/div[2]/div/div[6]/div[1]').text
ptPerfomance = float(ptPerfomance.replace(',','.'))
#print(ptPerfomance)
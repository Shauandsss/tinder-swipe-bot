from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from secrets import username, password
import pandas as pd
import pickle
from selenium.webdriver.common.action_chains import ActionChains
import datetime as strftime


class TinderBot():

    def savecook(self):
        pickle.dump(self.driver.get_cookies() , open("cookies.pkl","wb"))
        

    def load_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://notifica.saude.gov.br/notificacoes/form-notificacao')   
        

    def login(self):
        print('x')

        self.driver.get('https://notifica.saude.gov.br/notificacoes/form-notificacao')   

        estadotexto = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[21]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li/div/a').text
        #if estadotexto != estado:
        #    xiscampo = bot.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[21]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div/div[1]/div/i')               
        #    xiscampo.click()
        #or
        #clear

        #sendkeys estado[0]

        #sc.click()

                                              
        scx = bot.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[21]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li[23]/div/a')
        sc = bot.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[21]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li/div/a')                                        

                                                  
        cidade = bot.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[22]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li[1]/div/a')

    def excluir(self):
        Dados = pd.read_excel(r'C:\Users\Administrator\Desktop\e-Sus\Relação_Excluir.xlsx')
    
        for i in range(0,100):
            nNotif = Dados['Notif'][i]
            searchbar = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-lista-notificacoes/ion-content/div[2]/grid-padrao-notificacao/div/section[1]/div[1]/ion-searchbar/div/input')
            while(not(searchbar.is_displayed())):
                sleep(0.5)
            
            searchbar.send_keys(str(nNotif))
            searchbar.send_keys(Keys.ENTER)

            sleep(1)
            opt = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-lista-notificacoes/ion-content/div[2]/grid-padrao-notificacao/div/section[2]/div[2]/div[2]/div/ion-button')
            while(not(opt.is_displayed())):
                sleep(0.5)
            opt.click() 
            sleep(0.5)
            cancel = self.driver.find_element_by_xpath('//*[@id="ion-overlay-4"]/div/div[2]/modal-acoes-grid-notificacoes/ion-list/ion-item[1]')
            while(not(cancel.is_displayed())):
                sleep(0.5)
            sleep(0.5)
            cancel.click()

            cancel2 = self.driver.find_element_by_xpath('//*[@id="ion-overlay-5"]/div/div[3]/button[2]') 
            while(not(cancel2.is_displayed())):
                sleep(0.5)
            sleep(0.5)
            cancel2.click()


    def campos(self):
        Dados = pd.read_excel(r'C:\Users\Administrator\Desktop\e-Sus\Relação_Xaxim.xlsx')
        quantidade = 100
        i = 0
        x = 0

        nomecampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')        
        datanascampo = bot.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[10]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-input/input')
        cepcampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[15]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
        logradourocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[17]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
        numerocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[18]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
        complementocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[19]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
        bairrocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[20]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
        estadocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[21]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[1]/input')
        municipiocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[22]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[1]/input')
        dataNotifcampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[1]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-input/input')
        sinout = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[2]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-item[3]/ion-checkbox')                          
        inisincampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[4]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-input/input')
        estadotestecampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[6]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[3]/ion-checkbox')
        telefonecampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[23]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
        telefonecontcampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[24]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input') 
        sexo1campo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[12]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
        sexo2campo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[12]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[2]/ion-checkbox')
        raca1 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
        raca2 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[2]/ion-checkbox')
        raca3 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[3]/ion-checkbox')
        raca4 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[4]/ion-checkbox')
        raca5 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[5]/ion-checkbox')
        raca6 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[6]/ion-checkbox')

        xpathsexo = 0
        while(True):
            try:
                sexo1texto = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathsexo) + '-lbl"]').text
                sexo2texto = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathsexo + 1) + '-lbl"]').text
                if(sexo1texto == 'Masculino' or sexo1texto == 'Feminino'):
                    break
            except:
                xpathsexo = xpathsexo + 1
        print(sexo1texto)

        self.driver.execute_script("arguments[0].scrollIntoView()", raca1) 
        xpa = 0
        while(True):
            try:
                racatext1 = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpa) + '-lbl"]').text
                if(racatext1 == 'Branca') or (racatext1 == 'Preta') or (racatext1 == 'Parda') or (racatext1 == 'Amarela') or (racatext1 == 'Indigena') or (racatext1 == 'Ignorado'):
                    break
            except:
                xpa = xpa + 1
        print(racatext1)
        racatext2 = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpa + 1) + '-lbl"]').text
        racatext3 = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpa + 2) + '-lbl"]').text
        racatext4 = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpa + 3) + '-lbl"]').text
        racatext5 = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpa + 4) + '-lbl"]').text
        racatext6 = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpa + 5) + '-lbl"]').text

        xpathteste = 0
        estadotestecampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
        self.driver.execute_script("arguments[0].scrollIntoView()", estadotestecampo)
        estadotestecampo.click()


        teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
        while(not(teste.is_displayed())): 
            sleep(0.001) 
            teste.click()

        while(True):
            try:
                teste1text = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathteste) + '-lbl"]').text
                if(teste1text == 'TESTE RÁPIDO - ANTICORPO') or (teste1text == 'TESTE RÁPIDO - ANTÍGENO') or (teste1text == 'RT-PCR') or (teste1text == 'Enzimaimunoensaio – ELISA') or (teste1text == 'Imunoensaio por Eletroquimioluminescência – ECLIA') or (teste1text == 'Quimioluminescência - CLIA'):
                    break
            except:
                xpathteste = xpathteste + 1
                
        teste2text = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathteste + 1) + '-lbl"]')
        teste3text = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathteste + 2) + '-lbl"]')
        teste4text = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathteste + 3) + '-lbl"]')
        teste5text = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathteste + 4) + '-lbl"]')
        teste6text = self.driver.find_element_by_xpath('//*[@id="ion-cb-' + str(xpathteste + 5) + '-lbl"]')

        if teste1text == 'RT-PCR':
            teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
        elif teste2text == 'RT-PCR':
            teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[2]/ion-checkbox')
        elif teste3text == 'RT-PCR':
            teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[3]/ion-checkbox')
        elif teste4text == 'RT-PCR':
            teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[4]/ion-checkbox')
        elif teste5text == 'RT-PCR':
            teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[5]/ion-checkbox')
        elif teste6text == 'RT-PCR':
            teste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[8]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[6]/ion-checkbox')




        for i in range(0,quantidade):
            Saude = Dados['Saude'] [i]
            Seg = Dados['Seg'] [i]
            cpf = Dados['CPF'] [i]   
            try: 
                cpf_btn = self.driver.find_element_by_xpath("//*[@id='main-content']/app-form-notificacao/ion-content/div/div[2]/div/div[1]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-row/ion-col[1]/ion-item/ion-checkbox")
            except:
                while(not(cpf_btn.is_displayed())):    
                    cpf_btn = self.driver.find_element_by_xpath("//*[@id='main-content']/app-form-notificacao/ion-content/div/div[2]/div/div[1]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-row/ion-col[1]/ion-item/ion-checkbox")
                    sleep(0.001)

            if Saude == 'NÃO':
                btn_Saude = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[3]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-row/ion-col[2]/ion-item/ion-checkbox')        
                segorsau = 0
            elif Saude == 'SIM':
                btn_Saude = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[3]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-row/ion-col[1]/ion-item/ion-checkbox')
                segorsau = 1
                
        
            if Seg == 'NÃO':
                btn_Seg = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[4]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-row/ion-col[2]/ion-item/ion-checkbox')        
                segorsau = 0
            elif Seg == 'SIM':
                btn_Seg = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[4]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-row/ion-col[1]/ion-item/ion-checkbox')
                segorsau = 1
                

            if(segorsau == 1):
                cbo = Dados['CBO'][i]
                cbocampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[5]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[1]/input')
                cbocampo.send_keys(str(cbo))
                cbolista = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[5]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li/div/a')
                cbolista.click()

            cpfcampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[6]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/ion-input/input')
            cpfcampo.click()
            cpfcampo.send_keys(str(cpf))
            cpf_btn.click()

            

            nome = Dados['Nome'][i]
            sexo = Dados['Sexo'][i]
            datanas = Dados['DataNas'][i]

            try:
                datanas = Dados['DataNas'][i]    
                datanas = datanas.strftime("%d/%m/%Y")
                print(datanas)
            except:
                print('error')

            raca = Dados['Raca'][i]

            cep = Dados['CEP'] [i]
            logradouro = Dados['Logradouro'] [i]
            numero = Dados['Número'] [i]
            complemento = Dados['Complemento'] [i]
            bairro = Dados['Bairro'] [i]
            estado = Dados['Estado'] [i]
            municipio = Dados['Municipio'] [i]
            telefone = Dados['Telefone1'] [i]
            telefonecont = Dados['Telefone2'] [i]
            resultado = Dados['Teste'][i]

            
            
            
            nomecampo.click()
            btn_Saude.click()
            btn_Seg.click()


            nomecampo.clear()
            nomecampo.send_keys(nome)

            datanascampo.clear()
            datanascampo.send_keys(datanas)


            sexo1flag = sexo1campo.get_attribute('aria-checked')
            sexo2flag = sexo2campo.get_attribute('aria-checked')
            if sexo[0] == sexo1texto[0]:
                if sexo1flag == 'false':
                    sexo1campo.click()
                
            elif sexo[0] == sexo2texto[0]:
                if sexo2flag == 'false':
                    sexo2campo.click()

            raca1 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[13]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')

            self.driver.execute_script("arguments[0].scrollIntoView()", raca1)          

            if racatext1 == raca:
                raca1flag = raca1.get_attribute('aria-checked')
                if raca1flag == 'false':  
                    raca1.click()
            elif racatext2 == raca:
                raca2flag = raca2.get_attribute('aria-checked')
                if raca2flag == 'false':
                    raca2.click() 
            elif racatext3 == raca:
                raca3flag = raca3.get_attribute('aria-checked')
                if raca3flag == 'false':
                    raca3.click()  
            elif racatext4 == raca:
                raca4flag = raca4.get_attribute('aria-checked')
                if raca4flag == 'false':
                    raca4.click()  
            elif racatext5 == raca:
                raca5flag = raca5.get_attribute('aria-checked')
                if raca5flag == 'false':
                    raca5.click() 
            elif racatext6 == raca:
                raca6flag = raca6.get_attribute('aria-checked')
                if raca6flag == 'false':
                    raca6.click() 

            while(not(cepcampo.is_displayed())): 
                sleep(0.001) 

            cepcampo.click()
            cepcampo.clear()
            cepcampo.send_keys(str(cep))

            while(not(logradourocampo.is_displayed())): 
                sleep(0.001)
            logradourocampo.clear()
            logradourocampo.send_keys(logradouro)
           

            while(not(numerocampo.is_displayed())): 
                sleep(0.001)   
            numerocampo.clear()
            numerocampo.send_keys(str(numero))

    
            while(not(complementocampo.is_displayed())): 
                sleep(0.001)               
            complementocampo.clear()
            complementocampo.send_keys(complemento)  

            while(not(bairrocampo.is_displayed())): 
                sleep(0.001)  
            bairrocampo.clear()
            bairrocampo.send_keys(bairro)           
        
            while(not(estadocampo.is_displayed())): 
                sleep(0.001)  


            estadocampo.clear() 
            estadocampo.send_keys(estado)   
            sc = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[21]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li/div/a')
            sc.click()

            while(not(municipiocampo.is_displayed())): 
                sleep(0.001)        

            municipiocampo.clear()
            municipiocampo.send_keys(municipio)     
            cid = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[2]/div/div[22]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ng-autocomplete/div[1]/div[2]/ul/li[1]/div/a')
            cid.click()
            
            

            while(not(telefonecampo.is_displayed())):
                sleep(0.001)
            telefonecampo.clear()
            telefonecampo.send_keys(str(telefone))

            while(not(telefonecontcampo.is_displayed())):
                sleep(0.001) 
            telefonecontcampo.clear()
            telefonecontcampo.send_keys(str(telefonecont))

            self.driver.execute_script("arguments[0].scrollIntoView()", dataNotifcampo) 
            while(not(dataNotifcampo.is_displayed())): 
                sleep(0.001)
            dataNotif = '27/08/2020'
            dataNotifcampo.clear()
            dataNotifcampo.send_keys(dataNotif)        
            

            sin10 = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[2]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-item[10]/ion-checkbox')
            self.driver.execute_script("arguments[0].scrollIntoView()", sin10)
            while(not(sin10.is_displayed())):
                sleep(0.001)
            sin10.click()

            


            self.driver.execute_script("arguments[0].scrollIntoView()", inisincampo)                                        

            while(not(inisincampo.is_displayed())): 
               sleep(0.001)            
            inisincampo.send_keys('27/08/2020')
            
            self.driver.execute_script("arguments[0].scrollIntoView()", estadotestecampo)
            while(not(estadotestecampo.is_displayed())): 
               sleep(0.001)                   
            estadotestecampo.click()
            
                

            datacoletaflag = 1

            while(datacoletaflag == 1):
                try:                                                     
                    datacoletacampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[7]/div/ion-row/ion-col/app-campo-form/app-caixa-input/divform/app-caixa-input/div/div/div[2]/div/div[2]/ion-input/input')
                    datacoletaflag = 0
                except:
                    try:                                                   
                        datacoletacampo = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[7]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/ion-input/input')
                        datacoletaflag = 0
                    except:
                        datacoletaflag = 1
                        sleep(0.001)

            self.driver.execute_script("arguments[0].scrollIntoView()", teste)

            while(not(teste.is_displayed())): 
               sleep(0.001) 
            teste.click()

            savebtn = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[4]/ion-col[1]/ion-button[1]/ion-label')
            self.driver.execute_script("arguments[0].scrollIntoView()", savebtn)
            resultadoteste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[9]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
            if resultado[0] == 'N':
                resultadoteste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[9]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[1]/ion-checkbox')
            elif resultado[0] == 'P':
                resultadoteste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[9]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[2]/ion-checkbox')
            elif resultado[0] == 'I':
                resultadoteste = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[3]/div/div[9]/div/ion-row/ion-col/app-campo-form/app-caixa-input/div/div/div[2]/div/div[2]/div/ion-item[3]/ion-checkbox')

            while(not(resultadoteste.is_displayed())): 
               sleep(0.001) 
            resultadoteste.click()

            while(not(datacoletacampo.is_displayed())): 
               sleep(0.001)
          
            datacoletacampo.click()        
            datacoletacampo.send_keys('27/08/2020')

            savebtn = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-form-notificacao/ion-content/div/div[4]/ion-col[1]/ion-button[1]')
            self.driver.execute_script("arguments[0].scrollIntoView()", savebtn) 
            while(not(savebtn.is_displayed())): 
              sleep(0.001)                  
            savebtn.click()

            incluirflag = 1
            while(incluirflag == 1):
                try:                                                     
                   incluirbotao = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-lista-notificacoes/ion-content/div[1]/div[2]/ion-button[2]')
                   print(str(incluirbotao.is_displayed))
                   incluirbotao.click()
                   incluirflag = 0
                except:
                    incluirflag = 1
                sleep(0.001)
            
            sleep(1)


    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()

#bot.login()
bot.load_cookies()
#bot.campos()
#bot.catchData()

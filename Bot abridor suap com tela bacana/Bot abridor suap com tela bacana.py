#Bot abridor suap com tela bacana
#bot_de_login_automatico
from selenium import webdriver
from getpass import getpass
import smtplib      
import PySimpleGUI as sg


class TelaPython:
    #definindo o init, que é o consultor em python 
  def __init__(self):
    #Partes da tela
    #layout
    layout=[
    [sg.Text('URL'),sg.Input(key='endereco')],
    [sg.Text('Login'),sg.Input(key='login')],
    [sg.Text('Senha'),sg.Input(key='senha')],
    [sg.Button('Executar Bot')] 
    ]
    #Janela
    self.janela=sg.Window("Abridor automático de sites").layout(layout)
    #Extrair dados
    self.button, self.values = self.janela.Read()

    Endereço=self.values['endereco']
    Login=self.values['login']
    Senha=self.values['senha']

    driver = webdriver.Firefox()
    driver.get(Endereço)

    login_caixinha = driver.find_element_by_id('id_username')
    login_caixinha.send_keys(Login)

    senha_caixinha = driver.find_element_by_id('id_password')
    senha_caixinha.send_keys(Senha)

    botao_login = driver.find_element_by_class_name('submit-row')
    botao_login.submit()
    
  def Iniciar(self):      
    print(self.values)
tela = TelaPython()
tela.Iniciar()






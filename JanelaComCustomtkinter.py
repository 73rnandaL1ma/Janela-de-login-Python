from msilib.schema import CheckBox
import customtkinter as cust
##MUDANDO A APARENCIA DA JANELA - DEIXANDO ELA DARK
cust.set_appearance_mode("Dark") 
###COR BOTÃO DE LOGIN  (TEMA)
cust.set_default_color_theme("green")

##CRiANDO JANELA
janela = cust.CTk()
janela.geometry("500x300")
##DANDO NOME A JANELA
janela.title ("Projeto Fefe")

def clique():
 print ("Fazer Login")

texto = cust.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

###CRIANDO A ENTRADA DE EMAIL E SENHA
email = cust.CTkEntry (janela, placeholder_text_color="E-mail")
email.pack (padx = 10, pady =10)

###CRIANDO A ENTRADA DE SENHA E ADD O SHOW = (PARA NÃO MOSTRAR A SENHA AO DIGITAR)
senha = cust.CTkEntry (janela, placeholder_text_color="Senha", show ="**")
senha.pack (padx = 10, pady =10)

##CRIANDO UMA CHECKBOX (OPÇÃO DE SALVAR/LEMBRAR LOGIN)
checkbox = cust.CTkCheckBox(janela, text = "Lembrar Login")
checkbox.pack (padx= 10, pady = 10)

##ADD BOTÃO LOGIN
botao = cust.CTkButton (janela, text="Login", command= clique)
botao.pack(padx=10, pady=10)



janela.mainloop()
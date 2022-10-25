from ensurepip import version
from mailbox import NotEmptyError
import sys
from xml.dom.minidom import Element 
from PyQt5 import QtWidgets, uic
import mysql.connector as sql
from pyautogui import PRIMARY
from reportlab.pdfgen import canvas
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel



#banco de dados
banco = sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)
# senha
def senha():

    credenciais,senha = "duffhaus","salaodebeleza"
    linha1 = loguin.lineEdit.text()
    linha2 = loguin.lineEdit_2.text()
    if linha1 == "duffhaus" and linha2 == "salaodebeleza":
        interface.show()
        loguin.close()
    else:
        print("error")
#cadastro de clientes-cadastrar-ver clientes-excluir
def ver_clientes():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM usuario"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    interface.tableWidget.setRowCount(len(dados_lidos))
    interface.tableWidget.setColumnCount(4)

    for i in range(0,len(dados_lidos)):
        for j in range(0,4):
            interface.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    banco.commit()
def cadastro():
    linha1 = interface.lineEdit_10.text()#nome
    linha2 = interface.lineEdit_11.text()#telefone
    linha3 = interface.lineEdit_12.text()#data de nascimento


    cursor = banco.cursor()
    comando_sql = "INSERT INTO usuario(nome,telefone,nascimento) VALUES (%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3))
    cursor.execute(comando_sql,dados)
    banco.commit()

    interface.lineEdit_10.setText("")#nome
    interface.lineEdit_11.setText("")#telefone
    interface.lineEdit_12.setText("")#data de nascimento
def excluir_clientes():
    linha = interface.tableWidget.currentRow()
    interface.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM usuario")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM usuario WHERE id="+ str(valor_id))
    banco.commit()
#serviços cadastrar serviços feitos-organizar cada serviço em seu funcionario
def serviços_jefferson():
    linha4 = interface.lineEdit_13.text()#nome
    linha5 = interface.lineEdit_14.text()#serviço
    linha6 = interface.lineEdit_16.text()#valor
    linha7 = interface.lineEdit_15.text()#data
    
    cursor = banco.cursor()
    comando_sql = "INSERT INTO jefferson(nome,serviço,valor,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha4),str(linha5),str(linha6), str(linha7))
    cursor.execute(comando_sql,dados)
    banco.commit()
    interface.lineEdit_13.setText("")#nome
    interface.lineEdit_14.setText("")#serviço
    interface.lineEdit_16.setText("")#valor
    interface.lineEdit_15.setText("")#data
def serviços_marllon():
    linha4 = interface.lineEdit_13.text()#nome
    linha5 = interface.lineEdit_14.text()#serviço
    linha6 = interface.lineEdit_16.text()#valor
    linha7 = interface.lineEdit_15.text()#data
    
    cursor = banco.cursor()
    comando_sql = "INSERT INTO marllon(nome,serviço,valor,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha4),str(linha5),str(linha6), str(linha7))
    cursor.execute(comando_sql,dados)
    banco.commit()
    interface.lineEdit_13.setText("")#nome
    interface.lineEdit_14.setText("")#serviço
    interface.lineEdit_16.setText("")#valor
    interface.lineEdit_15.setText("")#data
def serviços_wall():
    linha4 = interface.lineEdit_13.text()#nome
    linha5 = interface.lineEdit_14.text()#serviço
    linha6 = interface.lineEdit_16.text()#valor
    linha7 = interface.lineEdit_15.text()#data
    
    cursor = banco.cursor()
    comando_sql = "INSERT INTO wallterlenia(nome,serviço,valor,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha4),str(linha5),str(linha6), str(linha7))
    cursor.execute(comando_sql,dados)
    banco.commit()
    interface.lineEdit_13.setText("")#nome
    interface.lineEdit_14.setText("")#serviço
    interface.lineEdit_16.setText("")#valor
    interface.lineEdit_15.setText("")#data
def serviços_sabrina():
    linha4 = interface.lineEdit_13.text()#nome
    linha5 = interface.lineEdit_14.text()#serviço
    linha6 = interface.lineEdit_16.text()#valor
    linha7 = interface.lineEdit_15.text()#data
    cursor = banco.cursor()
    comando_sql = "INSERT INTO sabrina(nome,serviço,valor,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha4),str(linha5),str(linha6), str(linha7))
    cursor.execute(comando_sql,dados)
    banco.commit()
    interface.lineEdit_13.setText("")#nome
    interface.lineEdit_14.setText("")#serviço
    interface.lineEdit_16.setText("")#valor
    interface.lineEdit_15.setText("")#data
def serviços_outro_func():
    linha4 = interface.lineEdit_13.text()#nome
    linha5 = interface.lineEdit_14.text()#serviço
    linha6 = interface.lineEdit_16.text()#valor
    linha7 = interface.lineEdit_15.text()#data
    cursor = banco.cursor()
    comando_sql = "INSERT INTO outro_func(nome,serviço,valor,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha4),str(linha5),str(linha6), str(linha7))
    cursor.execute(comando_sql,dados)
    banco.commit()
    interface.lineEdit_13.setText("")#nome
    interface.lineEdit_14.setText("")#serviço
    interface.lineEdit_16.setText("")#valor
    interface.lineEdit_15.setText("")#data
def radio_button():
    
    funcionario = ""
    
    if interface.radioButton.isChecked() :
        funcionario =serviços_sabrina()
        
    elif interface.radioButton_2.isChecked() :
        funcionario = serviços_jefferson()

    elif interface.radioButton_3.isChecked() :
        funcionario = serviços_marllon()

    elif interface.radioButton_4.isChecked() :
        funcionario = serviços_wall()

    else :
        funcionario = serviços_outro_func()
def imprimir_pdf():
    #pdf jeff
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM jefferson"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Serviços_jefferson.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Serviços Feito:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "nome")
    pdf.drawString(210,750, "serviço")
    pdf.drawString(310,750, "valor")
    pdf.drawString(410,750, "data")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    
    #pdf wall
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM wallterlenia"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("serviços Wall.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Serviços Feitos:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "id")
    pdf.drawString(110,750, "nome")
    pdf.drawString(210,750, "serviço")
    pdf.drawString(310,750, "valor")
    pdf.drawString(410,750, "data")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    #pdf marllon
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM marllon"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Serviços marllon.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Serviços feitos:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "id")
    pdf.drawString(110,750, "cliente")
    pdf.drawString(210,750, "serviço")
    pdf.drawString(310,750, "valor")
    pdf.drawString(410,750, "data")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    
    # pdf sabrina
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM sabrina"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("serviços sabrina.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Serviços feitos:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "id")
    pdf.drawString(110,750, "nome")
    pdf.drawString(210,750, "serviço")
    pdf.drawString(310,750, "valor")
    pdf.drawString(410,750, "data")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    #outro funcionario
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM outro_func"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("serviços outro func.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "serviços feitos:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "id")
    pdf.drawString(110,750, "nome")
    pdf.drawString(210,750, "serviço")
    pdf.drawString(310,750, "valor")
    pdf.drawString(410,750, "data")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
# contas
def salão():
    linha1 = contas1.lineEdit.text()
    linha2 = contas1.lineEdit_2.text()#telefone
    linha3 = contas1.lineEdit_3.text()#data de nascimento
    linha4 = contas1.lineEdit_4.text()#data de nascimento



    cursor = banco.cursor()
    comando_sql = "INSERT INTO contas(valor,produlto,empresa,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3), str(linha4))
    cursor.execute(comando_sql,dados)
    banco.commit()

    contas1.lineEdit.setText("")#valor
    contas1.lineEdit_2.setText("")#produlto
    contas1.lineEdit_3.setText("")#empresa
    contas1.lineEdit_4.setText("")#data
def ver_salao():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM contas"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    banco.commit()
    contas1.tableWidget.setRowCount(len(dados_lidos))
    contas1.tableWidget.setColumnCount(5)

    for i in range(0,len(dados_lidos)):
        for j in range(0,5):
            contas1.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ver_uber():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM uber"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    banco.commit()
    contas1.tableWidget_2.setRowCount(len(dados_lidos))
    contas1.tableWidget_2.setColumnCount(5)

    for i in range(0,len(dados_lidos)):
        for j in range(0,5):
            contas1.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ver_comida():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM comida"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    banco.commit()
    contas1.tableWidget_3.setRowCount(len(dados_lidos))
    contas1.tableWidget_3.setColumnCount(5)

    for i in range(0,len(dados_lidos)):
        for j in range(0,5):
            contas1.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def ver_pessoais():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM pessoais"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    banco.commit()
    contas1.tableWidget_4.setRowCount(len(dados_lidos))
    contas1.tableWidget_4.setColumnCount(5)

    for i in range(0,len(dados_lidos)):
        for j in range(0,5):
            contas1.tableWidget_4.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def excluir_salao():
    linha = contas1.tableWidget.currentRow()
    contas1.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM contas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM contas WHERE id="+ str(valor_id))
    banco.commit()
def contas():
    contas1.show()
    ver_salao()
    ver_clientes()
    ver_comida()
    ver_pessoais()
    somar_dividas()
def somar_dividas():
    #jeff
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM jefferson") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_3.setText(valor)
    banco.commit()

    #marllon
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM marllon") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_9.setText(valor)
    banco.commit()

    #wall
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM wallterlenia") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_8.setText(valor)
    banco.commit()

    #sabrina
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM sabrina") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_10.setText(valor)
    banco.commit()
    
    #outro funcionario
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM outro_func") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_11.setText(valor)
    banco.commit()

    #salao
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM contas") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_14.setText(valor)
    banco.commit()
    #uber
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM uber") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_19.setText(valor)
    banco.commit()
    #comida
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM comida") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_18.setText(valor)
    banco.commit()
    #pessoais
    cursor = banco.cursor() 
    cursor.execute("SELECT SUM(valor) FROM pessoais") 
    valor = str(cursor.fetchall()[0][0])
    contas1.label_20.setText(valor)
    banco.commit()
def escolher_contas():
    contas2 = ""
    
    if contas1.radioButton.isChecked() :
        contas2 = comida()
        
    elif contas1.radioButton_2.isChecked() :
        contas2 = gastos_pessoais()

    elif contas1.radioButton_3.isChecked() :
        contas2 = uber()

    elif contas1.radioButton_4.isChecked() :
        contas2 = salão()

    else :
        print("deu ruim")
def uber():
    linha1 = contas1.lineEdit.text()
    linha2 = contas1.lineEdit_2.text()#telefone
    linha3 = contas1.lineEdit_3.text()#data de nascimento
    linha4 = contas1.lineEdit_4.text()#data de nascimento



    cursor = banco.cursor()
    comando_sql = "INSERT INTO uber(valor,produlto,empresa,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3), str(linha4))
    cursor.execute(comando_sql,dados)
    banco.commit()

    contas1.lineEdit.setText("")#valor
    contas1.lineEdit_2.setText("")#produlto
    contas1.lineEdit_3.setText("")#empresa
    contas1.lineEdit_4.setText("")#data
def comida():
    linha1 = contas1.lineEdit.text()
    linha2 = contas1.lineEdit_2.text()#telefone
    linha3 = contas1.lineEdit_3.text()#data de nascimento
    linha4 = contas1.lineEdit_4.text()#data de nascimento



    cursor = banco.cursor()
    comando_sql = "INSERT INTO comida(valor,produlto,empresa,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3), str(linha4))
    cursor.execute(comando_sql,dados)
    banco.commit()

    contas1.lineEdit.setText("")#valor
    contas1.lineEdit_2.setText("")#produlto
    contas1.lineEdit_3.setText("")#empresa
    contas1.lineEdit_4.setText("")#data
def gastos_pessoais():
    linha1 = contas1.lineEdit.text()
    linha2 = contas1.lineEdit_2.text()#telefone
    linha3 = contas1.lineEdit_3.text()#data de nascimento
    linha4 = contas1.lineEdit_4.text()#data de nascimento



    cursor = banco.cursor()
    comando_sql = "INSERT INTO pessoais(valor,produlto,empresa,data) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3), str(linha4))
    cursor.execute(comando_sql,dados)
    banco.commit()

    contas1.lineEdit.setText("")#valor
    contas1.lineEdit_2.setText("")#produlto
    contas1.lineEdit_3.setText("")#empresa
    contas1.lineEdit_4.setText("")#data
#voltar
def voltar_contas():
    contas1.close()
    interface.show()
#def excluir
def excluir_uber():
    linha = contas1.tableWidget_2.currentRow()
    contas1.tableWidget_2.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM uber")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM contas WHERE id="+ str(valor_id))
    banco.commit()
def excluir_comida():
    linha = contas1.tableWidget_3.currentRow()
    contas1.tableWidget_3.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM comida")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM contas WHERE id="+ str(valor_id))
    banco.commit()
def excluir_pessoais():
    linha = contas1.tableWidget_4.currentRow()
    contas1.tableWidget_4.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM pessoais")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM contas WHERE id="+ str(valor_id))
    banco.commit()
def excluir_geral():
    tudo_outro()
    tudo_sabrina()
    tudo_wall()
    tudo_marllon()
    tudo_jeff()
    tudo_comida()
    tudo_pessoais()
    tudo_salao()
    tudo_uber()
def tudo_outro():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM outro_func"
    cursor.execute(comando_sql)
def tudo_sabrina():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM sabrina"
    cursor.execute(comando_sql)
def tudo_wall():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM wallterlenia"
    cursor.execute(comando_sql)
def tudo_jeff():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM jefferson"
    cursor.execute(comando_sql)
def tudo_marllon():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM marllon"
    cursor.execute(comando_sql)

def tudo_pessoais():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM pessoais"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    contas1.tableWidget_4.setRowCount(len(dados_lidos))
    contas1.tableWidget_4.setColumnCount(4)

    for i in range(0,len(dados_lidos)):
        for j in range(0,4):
            contas1.tableWidget_4.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def tudo_comida():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM comida"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    contas1.tableWidget_3.setRowCount(len(dados_lidos))
    contas1.tableWidget_3.setColumnCount(4)

    for i in range(0,len(dados_lidos)):
        for j in range(0,4):
            contas1.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def tudo_uber():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM uber"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    contas1.tableWidget_2.setRowCount(len(dados_lidos))
    contas1.tableWidget_2.setColumnCount(4)

    for i in range(0,len(dados_lidos)):
        for j in range(0,4):
            contas1.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def tudo_salao():
    cursor = banco.cursor()
    comando_sql = "DELETE  FROM contas"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    contas1.tableWidget.setRowCount(len(dados_lidos))
    contas1.tableWidget.setColumnCount(4)

    for i in range(0,len(dados_lidos)):
        for j in range(0,4):
            contas1.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
app = QtWidgets.QApplication([])
loguin = uic.loadUi("loguin.ui")
loguin.pushButton.clicked.connect(senha)
interface = uic.loadUi("interface.ui")
interface.pushButton.clicked.connect(cadastro)#liga o cadastro de clientes
interface.pushButton.clicked.connect(ver_clientes)#mostra clientes na table
interface.pushButton_6.clicked.connect(radio_button)#escolhe o funcionario
interface.pushButton_3.clicked.connect(excluir_clientes)#exclui clientes
interface.pushButton_8.clicked.connect(contas)#liga a segunda tela
interface.pushButton_7.clicked.connect(imprimir_pdf)#liga pdf

contas1=uic.loadUi("contas.ui")
contas1.pushButton.clicked.connect(escolher_contas)
contas1.pushButton.clicked.connect(ver_salao)
contas1.pushButton.clicked.connect(ver_uber)
contas1.pushButton.clicked.connect(ver_comida)
contas1.pushButton.clicked.connect(ver_pessoais)

contas1.pushButton_2.clicked.connect(excluir_geral)

contas1.pushButton_3.clicked.connect(excluir_salao)
contas1.pushButton_5.clicked.connect(excluir_uber)
contas1.pushButton_6.clicked.connect(excluir_comida)
contas1.pushButton_7.clicked.connect(excluir_pessoais)

contas1.pushButton_4.clicked.connect(voltar_contas)


loguin.show()
app.exec()

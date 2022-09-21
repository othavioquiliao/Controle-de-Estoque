from tkinter import Button, font
from tkinter.font import BOLD
import PySimpleGUI as sg
import pandas as pd
from datetime import datetime
from openpyxl import Workbook
import pathlib
from openpyxl import load_workbook

sg.theme("Reddit")


# Caminho do excel (pos import pandas as pd)
EXCEL_FILE = "Estoque.xlsx"

arquivo = pathlib.Path(EXCEL_FILE)

if arquivo.exists():
    pass
else:
    sg.popup("Criando pasta de estoque... tente abrir novamente")
    EXCEL_FILE = Workbook()
    sheet = EXCEL_FILE.active
    sheet["A1"] = "-FUNCIONARIO-"
    sheet["B1"] = "-ADICIONADO-"
    sheet["C1"] = "-VENCE-"
    sheet["D1"] = "-QUANTIDADE-"
    sheet["E1"] = "-CODIGO-"
    sheet["F1"] = "-PRODUTO-"
    sheet["G1"] = "-PRECO-"

    EXCEL_FILE.save("Estoque.xlsx")


df = pd.read_excel(EXCEL_FILE)


funcionarios = ["Carlos", "Lucia", "Leonardo", "Luana"]


def janela_login():
    sg.theme("Reddit")
    layout = [
        [
            [sg.Image(filename="Logo_Inicial.png")],
            [
                sg.Push(),
                sg.Text("Usuario", font=("Roboto", 10, BOLD)),
                sg.Input(
                    key="-USUARIO-",
                    size=(22, 1),
                ),
                sg.Push(),
            ],
            [
                sg.Push(),
                sg.Button(
                    "Continuar",
                    key="-BOTAOCONTINUAR-",
                    font=("Roboto", 10, BOLD),
                    button_color=("white", "DarkBlue"),
                    size=(10, 1),
                ),
                sg.Button(
                    "Sair",
                    button_color=("white", "DarkBlue"),
                    font=("Roboto", 10, BOLD),
                    size=(10, 1),
                ),
                sg.Push(),
            ],
        ]
    ]

    return sg.Window("Login", layout=layout, finalize=True)


def janela_principal():
    sg.theme("Reddit")
    layout = [
        [sg.Image(filename="Logo_Santa.png")],
        [sg.Text("Bem vindo ao sistema de estoque:", font=("Roboto  ", 20))],
        [
            sg.Push(),
            sg.Button(
                "Adicionar produto",
                size=(20, 1),
                key="-BOTAOADICIONAR-",
                font=("Roboto", 10, BOLD),
            ),
            sg.Button(
                "Remover produto",
                size=(20, 1),
                key="-BOTAOREMOVER-",
                font=("Roboto", 10, BOLD),
            ),
            sg.Push(),
        ],
        [
            sg.Push(),
            sg.Button(
                "Visualizar estoque",
                size=(20, 1),
                key="-BOTAOVISUALIZAR-",
                font=("Roboto", 10, BOLD),
            ),
            sg.Button(
                "Verificar vencimentos",
                size=(20, 1),
                key="-BOTAOVERIFICAR-",
                font=("Roboto", 10, BOLD),
            ),
            sg.Push(),
        ],
        [
            sg.Push(),
            sg.Button(
                "Voltar",
                size=(10, 1),
                button_color=("white", "darkblue"),
                font=("Roboto", 10, BOLD),
            ),
            sg.Button(
                "Sair",
                size=(10, 1),
                button_color=("white", "darkblue"),
                font=("Roboto", 10, BOLD),
            ),
            sg.Push(),
        ],
    ]
    return sg.Window(
        "Estoque", layout=layout, element_justification="center", finalize=True
    )


def Adicionar_Produtos():
    sg.theme("Reddit")
    layout = [
        [
            sg.Text("Funcionario:", size=(15, 1), font=("Roboto", 12)),
            sg.Push(),
            sg.InputCombo(funcionarios, size=(20, 1), key="-FUNCIONARIO-"),
            sg.Push(),
            sg.Button(
                "Data",
                target="-ADICIONADO-",
                font=("Roboto", 10, BOLD),
            ),
            sg.InputText(size=(10, 1), key="-ADICIONADO-"),
            sg.Push(),
            sg.Button(
                "Vencimento",
                target="-VENCE-",
                font=("Roboto", 10, BOLD),
            ),
            sg.InputText(size=(8, 1), key="-VENCE-"),
        ],
        [
            sg.Text("Codigo de barra:", size=(13, 1), font=("Roboto", 12)),
            sg.InputText(size=(26, 1), key="-CODIGO-", font=("Roboto", 12)),
            sg.Push(),
            sg.Text("Quantidade:", size=(9, 1), font=("Roboto", 12)),
            sg.InputText(size=(11, 1), key="-QUANTIDADE-", font=("Roboto", 12)),
        ],
        [
            sg.Text("Nome do produto:", size=(14, 1), font=("Roboto", 12)),
            sg.InputText(size=(25, 1), key="-PRODUTO-", font=("Roboto", 12)),
            sg.Push(),
            sg.Text("Preço: ", size=(5, 1), font=("Roboto", 12)),
            sg.InputText(size=(11, 1), key="-PRECO-", font=("Roboto", 12)),
        ],
        [sg.VPush()],
        [
            sg.Push(),
            sg.Button(
                "Adicionar",
                size=(15, 1),
                font=("Roboto", 12, BOLD),
                button_color=("white", "green"),
                key="-BOTAOADICIONARPRODUTO-",
            ),
            sg.Button(
                "Limpar", size=(15, 1), font=("Roboto", 12, BOLD), key="-LIMPAR-"
            ),
            sg.Button(
                "Voltar",
                size=(15, 1),
                font=("Roboto", 12, BOLD),
                button_color=("white", "darkblue"),
            ),
            sg.Push(),
        ],
    ]
    return sg.Window("Adicionar produtos", layout=layout, finalize=True)


# --------------------- TENTATIVA DE FUNÇÃO PARA REMOVER PRODUTOS ---------------------#
def Limpar_Janela_Adicionar():
    for key in values:
        janela3[
            "-ADICIONADO-",
            "-ADICIONADO-",
            "-CODIGO-",
            "-QUANTIDADE-",
            "-PRODUTO-",
            "-PRECO-",
        ].update(" ")
    return None


# --------------------- USUARIOS PARA LOGIN ---------------------#

usuariosLogin = ["1", "Davi", "Carlos", "Othavio", "lucas"]


# ----------------------------- VIZUALIZAÇAO DAS JANELAS E EVENTOS --------------------------------------#

janela1, janela2, janela3 = janela_login(), None, None

while True:
    window, event, values = sg.read_all_windows()
    # -------------------------------JANELA LOGIN------------------------------
    if window == janela1 and event == sg.WIN_CLOSED or event == "Sair":
        break
    elif window == janela1 and event == "-BOTAOCONTINUAR-":
        if values["-USUARIO-"] in usuariosLogin:
            janela1.hide()
            janela2 = janela_principal()
        else:
            sg.popup("Usuario invalido")

    # ------------------------------- JANELA PRINCIPAL --------------------------------
    elif window == janela2 and event == sg.WIN_CLOSED or event == "Sair":
        break

    elif window == janela2 and event == "Voltar":
        janela2.hide()
        janela1 = janela_login()

    # ------------------------JANELA ADICIONAR PRODUTOS --------------------------------
    elif window == janela2 and event == "-BOTAOADICIONAR-":
        janela2.hide()
        janela3 = Adicionar_Produtos()
    elif window == janela3 and event == "Voltar":
        janela3.hide()
        janela2 = janela_principal()
    elif window == janela3 and event == sg.WIN_CLOSED:
        break
    elif window == janela3 and event == "-LIMPAR-":
        for key in values:  # key é o nome do elemento
            janela3[key].update(" ")

    elif window == janela3 and event == "Data":
        date = sg.popup_get_date(close_when_chosen=True)
        if date:
            month, day, year = date
            janela3["-ADICIONADO-"].update(f"{day:0>2d}/{month:0>2d}/{year}")
    elif window == janela3 and event == "Vencimento":
        date = sg.popup_get_date(close_when_chosen=True)
        if date:
            month, day, year = date
            janela3["-VENCE-"].update(f"{day:0>2d}/{month:0>2d}/{year}")

    # -------------------------- FUNÇAO QUE ADICIONA PRODUTOS --------------------------------
    elif window == janela3 and event == "-BOTAOADICIONARPRODUTO-":
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup("Produto adicionado com sucesso")
        for key in values:
            janela3[key].update(" ")

window.close()

import tkinter as tk

def botao_clique(numero):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + str(numero))

def botao_limpar():
    entrada.delete(0, tk.END)

def botao_adicionar():
    primeiro_numero = entrada.get()
    global num_1
    global operacao_matematica
    operacao_matematica = "adicao"
    num_1 = float(primeiro_numero)
    entrada.delete(0, tk.END)

def botao_subtrair():
    primeiro_numero = entrada.get()
    global num_1
    global operacao_matematica
    operacao_matematica = "subtracao"
    num_1 = float(primeiro_numero)
    entrada.delete(0, tk.END)

def botao_multiplicar():
    primeiro_numero = entrada.get()
    global num_1
    global operacao_matematica
    operacao_matematica = "multiplicacao"
    num_1 = float(primeiro_numero)
    entrada.delete(0, tk.END)

def botao_dividir():
    primeiro_numero = entrada.get()
    global num_1
    global operacao_matematica
    operacao_matematica = "divisao"
    num_1 = float(primeiro_numero)
    entrada.delete(0, tk.END)

def botao_igual():
    segundo_numero = entrada.get()
    entrada.delete(0, tk.END)

    if operacao_matematica == "adicao":
        resultado = num_1 + float(segundo_numero)
    elif operacao_matematica == "subtracao":
        resultado = num_1 - float(segundo_numero)
    elif operacao_matematica == "multiplicacao":
        resultado = num_1 * float(segundo_numero)
    elif operacao_matematica == "divisao":
        resultado = num_1 / float(segundo_numero)

    entrada.insert(tk.END, resultado)
    resultado_entrada.delete(0, tk.END)
    resultado_entrada.insert(tk.END, resultado)

def botao_ponto():
    atual = entrada.get()
    if "." not in atual:
        entrada.insert(tk.END, ".")

def botao_espaco():
    atual = entrada.get()
    entrada.delete(len(atual) - 1)

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=40, borderwidth=8)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

botao_1 = tk.Button(janela, text="1", padx=40, pady=20, command=lambda: botao_clique(1))
botao_2 = tk.Button(janela, text="2", padx=40, pady=20, command=lambda: botao_clique(2))
botao_3 = tk.Button(janela, text="3", padx=40, pady=20, command=lambda: botao_clique(3))
botao_4 = tk.Button(janela, text="4", padx=40, pady=20, command=lambda: botao_clique(4))
botao_5 = tk.Button(janela, text="5", padx=40, pady=20, command=lambda: botao_clique(5))
botao_6 = tk.Button(janela, text="6", padx=40, pady=20, command=lambda: botao_clique(6))
botao_7 = tk.Button(janela, text="7", padx=40, pady=20, command=lambda: botao_clique(7))
botao_8 = tk.Button(janela, text="8", padx=40, pady=20, command=lambda: botao_clique(8))
botao_9 = tk.Button(janela, text="9", padx=40, pady=20, command=lambda: botao_clique(9))
botao_0 = tk.Button(janela, text="0", padx=40, pady=20, command=lambda: botao_clique(0))
botao_adicionar = tk.Button(janela, text="+", padx=39, pady=20, command=botao_adicionar)
botao_subtrair = tk.Button(janela, text="- ", padx=39, pady=20, command=botao_subtrair)
botao_multiplicar = tk.Button(janela, text="* ", padx=39, pady=20, command=botao_multiplicar)
botao_dividir = tk.Button(janela, text="/ ", padx=39, pady=20, command=botao_dividir)
botao_limpar = tk.Button(janela, text="C", padx=39, pady=20, command=botao_limpar)
botao_igual = tk.Button(janela, text="=", padx=39, pady=20, command=botao_igual)
botao_ponto = tk.Button(janela, text=". ", padx=40, pady=20, command=botao_ponto)
botao_espaco = tk.Button(janela, text="←", padx=38, pady=20, command=botao_espaco)

botao_1.grid(row=1, column=0)
botao_2.grid(row=1, column=1)
botao_3.grid(row=1, column=2)
botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)
botao_7.grid(row=3, column=0)
botao_8.grid(row=3, column=1)
botao_9.grid(row=3, column=2)
botao_limpar.grid(row=4, column=0)
botao_0.grid(row=4, column=1)
botao_espaco.grid(row=4, column=2)
botao_adicionar.grid(row=5, column=0)
botao_subtrair.grid(row=5, column=1)
botao_multiplicar.grid(row=5, column=2)
botao_dividir.grid(row=6, column=0)
botao_ponto.grid(row=6, column=1)
botao_igual.grid(row=6, column=2)

janela.mainloop()
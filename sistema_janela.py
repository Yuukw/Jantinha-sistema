import tkinter as tk

def calcular():
    try:
        qtd_j = int(entrada_j.get())
        qtd_e = int(entrada_e.get())
        preco_j = float(entrada_pj.get())
        preco_e = float(entrada_pe.get())
        gasto = float(entrada_g.get())
        
        faturamento = qtd_j * preco_j + qtd_e * preco_e
        lucro = faturamento - gasto
        falta = 2000 - lucro
        
        if falta > 0:
            msg = f"Faturou: R$ {faturamento:.2f}\nLucro: R$ {lucro:.2f}\nFalta pagar: R$ {falta:.2f}"
        else:
            msg = f"Faturou: R$ {faturamento:.2f}\n🎉 INVESTIMENTO PAGO!\nLucro extra: R$ {-falta:.2f}"
        
        resultado["text"] = msg
    except:
        resultado["text"] = "Preencha tudo com números!"

janela = tk.Tk()
janela.title("Sistema Jantinha V2 - Configurável")
janela.geometry("320x500")

tk.Label(janela, text="Preço Jantinha: R$", font=("Arial", 10, "bold")).pack()
entrada_pj = tk.Entry(janela); entrada_pj.insert(0, "20"); entrada_pj.pack()

tk.Label(janela, text="Preço Espetinho: R$", font=("Arial", 10, "bold")).pack()
entrada_pe = tk.Entry(janela); entrada_pe.insert(0, "12"); entrada_pe.pack()

tk.Label(janela, text="--- VENDAS DE HOJE ---", font=("Arial", 10)).pack(pady=10)

tk.Label(janela, text="Qtd Jantinhas vendidas:").pack()
entrada_j = tk.Entry(janela); entrada_j.pack()
tk.Label(janela, text="Qtd Espetinhos vendidos:").pack()
entrada_e = tk.Entry(janela); entrada_e.pack()
tk.Label(janela, text="Quanto gastou hoje? R$").pack()
entrada_g = tk.Entry(janela); entrada_g.pack()

tk.Button(janela, text="CALCULAR", command=calcular, bg="green", fg="white", height=2, width=20).pack(pady=20)
resultado = tk.Label(janela, text="", font=("Arial", 12), justify="left"); resultado.pack()

janela.mainloop()

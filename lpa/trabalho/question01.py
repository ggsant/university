# o que falta?
# colocar comentarios relevantes k
# tenho algumas duvidas em relação ao enunciado

def calcula_valor_do_juros(quantidadeDeParcelas): # Exigência 03
    if quantidadeDeParcelas < 4: # Exigência 05
        return 0.0  
    elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6:
        return 0.04
    elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas < 9:
        return 0.08
    elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13:
        return 0.16
    else:
        return 0.32
        
def calcula_valor_da_parcela(valorDoPedido, quantidadeDeParcelas, juros): # Exigência 04
     valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeDeParcelas
     valorArredondado = round(valorDaParcela, 2) # verificar se tem que arredondar ou não, se arredondar o valor total fica diferente do apresentado no print
     return valorArredondado
 
def calcula_valor_total_parcelado(valorDaParcela, quantidadeDeParcelas): # Exigência 04
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
    valorArredondado = round(valorTotalParcelado, 2) # verificar se tem que arredondar ou não,
    return valorArredondado

# Main code
print('Bem-vindo a Loja da Gabriela Pereira dos Santos') # Exigência 01

valorDoPedido = float(input('Entre com o valor do pedido: ')) # Exigência 02
quantidadeDeParcelas = float(input('Entre com a quantidade de parcelas: ')) # Exigência 02

juros = calcula_valor_do_juros(quantidadeDeParcelas)
valorDaParcela = calcula_valor_da_parcela(valorDoPedido, quantidadeDeParcelas, juros)
valorTotalParcelado = calcula_valor_total_parcelado(valorDaParcela, quantidadeDeParcelas)

print(f'O valor das parcelas é de: R$ {valorDaParcela}')
print(f'O valor Total Parcelado é de: R$ {valorTotalParcelado}')



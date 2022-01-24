from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria

# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

# fila_teste_2 = FilaNormal()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

f1 = FabricaFila().pegar_fila('prioritaria')
f1.atualiza_fila()
f1.atualiza_fila()
print(f1.chama_cliente(10))
print(f1.chama_cliente(11))
print(
    f1.estatistica(
        '01/01/2021', 120, EstatisticaResumida('01/01/2021', 120)
    )
)
print(
    f1.estatistica(
        '01/01/2021', 120, EstatisticaDetalhada('01/01/2021', 120)
    )
)

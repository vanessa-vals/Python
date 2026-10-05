
# # exemplo sem a orientação ao objetos
# vendedor = "Nathan"
# vendas = 1000.00
# meta = 500

# if vendas >= meta:
#     print(f"{vendedor} bateu a meta de vendas.")    
#     else:
#     print(f"{vendedor} não bateu a meta de vendas.")       

# import os
# os.system('cls' if os.name == 'nt' else 'clear')
from classe import Vendedor


# exemplo com a orientação ao objetos de preferência criar classe com a 1° em Maiuscula
# class Vendedor:
#     def __init__(self, nome):
#         self.nome = nome
#         self.vendas = 0

#     def vendeu(self, vendas):
#         self.vendas = vendas

#     def bateu_meta(self, meta):
#         if self.vendas >= meta:
#             print(self.nome, "Bateu a meta")
#         else:
#             print(self.nome," Não bateu a meta")


vendedor1 = Vendedor("Nathan")
print(vendedor1.nome)
vendedor1.vendeu(1000)
vendedor1.bateu_meta(500)

vendedor2 = Vendedor ('João')
print (vendedor2.nome)
vendedor2.vendeu(400)
vendedor2.bateu_meta(401)


   
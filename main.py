# Instalação de bibliotecas
# pip install python-barcode
# pip install pillow

# Exemplo: Lista de produtos de Informática Hardware
from barcode import EAN13
from barcode.writer import ImageWriter

codigos_produtos = {
  'Gabinete': '999888777111',
  'Placa Mae': '888777666111',
  'Processador': '777666555111',
  'Memoria RAM': '666555444111',
  'Fonte': '555444333111',
  'SSD': '444333222111',
  'Water Cooler': '333222111000',
  'Placa de Video': '222111000111'
}

for produto in codigos_produtos:
  codigo = codigos_produtos[produto]
  codigo_barra = EAN13(codigo, writer=ImageWriter())
  codigo_barra.save(f'codigo_barra_{produto}')
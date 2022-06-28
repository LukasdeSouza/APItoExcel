from urllib import request
import openpyxl
import requests

cep_input = input("Digite o CEP para consulta:")
cep_input2 = input("Digite o segundo CEP para consulta:")
cep_input3 = input("Digite o terceiro CEP consulta:")
cep_input4 = input("Digite o quarto CEP para consulta:")

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
result_data = (request.json())

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input2))
result_data2 = (request.json())

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input3))
result_data3 = (request.json())

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input4))
result_data4 = (request.json())


certisign = openpyxl.Workbook()

certisign.create_sheet('Certisign')

frutas_page = certisign['Certisign']
frutas_page.append(['CEP', 'Rua', 'Bairro'])
frutas_page.append(['{}'.format(result_data['cep']),'{}'.format(result_data['logradouro']),'{}'.format(result_data['bairro'])])
frutas_page.append(['{}'.format(result_data2['cep']),'{}'.format(result_data2['logradouro']),'{}'.format(result_data2['bairro'])])
frutas_page.append(['{}'.format(result_data3['cep']),'{}'.format(result_data3['logradouro']),'{}'.format(result_data3['bairro'])])
frutas_page.append(['{}'.format(result_data4['cep']),'{}'.format(result_data4['logradouro']),'{}'.format(result_data4['bairro'])])
certisign.save('Excel test.xlsx')

print('Planiha gerada com sucesso! =D')
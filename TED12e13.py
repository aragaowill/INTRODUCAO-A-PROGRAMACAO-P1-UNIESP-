# Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão,
# chame este dicionário de glossário. Pense em cinco palavras relacionada à programação que você
# conheceu nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
# Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante.
# Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado,
# ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha.
# Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par de palavra-significado
# em sua saída.
# Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code.

glossario = {
    'Algoritimo': 'É uma Sequência de instruções ou comandos realizados de maneira sistemática com o objetivo de resolver um problema ou executar uma tarefa.',
    'Dicionario em Python': 'É uma coleção não ordenada de valores de dados, usada para armazenar valores de dados como um mapa.',
    'Visual Studio Code': 'Ambiente de desenvolvimento de códigos para vários tipos de linguagem.',
    'Python': 'Linguagem de programação.',
    'Variável': 'É um objeto (uma posição, frequentemente localizada na memória) capaz de reter e representar um valor ou expressão.'
}
for key, value in glossario.items():
    print(f'{key} : {value} \n -----------------------------------------------------------------')
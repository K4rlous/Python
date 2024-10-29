# Biblioteca datetime

"A biblioteca datetime em Python é uma ferramenta poderosa para manipulação de datas e horas. Ela fornece classes para trabalhar com data, hora, fusos horários, intervalos de tempo e muito mais. Vamos explorar algumas das principais funcionalidades:"

"Importação e Classes Básicas:"

# datetime.date: Representa uma data (ano, mês, dia).
# datetime.time: Representa uma hora (horas, minutos, segundos, microsegundos).
# datetime.datetime: Combina data e hora.
# datetime.timedelta: Representa a diferença entre duas datas ou horas.

import datetime

# Data atual
data_atual = datetime.date.today()
print("Data atual:", data_atual)

# Hora atual
hora_atual = datetime.datetime.now().time()
print("Hora atual:", hora_atual)

# Data e hora atuais
data_hora_atual = datetime.datetime.now()
print("Data e Hora atual:", data_hora_atual)

"Trabalhando com datetime.timedelta: Útil para realizar operações aritméticas com datas e horas."

# 10 dias no futuro
futuro = data_atual + datetime.timedelta(days=10)
print("10 dias no futuro:", futuro)

# 10 dias no passado
passado = data_atual - datetime.timedelta(days=10)
print("10 dias no passado:", passado)

"Formatação de Datas e Horas:"

# strftime: Formata objetos de data e hora em strings.
# strptime: Converte strings em objetos de data e hora.

# Formatação de data
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)

# Convertendo string para datetime
data_string = "25/12/2022 20:30:00"
data_convertida = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
print("Data convertida:", data_convertida)

"Trabalhando com Fusos Horários:"

#pytz é uma biblioteca auxiliar popular para lidar com fusos horários.

import pytz

# Fuso horário atual
data_hora = datetime.datetime.now(pytz.utc)
print("Data e Hora UTC:", data_hora)

# Converter para um fuso horário específico
fuso_horario = pytz.timezone('America/Sao_Paulo')
data_hora_local = data_hora.astimezone(fuso_horario)
print("Data e Hora em São Paulo:", data_hora_local)

# shop/context_processors.py
from datetime import datetime
import pytz

def ano_corrente(request):
    fuso = pytz.timezone('America/Sao_Paulo') # Pegar fuso horário de São Paulo
    data_corrente = datetime.now(fuso) # Pegar data e hora corrente com fuso horário
    ano_corrente = data_corrente.strftime('%Y') # Formatar para pegar só o ano com 4 dígitos
    return {'ano_corrente': ano_corrente} # Retornar dicionário com o ano corrente

def data_corrente_completa(request):
  fuso = pytz.timezone('America/Sao_Paulo')
  data_corrente = datetime.now(fuso)
  data_corrente = data_corrente.strftime('%d/%m/%Y %H:%M')
  return {'data_corrente': data_corrente}
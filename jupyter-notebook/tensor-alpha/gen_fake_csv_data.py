from faker import Faker
import random
import csv

# Classe do gerador de dados.
class SensitiveDataGenerator():
  def __init__(self, language:str) -> None:
    """_summary_
    Args:
        language (str): _description_
    """    
    self.language = language
  
  # Gerador do header.
  def __generate_data_header(self) -> list:
    """_summary_
    Returns:
        list: _description_
    """    
    return ['nome', 'cartão de crédito', 'telefone', 'tipo do dado']
  
  # Gerador de dados sensitivos falsos.
  def __generate_data(self, type) -> list:
    """_summary_
    Returns:
        list: _description_
    """    
    fake = Faker(self.language)
    if type == True:
      return [fake.name(), fake.credit_card_number(), fake.phone_number(), 1]
    return [fake.name(), fake.credit_card_number(), fake.phone_number()]
  
  # Gerador de dados aleatórios falsos, nem todas as linhas serão dados sensíveis.
  def __generate_data_random(self, type:bool) -> list:
    """_summary_
    Returns:
        list: _description_
    """    
    fake = Faker(self.language)
    if type:
      if(random.randint(0,1) < 1):
        return [fake.name(), fake.credit_card_number(), fake.phone_number(), 1]
      else:
        return [fake.name(), fake.android_platform_token(), fake.job(), 0]
    if(random.randint(0,1) < 1):
      return [fake.name(), fake.credit_card_number(), fake.phone_number()]
    else:
      return [fake.name(), fake.android_platform_token(), fake.job()]

  # Escrita de CSV baseado em dados de entrada pro usuário.
  def write_csv_data_from_list(self, data:list, name='dados_sensiveis_lista.csv', title:list=None, size:int=10) -> True:
    """_summary_
    Args:
        data (list): _description_
        name (str, optional): _description_. Defaults to 'dados_sensiveis_lista.csv'.
    Returns:
        True: _description_
    """    
    with open(name, 'w',  newline='', encoding='utf-8') as csv_file:
      writer:object = csv.writer(csv_file)
      if(title is None):
        writer.writerow(self.__generate_data_header())
      else:
        writer.writerow(title)
      for _ in range(1, size):
        writer.writerow(data)
  
  # Escrita de dados CSV gerados, sendo eles apenas senspiveis.
  def write_csv_data_sensitive_only_without_result(self, name='dados_sensiveis.csv', title:list=None, size:int=10):
    """_summary_
    Args:
        name (str, optional): _description_. Defaults to 'dados_sensiveis.csv'.
    """    
    with open(name, 'w',  newline='', encoding='utf-8') as csv_file:
        writer:object = csv.writer(csv_file)
        if(title is None):
          writer.writerow(self.__generate_data_header())
        else:
          writer.writerow(title)
        for _ in range(1, size):
          writer.writerow(self.__generate_data(False))
  
  def write_csv_data_sensitive_only(self, name='dados_sensiveis.csv', title:list=None, size:int=10):
    """_summary_
    Args:
        name (str, optional): _description_. Defaults to 'dados_sensiveis.csv'.
    """    
    with open(name, 'w',  newline='', encoding='utf-8') as csv_file:
        writer:object = csv.writer(csv_file)
        if(title is None):
          writer.writerow(self.__generate_data_header())
        else:
          writer.writerow(title)
        for _ in range(1, size):
          writer.writerow(self.__generate_data(True))

  # Escrita de dados CSV gerados, sendo eles apenas aleatórios, podendo ser sensível ou não
  def write_csv_data_random(self, name:str='dados_sensiveis_aleatorio.csv', title:list=None, size:int=10) -> True:
    """_summary_
    Args:
        name (str, optional): _description_. Defaults to 'dados_sensiveis_aleatorio.csv'.
    Returns:
        True: _description_
    """    
    with open(name, 'w',  newline='', encoding='utf-8') as csv_file:
      writer:object = csv.writer(csv_file)
      if(title is None):
        writer.writerow(self.__generate_data_header())
      else:
        writer.writerow(title)
      for _ in range(1, size):
        writer.writerow(self.__generate_data_random(True))
  
  def write_csv_data_random_no_result(self, name:str='dados_sensiveis_aleatorio_sem_resultado.csv', title:list=None, size:int=10) -> True:
    """_summary_
    Args:
        name (str, optional): _description_. Defaults to 'dados_sensiveis_aleatorio.csv'.
    Returns:
        True: _description_
    """    
    with open(name, 'w',  newline='', encoding='utf-8') as csv_file:
      writer:object = csv.writer(csv_file)
      if(title is None):
        writer.writerow(['nome', 'cartão de crédito', 'telefone'])
      else:
        writer.writerow(title)
      for _ in range(1, size):
        writer.writerow(self.__generate_data_random(False))

if __name__ == '__main__':
  sensitive_data_generator = SensitiveDataGenerator('pt_br')
  sensitive_data_generator.write_csv_data_random(title=['Dado A', 'Dado B', 'Dado C', 'tipo'])
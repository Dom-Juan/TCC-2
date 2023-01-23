import hashlib
import csv

from rsa_alg import RSA



def sha_512_hash(data):
  return hashlib.sha512(data.encode('utf-8')).hexdigest()


def generate_rsa_str(result)-> str:
  return (''.join(str(x) for x in result))


def rsa_encrypt(predict_x, x, classes, filename='dataset_encriptado_teste.csv'):
  with open(filename, 'w',  newline='', encoding='utf-8') as csv_file:
    writer:object = csv.writer(csv_file)
    writer.writerow(['Coluna A', 'Coluna B', 'Coluna C'])
    rsa_alg = RSA(17, 41)
    rsa_alg.calc_n()
    rsa_alg.calc_euler_totient()
    rsa_alg.calc_public_key(15)
    for index in range(1, 1000-1):
      print(f'Iteração: {index}')
      if(round(predict_x[index][0]) == classes[index]):
        r1 = rsa_alg.encrypt_message(x['Coluna A'][index])
        r2 = rsa_alg.encrypt_message(x['Coluna B'][index])
        r3 = rsa_alg.encrypt_message(x['Coluna C'][index])
        writer.writerow([
          generate_rsa_str(r1),
          generate_rsa_str(r2),
          generate_rsa_str(r3)
          ])
      else:
        writer.writerow([x['Coluna A'][index], x['Coluna B'][index], x['Coluna C'][index]])
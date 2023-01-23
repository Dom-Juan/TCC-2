import matplotlib.pyplot as plot


plot.style.use('ggplot')
plot.style.use('dark_background')


# Mostrando o history dos models.
def plot_history(history):
  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']
  loss = history.history['loss']
  val_loss = history.history['val_loss']
  x = range(1, len(accuracy) + 1)
  # Plot da figura.
  plot.figure(figsize=(12, 5))
  plot.subplot(1, 2, 1)
  plot.plot(x, accuracy, 'b', label='Acurácia de treinamento')
  plot.plot(x, val_accuracy, 'r', label='Validação de acurácia')
  plot.title('Treinamento e validação de acurácia')
  plot.xlabel('Amostra')
  plot.ylabel('Acurácia')
  plot.legend()
  plot.subplot(1, 2, 2)
  plot.plot(x, loss, 'b', label='Perca/loss no treinamento')
  plot.plot(x, val_loss, 'r', label='Perca/loss na validação')
  plot.title('Treinamento e validação de perca/loss.')
  plot.xlabel('Amostra')
  plot.ylabel('Perca')
  plot.legend()


# Mostrando a precisão.
def plot_history_accuracy(history):
  plot.plot(history.history['accuracy'])
  plot.plot(history.history['val_accuracy'])
  plot.title('model accuracy')
  plot.ylabel('acurácia')
  plot.xlabel('épocas')
  plot.legend(['treino', 'teste'], loc='upper left')
  plot.show()


# Mostrando o loss.
def plot_history_loss(history):
  plot.plot(history.history['loss'])
  plot.plot(history.history['val_loss'])
  plot.title('model loss')
  plot.ylabel('perca')
  plot.xlabel('épocas')
  plot.legend(['treino', 'teste'], loc='upper left')
  plot.show()


# Mostrando a comapração da validação de treinamento vs a de teste.
def plot_validation_acc_vs_trainning_acc(history):
  loss_train = history.history['accuracy']
  loss_val = history.history['val_accuracy']
  epochs = range(1,11)
  plot.plot(epochs, loss_train, 'g', label='Acurácia de treinamento.')
  plot.plot(epochs, loss_val, 'b', label='Acurácia de validação.')
  plot.title('Treinamento e Validção de acurácia')
  plot.xlabel('Épocas')
  plot.ylabel('Acurácia')
  plot.legend()
  plot.show()


# Mostra as porcentagens.
def percentage_helper(pct, allvals):
  absolute = int(pct/100.*np.sum(allvals))
  return "{:.1f}%\n({:d})".format(pct, absolute)

# Função de plot de gráficos de pizzas.
def plot_pie(data: list):
  results = [
  "Positivos",
  "Negativos",
  "Falsos Positivos",
  "Falsos Negativos"
  ]
  #  Criando a área de plot o gráfico e definimos o seu tamanho.
  fig, ax = plot.subplots(figsize=(10,8), subplot_kw=dict(aspect="equal"))
  # Criando o grafico e usando a função custom para mostrar as porcentagens.
  wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: percentage_helper(pct, data), textprops=dict(color="w"), startangle=45)
  # Definindo a caixa de legenda externa, título, localização e aonde a legenda ficará colada no fundo.
  ax.legend(wedges, results, title="Tipos de Detecções", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
  # Definindo o tamanho do texto vai ser mostrado.
  plot.setp(autotexts, size=12, weight="bold")
  # Mostrando o título do gráfico.
  ax.set_title("Quantidade de detecções")
  # Mostrando o gráfico.
  plot.show()

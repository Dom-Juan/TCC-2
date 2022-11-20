import matplotlib.pyplot as plot
plot.style.use('ggplot')

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
  plot.legend()
  plot.subplot(1, 2, 2)
  plot.plot(x, loss, 'b', label='Perca/loss no treinamento')
  plot.plot(x, val_loss, 'r', label='Perca/loss na validação')
  plot.title('Treinamento e validação de perca/loss.')
  plot.legend()

def plot_history_accuracy(history):
  plot.plot(history.history['accuracy'])
  plot.plot(history.history['val_accuracy'])
  plot.title('model accuracy')
  plot.ylabel('acurácia')
  plot.xlabel('épocas')
  plot.legend(['treino', 'teste'], loc='upper left')
  plot.show()

def plot_history_loss(history):
  plot.plot(history.history['loss'])
  plot.plot(history.history['val_loss'])
  plot.title('model loss')
  plot.ylabel('perca')
  plot.xlabel('épocas')
  plot.legend(['treino', 'teste'], loc='upper left')
  plot.show()

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
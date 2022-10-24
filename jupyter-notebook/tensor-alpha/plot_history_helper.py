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
  plot.plot(x, accuracy, 'b', label='Precisão de treinamento')
  plot.plot(x, val_accuracy, 'r', label='Validação de precisão')
  plot.title('Treinamento e validação de precisão')
  plot.legend()
  plot.subplot(1, 2, 2)
  plot.plot(x, loss, 'b', label='Perca/loss no treinamento')
  plot.plot(x, val_loss, 'r', label='Perca/loss na validação')
  plot.title('Treinamento e validação de perca/loss.')
  plot.legend()

import matplotlib.pyplot as plot
plot.style.use('ggplot')

def plot_history(history):
  acc = history.history['acc']
  val_acc = history.history['val_acc']
  loss = history.history['loss']
  val_loss = history.history['val_loss']
  x = range(1, len(acc) + 1)

  plot.figure(figsize=(12, 5))
  plot.subplot(1, 2, 1)
  plot.plot(x, acc, 'b', label='Training acc')
  plot.plot(x, val_acc, 'r', label='Validation acc')
  plot.title('Training and validation accuracy')
  plot.legend()
  plot.subplot(1, 2, 2)
  plot.plot(x, loss, 'b', label='Training loss')
  plot.plot(x, val_loss, 'r', label='Validation loss')
  plot.title('Training and validation loss')
  plot.legend()

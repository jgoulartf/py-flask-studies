from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import Accuracy, Precision, Recall
from tensorflow.keras.utils import to_categorical
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Gerar dados de exemplo
X, y = make_classification(n_samples=1000, n_classes=2, random_state=1)
y = to_categorical(y)

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Definir o modelo
model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compilar o modelo, definindo as métricas que deseja usar
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=[Accuracy(), Precision(), Recall()])

# Treinar o modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

# Avaliar o modelo nos dados de teste
test_loss, test_acc, test_precision, test_recall = model.evaluate(X_test, y_test, verbose=0)

# Imprimir as métricas
print('Test Loss: ', test_loss)
print('Test Accuracy: ', test_acc)
print('Test Precision: ', test_precision)
print('Test Recall: ', test_recall)
### Prerequisites
Scikit Learn, Pandas, numpy, openpyxl and Flask (for API).

создать виртуальную среду Python с помощью команды:
```
python3 -m venv cluster-env
```

Активируйте среду, используя:
1. mac
```
source cluster-env/bin/activate
```

2. windows 
```
tutorial-env\Scripts\activate.bat
```
Выполните команду ниже, чтобы установить необходимое.

```
pip3 install -r requirements.txt
```

### Running the project
1. Создайте модель машинного обучения, выполнив команду ниже -
```
python model.py
```
Это создаст сериализованную версию нашей модели в файле model.pkl.

2. Запустите app.py, используя команду ниже, чтобы запустить Flask API.
```
python app.py
```
3. Перейти к URL http://localhost:5000

Введите действительные числовые значения во все 4 поля ввода и нажмите «Predict».

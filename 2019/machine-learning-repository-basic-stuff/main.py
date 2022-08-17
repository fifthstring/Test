import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
#from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
import os


from sklearn.metrics import accuracy_score
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis=1)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']
from sklearn import preprocessing

train_x = preprocessing.scale(train_x)
test_x = preprocessing.scale(test_x)


model = RandomForestClassifier()

x = model.fit(train_x,train_y,epochs = 100,batch_size = 24)

#print('Depth of the Decision Tree :', model.get_depth())

predict_train = model.predict(train_x)
print('Target on train data',predict_train)
accuracy_train = accuracy_score(train_y,predict_train)
print('accuracy on train: ', accuracy_train)
predict_test = model.predict(test_x)
#print('Target on test data',predict_test)
accuracy_test = accuracy_score(test_y,predict_test)
print('accuracy on test: ', accuracy_test)

single_x_test = [1.0,37.0042,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0
]
single_x_test= preprocessing.scale(single_x_test)
q = model.predict( np.array( [single_x_test] )  )

'''
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis=1)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']

preprocessing.scale(train_x)
preprocessing.scale(test_x)

model = RandomForestClassifier()
model.fit(train_x,train_y)
pt=  model.predict(test_x)

accuracy_test = accuracy_score(test_y,pt)
print('accuracy on test: ', accuracy_test)

'''







'''
import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis = 1)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis = 1)
test_y = test_data['Survived']

train_x = preprocessing.scale(train_x)
test_x = preprocessing.scale(test_x)

model= DecisionTreeClassifier()

model.fit(train_x,train_y)
predict_train = model.predict(train_x)
predict_test = model.predict(test_x)
accuracy_tr = accuracy_score(train_y,predict_train)
accuracy_te = accuracy_score(test_y,predict_test)

print('Test acc.:',accuracy_te)
single_x_test = [1.0,37.0042,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0
]
single_x_test= preprocessing.scale(single_x_test)
q = model.predict( np.array( [single_x_test] )  )
'''
'''
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
train = pd.read_csv('train-data.csv')
test = pd.read_csv('test-data.csv')

x = train.drop(columns = ['Survived'],axis = 1)
y = train['Survived']
xt = test.drop(columns = ['Survived'],axis = 1)
yt = test['Survived']

x = preprocessing.scale(x)
xt = preprocessing.scale(xt)


model = RandomForestClassifier()
model.fit(x,y)

tpred = model.predict(x)
pred = model.predict(xt)

a = accuracy_score(y,tpred)
b = accuracy_score(yt,pred)

print('test acc:',b)
'''

'''
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

train = pd.read_csv('train-data.csv')
test = pd.read_csv('test-data.csv')

trx = train.drop(columns = ['Survived'],axis = 1)
tex = test.drop(columns = ['Survived'],axis = 1)
tr = train['Survived']
te = test['Survived']

preprocessing.scale(trx)
preprocessing.scale(tex)

model = RandomForestClassifier()
model.fit(trx,tr)


tpred = model.predict(tex)
tac = accuracy_score(te,tpred)

print('Acc:', tac)
'''


'''
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

xx = pd.read_csv('train-data.csv')
xxx = pd.read_csv('test-data.csv')

X = xx.drop(columns = ['Survived'],axis = 1)
y = xx['Survived']

Xt = xxx.drop(columns = ['Survived'],axis = 1)
yt = xxx['Survived']

X = preprocessing.scale(X)
Xt = preprocessing.scale(Xt)

model = DecisionTreeClassifier()
model.fit(X,y)

pred = model.predict(Xt)

accurac = accuracy_score(yt,pred)

print('Acc:',accurac)
'''


'''
import pandas as pd
import numpy as np
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis=1)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']
model = LogisticRegression()
model.fit(train_x,train_y)
'''
#print('Depth of the Decision Tree :', model.get_depth())
'''
predict_train = model.predict(train_x)
print('Target on train data',predict_train)
accuracy_train = accuracy_score(train_y,predict_train)
print('accuracy on train: ', accuracy_train)
predict_test = model.predict(test_x)
#print('Target on test data',predict_test)
accuracy_test = accuracy_score(test_y,predict_test)
print('accuracy on test: ', accuracy_test)

single_x_test = [1.0,37.0042,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0
]
q = model.predict( np.array( [single_x_test,] )  )


'''
'''
from sklearn import preprocessing
import pandas as pd
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis=1)
preprocessing.scale(train_x)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']
preprocessing.scale(test_x)

from keras.models import Sequential
from keras.layers import Dense
c = Sequential()
c.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 24))
c.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'relu'))
c.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'relu'))
c.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
c.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])
epochs = c.fit(train_x, train_y, epochs=100, batch_size=64)
y_pred = c.predict(test_x)

y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_y, y_pred)
t = cm[0][0] + cm[1][1]
r = cm[0][1] + cm[1][0]
print('Accuracy on test data:',(t/(t+r)) * 100)

'''
'''
from sklearn import preprocessing
import pandas as pd
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis=1)
preprocessing.scale(train_x)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']
preprocessing.scale(test_x)
'''
'''
from keras.models import Sequential
from keras.layers import Dense
from sklearn import preprocessing

model = Sequential()
model.add(Dense(units = 6, kernel_initializer='normal', activation = 'relu',input_dim = 24))
model.add(Dense(units = 64, kernel_initializer='normal', activation = 'relu'))

model.add(Dense(units = 64, kernel_initializer='normal', activation = 'relu'))
model.add(Dense(units = 1, kernel_initializer='normal',activation = 'sigmoid'))

model.compile(optimizer = 'rmsprop',loss = 'binary_crossentropy',metrics = ['accuracy'])
train = model.fit(train_x,train_y,epochs = 200, batch_size = 64)
pred = model.predict(test_x)
pred = pred > 0.5
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_y,pred)



t = cm[0][0] + cm[1][1]
r = cm[0][1] + cm[1][0]
print('Accuracy on test data:',(t/(t+r)) * 100)

'''
'''
from keras.layers import Dense
from keras.models import Sequential
from keras import preprocessing

m = Sequential()
m.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'relu' , input_dim = 24 ))
m.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu' ))
m.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu' ))
m.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu' ))
m.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'sigmoid' ))
m.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy',metrics = ['accuracy'])
e = m.fit(train_x,train_y,epochs = 100,batch_size = 64)
pred = m.predict(test_x)
pred = pred > 0.5
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_y,pred)

t = cm[0][0] + cm[1][1]
r = cm[0][1] + cm[1][0]
print('Accuracy on test data:',(t/(t+r)) * 100)

'''

'''

from sklearn import preprocessing
import pandas as pd
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')
train_x = train_data.drop(columns=['Survived'],axis=1)
preprocessing.scale(train_x)
train_y = train_data['Survived']
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']
preprocessing.scale(test_x)


from keras.layers import Dense
from keras.models import Sequential
from sklearn.metrics import confusion_matrix

model = Sequential()
model.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'relu',input_dim = 24))
model.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'sigmoid'))

model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy',metrics = ['accuracy'])
e = model.fit(train_x,train_y,epochs = 100,batch_size = 64)
pred = model.predict(test_x)
pred = pred > 0.5
cm = confusion_matrix(test_y,pred)

'''






'''
from sklearn import preprocessing
from keras.layers import Dense
from keras.models import Sequential 

model = Sequential()
model.add(Dense(units= 1, kernel_initializer = 'normal',activation = 'relu', input_dim = 24))
model.add(Dense(units= 32, kernel_initializer = 'normal',activation = 'relu'))
model.add(Dense(units= 64, kernel_initializer = 'normal',activation = 'relu'))
model.add(Dense(units= 32, kernel_initializer = 'normal',activation = 'relu'))
model.add(Dense(units= 1, kernel_initializer = 'normal',activation = 'sigmoid'))
model.compile(optimizer = 'rmsprop',loss = 'binary_crossentropy', metrics = ['accuracy'])
e = model.fit(train_x,train_y,epochs = 10, batch_size = 24)

pred = model.predict(test_x)
from sklearn.metrics import confusion_matrix
pred = pred > 0.5
cm = confusion_matrix(test_y,pred)
'''

'''
import pandas as pd
from keras.ensemble import RandomForestClassifier
from keras import preprocessing
from keras.layers import Dense
from keras.models import Sequential
import os
os.environ['KERAS_BACKEND'] = 'theano'
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

train_x = train_data.drop(columns = ['Survived'],axis = 1)

train_y= train_data['Survived']

test_x = test_data.drop(columns = ['Survived'],axis = 1)

test_y = test_data['Survived']

preprocessing.scale(train_x)
preprocessing.scale(test_x)

model = Sequential()
model.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'relu', input_dim = 24))
model.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 64, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'sigmoid'))
e = model.fit(train_x,train_y, epochs = 100, batch_size = 24)
from sklearn.metrics import confusion_matrix
pred = model.predict(test_x)
pred = pred > 0.5
cm = confusion_matrix(test_y,pred)
'''
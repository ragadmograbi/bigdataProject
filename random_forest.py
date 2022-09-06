
from exploratory_data import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics



# Putting feature variable to X
X = not_null_data.drop('class',axis=1)
# Putting response variable to y
y = target

#convert the vals(chars) in the data frame to int/float
def charToInt(arr):
    new_arr = []
    for x in arr:
        if type(x) == float :
            new_arr.append(x)
            continue
        new_arr.append(ord(x)-ord('a'))
    new_arr = np.array(new_arr)
    return new_arr


X = X.apply(lambda x : charToInt(x), axis=0)

# now lets split the data into train and test
from sklearn.model_selection import train_test_split



# Splitting the data into train and test
def splitting_data1():

    print("splitting the data into train and test 70-30")
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)
    print("X_train shape = ", X_train.shape)
    print("X_test shape = ", X_test.shape)
    print("y_train shape = ", y_train.shape)
    print("y_test shape = ", y_test.shape)

    rf = RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    #add index to the rf pred
    rf_pred_data_frame = pd.DataFrame(data=rf_pred, index=y_test.index)

    plt.subplot(2,1,1)
    plt.plot(rf_pred_data_frame.iloc[:,0],'r.',
             y_test,'b*')
    plt.subplot(2,1,2)
    plt.plot(y_test,'b*',
             rf_pred_data_frame.iloc[:,0],'r.')
    plt.show()

    print(f"Random Forest accuracy: {metrics.accuracy_score(y_test,rf_pred)}")
    print(confusion_matrix(y_test, rf_pred))



#another way to split the data 50-30-20
def splitting_data2():
    print("another way to split the data 50-30-20")
    X_train2, X_other, y_train2, y_other = train_test_split(X, y, train_size=0.5, random_state=42)
    X_validation, X_test2, y_validation,y_test2 = train_test_split(X_other, y_other, train_size=0.3, random_state=42)

    print("X_train2 shape = ", X_train2.shape)
    print("X_test2 shape = ", X_test2.shape)
    print("X_validation shape = ", X_validation.shape)

    print("y_train2 shape = ", y_train2.shape)
    print("y_test2 shape = ", y_test2.shape)
    print("y_validation shape = ", y_validation.shape)

    rf2 = RandomForestClassifier(n_estimators=100).fit(X_train2, y_train2)
    rf_pred_test2 = rf2.predict(X_test2)
    rf_pred_validation = rf2.predict(X_validation)
    print(f"Random Forest accuracy: {metrics.accuracy_score(y_test2,rf_pred_test2)}")
    print(confusion_matrix(y_test2, rf_pred_test2))

    print("validation")
    print(f"Random Forest accuracy: {metrics.accuracy_score(y_validation,rf_pred_validation)}")
    print(confusion_matrix(y_validation, rf_pred_validation))

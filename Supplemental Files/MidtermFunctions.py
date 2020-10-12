#the following is from the Lecture 6 demo notebook

import matplotlib.pyplot as plt
from sklearn import tree
def draw_tree(estimator, feature_names, filename):
    """
    Takes Tree model estimator and plots it's tree structure.
    estimator is a fitted model
    feature_names is a list of strings
    takes a file name for the saved image
    It returns a plot of the decision tree and a saved image
    """
    fig = plt.figure(figsize= (15,15))
    tree.plot_tree(estimator, 
                   feature_names= feature_names,
                   class_names = ['Bad Wine', 'Just Okay Wine', 'Good Wine'],
                    filled=True)
    fig.savefig(filename)
    
from sklearn.metrics import classification_report     
from sklearn.model_selection import cross_val_score #https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation used this page to determine how to use this
def Accuracy(estimator, X, y, cv, X_test,y_test):
    """
    This automates the print function along with the cross validation score to simplify the code in the notebook
    takes the fitted model (estimator)
    The predictor data, X, and the target data, y
    cv is the number of folds used in the cross validation
    Output is an accuracy estimat and the classification report
    """
    scores = cross_val_score(estimator, X, y, cv=cv)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    pred = estimator.predict(X_test)
    print('Classification Report')
    print(classification_report(y_test, pred, zero_division = 0))
    
from sklearn.metrics import classification_report #https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html
from sklearn.metrics import confusion_matrix #https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

def VizConfusionMatrix(estimator, X_test, y_test):
    """
    This produces a vizualisation of a confusion matrix for a given 
    fitted model 'estimator'. It takes the test data and outputs a viz of the matrix
    """
    pred = estimator.predict(X_test)
    cm = confusion_matrix(y_test, pred)
    
    labels = ['Bad','Good', 'Okay']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm)
    plt.title('Confusion matrix of the classifier')
    fig.colorbar(cax)
    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
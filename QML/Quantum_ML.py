#Copyright Brian Haney 2021
# AlgoBoost
# QNN for BSD
# import numpy
import numpy as np
# import data

# Load data set
# All rational points on an elliptic curve
# Shuffle data for random selection for training and test data
idx = np.arange(len(data.target))
np.random.shuffle(idx)

# Use 2/3 of data set for training, 1/3 for testing
idx_train = idx[:2*len(idx)//3]
idx_test = idx[2*len(idx)//3:]

# Set up data points for training and testing
X_train = data.data[idx_train]
X_test = data.data[idx_test]

# Set up labels for training and testing.
y_train = 2 * data.target[idx_train] - 1  
y_test = 2 * data.target[idx_test] - 1

#Dataset information
print("Training data size: \t%d samples with %d features" %(X_train.shape[0], X_train.shape[1]))
print("Testing data size: \t%d samples" %(X_test.shape[0]))
print('---------------------------------------')

#Decision Tree, Random Forest, and algoboost are Classical Algorithms
#Decision Tree Function
def Decision_Tree(X_train, y_train, X_test, y_test):
    from sklearn import tree
    clf1 = tree.DecisionTreeClassifier()
    clf1.fit(X_train, y_train)
    y_train1 = clf1.predict(X_train)
    y_test1 = clf1.predict(X_test)
    from sklearn.metrics import accuracy_score
    print('Accuracy for training data: \t', (accuracy_score(y_train, y_train1)))
    print('Accuracy for test data: \t', (accuracy_score(y_test, y_test1)))
    return clf1
    
clf1 = Decision_Tree(X_train, y_train, X_test, y_test)

#Random Forest Function
def Random_Forest(X_train, y_train, X_test, y_test):
    from sklearn.ensemble import RandomForestClassifier
    clf2 = RandomForestClassifier(max_depth=2, n_estimators=30)
    clf2.fit(X_train, y_train)
    y_train2 = clf2.predict(X_train)
    y_test2 = clf2.predict(X_test)
    from sklearn.metrics import accuracy_score
    print('Accuracy during training: \t', (accuracy_score(y_train, y_train2)))
    print('Accuracy during test data: \t', (accuracy_score(y_test, y_test2)))
    return clf2

clf2 = Random_Forest(X_train, y_train, X_test, y_test)

#algoboost Function
def algoboost(X_train, y_train, X_test, y_test):
    from sklearn.ensemble import algoboostClassifier
    clf3 = algoboostClassifier(n_estimators=30)
    clf3.fit(X_train, y_train)
    y_train3 = clf3.predict(X_train)
    y_test3 = clf3.predict(X_test)
    from sklearn.metrics import accuracy_score
    print('Accuracy during training: \t', (accuracy_score(y_train, y_train3)))
    print('Accuracy during training: \t', (accuracy_score(y_test, y_test3)))
    return clf3
    
clf3 = algoboost(X_train, y_train, X_test, y_test)

#QBoost and QBoost Plus are quantum algorithms
#QBoost and QBoost Plus require DWave resources to successfully run
#QBoost Function

def QBoost(X_train, y_train, X_test, y_test):
    NUM_READS = 1000
    DW_PARAMS = {'num_reads': NUM_READS,
                 'auto_scale': True,
                 'num_spin_reversal_transforms': 10,
                 'postprocess': 'optimization',
                 }

    from dwave.system.samplers import DWaveSampler
    from dwave.system.composites import EmbeddingComposite
    dwave_sampler = DWaveSampler(solver={'qpu': True}) 
    emb_sampler = EmbeddingComposite(dwave_sampler)
    from qboost import WeakClassifiers, QBoostClassifier
    clf4 = QBoostClassifier(n_estimators=30, max_depth=2)
    clf4.fit(X_train, y_train, emb_sampler, lmd=1.0, **DW_PARAMS)
    y_train4 = clf4.predict(X_train)
    y_test4 = clf4.predict(X_test)
    from sklearn.metrics import accuracy_score
    print('Accuracy for training data: \t', (accuracy_score(y_train, y_train4)))
    print('Accuracy for test data: \t', (accuracy_score(y_test, y_test4)))
    return clf4
clf4 = QBoost(X_train, y_train, X_test, y_test)

#QBoost Plus Function
def QBoostPlus(X_train, y_train, X_test, y_test, clf1, clf2, clf3, clf4):
    NUM_READS = 1000
    DW_PARAMS = {'num_reads': NUM_READS,
                 'auto_scale': True,
                 'num_spin_reversal_transforms': 10,
                 'postprocess': 'optimization',
                 }

    from dwave.system.samplers import DWaveSampler
    from dwave.system.composites import EmbeddingComposite

    dwave_sampler = DWaveSampler(solver={'qpu': True})
    emb_sampler = EmbeddingComposite(dwave_sampler)
    
    from qboost import QboostPlus

    clf5 = QboostPlus([clf1, clf2, clf3, clf4])
    clf5.fit(X_train, y_train, emb_sampler, lmd=0.2, **DW_PARAMS)
    y_train5 = clf5.predict(X_train)
    y_test5 = clf5.predict(X_test)

    from sklearn.metrics import accuracy_score

    print('Accuracy for training data: \t', (accuracy_score(y_train, y_train5)))
    print('Accuracy for test data: \t', (accuracy_score(y_test, y_test5)))
    
    return clf5
    
clf5 = QBoostPlus(X_train, y_train, X_test, y_test, clf1, clf2, clf3, clf4)

#Print Results
print('---------------------------------------')
# Decision Tree
print('Tree: ')
clf1 = Decision_Tree(X_train, y_train, X_test, y_test)
print('---------------------------------------')
# Random Forest
print('Forest: ')
clf2 = Random_Forest(X_train, y_train, X_test, y_test)
print('---------------------------------------')
# algoboost
print('algoboost: ')
clf3 = algoboost(X_train, y_train, X_test, y_test)
print('---------------------------------------')
# QBoost
print('QBoost: ')
clf4 = QBoost(X_train, y_train, X_test, y_test) 
print('---------------------------------------')
# QBoostPlus
print('QBoostPlus: ')
clf5 = QBoostPlus(X_train, y_train, X_test, y_test, clf1, clf2, clf3, clf4) 
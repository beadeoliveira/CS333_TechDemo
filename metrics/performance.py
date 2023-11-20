#Performance Metrics

#Precision: ratio of true positives to overall prediction
def precision(truepos, falsepos):
    precision = truepos / (truepos +falsepos)
    return precision

#Recall: ratio of correct predictions and all correct observations in sample space
def recall(truepos, falseneg):
    recall = truepos / (truepos + falseneg)
    return recall

#F1:  weighted harmonic mean of precision and recall
def f1(precision, recall):
    f1 = 2 * ((precision * recall) / (precision + recall))
    return f1

#Accuracy: ratio of correct predictions to overall observations
def accuracy(truepos, trueneg, falsepos, falseneg):
    accuracy = (truepos + trueneg) / (truepos + falsepos + falseneg + trueneg)
    return accuracy
'''
Created on May 7, 2011

@author: "Carsten Witzke"
'''
from de.staticline.tools.libsvmtools import LibsvmFileImporter
from de.staticline.regression.simpleregression import RidgeRegression


def regressionDemo():
    # get data sets from file
    trainingSet = LibsvmFileImporter('data/regression/cadata.txt').get_dataSet()
    #testSet = LibsvmFileImporter('data/lin_reg.t').get_dataSet()
    
    # make new ridge regression
    rr = RidgeRegression()
    
    for i in range(5):
        # optional: set complexity parameter
        rr.set_lambda(i) # 0: linear regression w/o regularization
        # train the model
        rr.trainModel(trainingSet)
        # get model
        #print 'model:\n%s' % rr.get_model()
        # get RSS
        print u'RSS(\u03bb=%d): %f' % (rr.get_lambda(),rr.get_rss())
        # validation
        #rr.validate_model(testSet) #currently not implemented

if __name__ == '__main__':
    regressionDemo()
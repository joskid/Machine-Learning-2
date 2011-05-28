#!/usr/bin/python
'''
Created on May 28, 2011

@author: Carsten Witzke
'''
import sys
import getopt
from de.staticline.classification.svmlinear import DualCoordinateDescent
from de.staticline.classification.dummys import Always1Predictor
from de.staticline.classification.svm import SMO_Keerthi
import os
from de.staticline.tools.libsvmtools import LibsvmFileImporter
from de.staticline.kernels.kernels import poly

def main(argv):
    ## get arguments
    try:
        opts, args = getopt.getopt(argv, 'hc:', ['help','classifier=','training-file=','test-file='])
    except getopt.GetoptError, error:
        print str(error)
        usage()
        sys.exit(2)
    
    ## handle arguments
    classifier = None
    cParameters = None
    trainingFile = None
    testFile = None
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        if opt in ('-c', '--classifier'):
            if arg == 'svm-cd':
                classifier = DualCoordinateDescent()
            elif arg == 'dummy':
                classifier = Always1Predictor()
            elif arg == 'svm-smo-keerthi':
                #classifier = SMO_Keerthi() #TODO: implement
                pass
            else:
                print 'Sorry, this classifier is currently not implemented :('
                sys.exit()
        if opt == '--training-file':
            if os.path.exists(arg):
                trainingFile = arg
            else:
                print 'It seems that the training file you specified does not exist. Please check path.'
                sys.exit()
        if opt == '--test-file':
            if os.path.exists(arg):
                testFile = arg
            else:
                print 'It seems that the test file you specified does not exist. Please check path.'
                sys.exit()
    
    ## process input
    if classifier == None:
        print 'No classifier specified.'
        usage()
        sys.exit()
    if trainingFile == None:
        print 'No training file specified.'
        usage()
        sys.exit()
    if testFile == None:
        print 'No test file specified.'
        usage()
        sys.exit()
    training = LibsvmFileImporter(trainingFile).get_dataSet()
    testing = LibsvmFileImporter(testFile).get_dataSet()
    
    #TODO: parameter handling
    complexity = 1
    accuracy = 1e-10
    kernel = poly
    classifier.train(training.get_features(), training.get_targets(), complexity, accuracy, kernel)    
    
        
def usage(): #TODO: improve
    print '''usage: {file} [options]
    
    -h, --help                                        display this usage information
    -c, --classifier=svm-cd|svm-smo-keerti|dummy      select a classifier
    # options
    --training-file=FILE                              read training data from FILE
    --test-file=FILE                                  evaluate on FILE
'''.format(file=__file__)

if __name__ == '__main__':
    main(sys.argv[1:])
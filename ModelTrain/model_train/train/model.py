from sklearn.svm import SVC
from sklearn.ensemble import  RandomForestClassifier
from model_train.configs.config import CLASSIFIER_TYPE, RANDOM_STATE
from model_train.utils.logger import logger

def build_classifier():
    
    try :
        if CLASSIFIER_TYPE == 'svm':
            cls = SVC(kernel='linear', 
                    probability=True,
                    random_state=RANDOM_STATE)
        elif CLASSIFIER_TYPE == 'random_forest':
            cls = RandomForestClassifier(n_estimators=100, 
                                    random_state=RANDOM_STATE)
        else :
            raise ValueError(f"Invalid classifier {CLASSIFIER_TYPE}. Use 'svm' or 'random_forest'")
        
        return cls
    except ValueError as e:
        logger.warning(f"{e} . Se usara SVM por defecto")
        
        cls = SVC(kernel='linear', probability=True, random_state=RANDOM_STATE)
        return cls
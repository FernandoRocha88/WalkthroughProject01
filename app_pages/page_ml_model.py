import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import clf_performance_train_validation_test_set


def page_ml_model_body():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Traninig Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Traninig Losses')
    st.write("---")

    st.write("### Performance on Train, Validation and Test Set")
    clf_performance_train_validation_test_set(version=version)
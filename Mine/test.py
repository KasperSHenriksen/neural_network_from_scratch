import numpy as np
import neuralnetwork as nn
#from NeuralNetwork import ActivationFunctions as af



model = nn.neuralnetwork.Model()
model.add(nn.Layer(input_size=2,output_size=3,activation=af.ReLU))
model.add(nn.Layer(input_size=3,output_size=3,activation=Activation_Functions.ReLU))
model.add(nn.Layer(input_size=3,output_size=2,activation=Activation_Functions.ReLU))
model.add(nn.Layer(input_size=2,output_size=2,activation=Activation_Functions.softmax))
model.summary()

# EPOCHS = 5
# for epoch in range(0,EPOCHS):
#     print(f'____Epoch {epoch}______')
data = [3,2]
outcome = model.forward_propagation(data)

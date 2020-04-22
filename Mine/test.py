import numpy as np
from MyNeuralNetwork import neuralnetwork as nn
#from MyNeuralNetwork import activationfunctions as activation

model = nn.neuralnetwork.Model()
model.add(nn.Layer(input_size=2,output_size=3,activation=af.ReLU))
model.add(nn.Layer(input_size=3,output_size=3,activation=activation.ReLU))
model.add(nn.Layer(input_size=3,output_size=2,activation=activation.ReLU))
model.add(nn.Layer(input_size=2,output_size=2,activation=activation.softmax))
model.summary()

# EPOCHS = 5
# for epoch in range(0,EPOCHS):
#     print(f'____Epoch {epoch}______')
data = [3,2]
outcome = model.forward_propagation(data)

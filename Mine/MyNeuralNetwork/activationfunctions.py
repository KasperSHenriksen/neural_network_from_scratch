from MyNeuralNetwork import neuralnetwork as nn

class Activation_Functions(nn):
    def __init__(self):
        pass

    def ReLU(neurons):
        temp_list = []
        for neuron in neurons:
            temp_list.append(np.maximum(0,neuron.value))
        return temp_list

    def softmax(neurons):
        total = 0
        for neuron in neurons:
            if neuron.value < 0:
                neuron.value = 0.0001
            total += neuron.value

        temp_list = []
        for neuron in neurons:
            temp_list.append(neuron.value/total)
        return temp_list

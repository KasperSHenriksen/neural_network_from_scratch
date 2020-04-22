import numpy as np

class Neuron:
    def __init__(self,bias,weights,value):
        self.bias = bias
        self.weights = weights
        self.value = value


class Layer:
    def __init__(self,input_size,output_size,activation):
        self.neurons = []
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation

        for i in range(0,self.input_size):
            #CHANGE LATER UNIFORM
            bias = 1 #np.random.uniform(-5,5)
            value = 0 #np.random.uniform(-5,5)

            weights = []
            for j in range(0,self.output_size):
                weights.append(np.random.uniform(-10,20))

            neuron = Neuron(bias,weights,value)
            self.neurons.append(neuron)

    def get_neuron_by_index(self,index):
        return self.neurons[index]

    def get_input_and_output_sizes(self):
        return self.input_size, self.output_size

    def size(self):
        return len(self.neurons)

class Model:
    def __init__(self):
        self.layers = []

    def add(self,layer):
        self.layers.append(layer)

    def forward_propagation(self,x):
        #First layer:
        for i in range(0,len(x)):
            self.layers[0].neurons[i].value = x[i]

        for layer_idx, layer in enumerate(self.layers):
            #Skip if first layer
            if layer_idx == 0:
                continue

            #For other layers
            for current_neuron_idx, current_neuron in enumerate(layer.neurons):
                value = 0
                for previous_neuron_idx, previous_neuron in enumerate(self.layers[layer_idx-1].neurons):
                    value += previous_neuron.value * previous_neuron.weights[current_neuron_idx]
                    #print(f'{previous_neuron.value} and {previous_neuron.weights[previous_neuron_idx]} equals: {value}')
                value += current_neuron.bias
                current_neuron.value = value

            #Using activation at each value
            for idx, new_value in enumerate(layer.activation(layer.neurons)):
                layer.neurons[idx].value = new_value

        #Print all neurons, just for debugging
        for i, layer in enumerate(self.layers):
            for neuron in layer.neurons:
                #print(f'Layer {i}: Neuron Value: {neuron.value}')
                pass

        return self.layers[len(self.layers)-1].neurons

    def summary(self):
        for i in range(0,len(self.layers)):
            input_size, output_size = self.layers[i].get_input_and_output_sizes()
            self.layers[i].activation
            print(f'[Layer {i}] Input size: {input_size}. Output size: {output_size}.')

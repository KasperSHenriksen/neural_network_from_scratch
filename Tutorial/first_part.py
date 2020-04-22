inputs = [1, 2, 3, 2.5]

weights1 = [0.2,0.8,-0.5,1.0]
weights2 = [0.5,-10.91,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5




output=[inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3]+bias1,
        inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3]+bias2,
        inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3]+bias3]

print(output)







inputs = [1.4,1.2,2.5]

weights1 = [0.2,0.8,-0.5]
weights2 = [0.5,-10.91,0.26]
weights3 = [0.1,-5.91,-0.3]
weights4 = [1.5,-2.5,0.9]
weights5 = [5.2,-0.21,3.41]

bias1 = 2
bias2 = 1.5
bias3 = 3.5
bias4 = 2.5
bias5 = 5.5

output=[inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + bias1,
        inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + bias1,
        inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + bias1,
        inputs[0]*weights4[0] + inputs[1]*weights4[1] + inputs[2]*weights4[2] + bias1,
        inputs[0]*weights5[0] + inputs[1]*weights5[1] + inputs[2]*weights5[2] + bias1,
        ]

print(output)






for i in range(0,current_layer.size()): #Go through each neuron in list
    output_value = 0
    for j in range(0,previous_layer.size()): #Go through each connected neuron
        output_value += previous_neuron_list[j].value * current_layer_list[i].weights[j]
    output_value += current_layer_list[i].bias
    current_layer_list[i].value = output_value

for i in range(0,3):
    print(current_layer_list[i].value)


            # for idx, layer in enumerate(self.layers):
            #     if idx == 0:
            #         continue
            #
            #     for neuron in layer.neurons:
            #         for neuron in layer


            # for i in range(0,self.layers[1].size()): #Go through each neuron in list
            #     output_value = 0
            #     for j in range(0,self.layers[0].size()): #Go through each connected neuron
            #         print(self.layers[1].get_neuron_by_index(i).weights[j])
            #         output_value += self.layers[0].get_neuron_by_index(j).value * self.layers[1].get_neuron_by_index(i).weights[j]
            #     output_value += self.layers[1].get_neuron_by_index(i).bias
            #     self.layers[1].get_neuron_by_index(i).value = output_value
            #
            # for i in range(0,3):
            #     print(self.layers[1].get_neuron_by_index(i).value)

import random

attributes = [['Sunny','Rainy'],
              ['Warm','Cold'],
              ['Normal','High'],
              ['Strong','Weak'],
              ['Warm','Cool'],
              ['Same','Change']]

num_attributes = len(attributes)

def getRandomTrainingExample(target_concept = ['?'] * num_attributes):
    training_example = []
    classification = True
    for i in range(num_attributes):
        training_example.append(attributes[i][random.randint(0,1)])
        if target_concept[i] != '?' and target_concept[i] != training_example[i]:
            classification = False
    return training_example, classification

def findS(training_examples = []):
    hypothesis = ['0'] * num_attributes
    for example in training_examples:
        if example[1]:
            for i in range(num_attributes):
                example_attribute = example[0][i]
                hypothesis_attribute = hypothesis[i]
                if example_attribute == attributes[i][0]:
                    if hypothesis_attribute == '0':
                        hypothesis_attribute = attributes[i][0]
                    elif hypothesis_attribute == attributes[i][1]:
                        hypothesis_attribute = '?'
                elif example_attribute == attributes[i][1]:
                    if hypothesis_attribute == '0':
                        hypothesis_attribute = attributes[i][1]
                    elif hypothesis_attribute == attributes[i][0]:
                        hypothesis_attribute = '?'
                hypothesis[i] = hypothesis_attribute
    return hypothesis

def experiment(target_concept = ['?'] * num_attributes):
    training_examples = []
    while findS(training_examples) != target_concept:
        training_examples.append(getRandomTrainingExample(target_concept))
    return len(training_examples)

def main():
    target_concept = ['Sunny','Warm','?','?','?','?']
    num_experiments = 1000
    experiment_results = []
    for i in range(num_experiments):
        experiment_results.append(experiment(target_concept))
    average_result = sum(experiment_results) / num_experiments

    print(str(len(experiment_results)) + ' Experiments Ran')
    print('Average # Examples Required: ' + str(average_result))
    print('Target Concept:' + str(target_concept))

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from sklearn import datasets
from genetic_algorithm import genetic_algorithm
from tqdm import tqdm
import matplotlib.pyplot as plt

def normalize_dataset(dataset):
    # Normalize the dataset to [0, 1]
    min_arr = np.amin(dataset, axis=0)
    return (dataset - min_arr) / (np.amax(dataset, axis=0) - min_arr)


def evaluate_new_fuzzy_system(w1, w2, w3, w4, data, target):
    universe = np.linspace(0, 1, 100)

    x = []
    for w in [w1, w2, w3, w4]:
        x.append({'s': fuzz.trimf(universe, [0.0, 0.0, w]),
                  'm': fuzz.trimf(universe, [0.0, w, 1.0]),
                  'l': fuzz.trimf(universe, [w, 1.0, 1.0])})

    x_memb = []
    for i in range(4):
        x_memb.append({})
        for t in ['s', 'm', 'l']:
            x_memb[i][t] = fuzz.interp_membership(universe, x[i][t], data[:, i])

    is_setosa = np.fmin(np.fmax(x_memb[2]['s'], x_memb[2]['m']), x_memb[3]['s'])
    is_versicolor = np.fmax(np.fmin(
        np.fmin(np.fmin(np.fmax(x_memb[0]['s'], x_memb[0]['l']), np.fmax(x_memb[1]['m'], x_memb[1]['l'])),
                np.fmax(x_memb[2]['m'], x_memb[2]['l'])), x_memb[3]['m']), np.fmin(x_memb[0]['m'], np.fmin(
        np.fmin(np.fmax(x_memb[1]['s'], x_memb[1]['m']), x_memb[2]['s']), x_memb[3]['l'])))
    is_virginica = np.fmin(np.fmin(np.fmax(x_memb[1]['s'], x_memb[1]['m']), x_memb[2]['l']), x_memb[3]['l'])

    result = np.argmax([is_setosa, is_versicolor, is_virginica], axis=0)

    return (result == target).mean()


def main():
    iris = datasets.load_iris()
    normalized_iris = normalize_dataset(iris.data)
    n_features = normalized_iris.shape[1]

    fitness = lambda w: 1.0 - evaluate_new_fuzzy_system(w[0], w[1], w[2], w[3], normalized_iris, iris.target)

    record = {'GA': []}

    for _ in tqdm(range(30)):
        # GA
        best, fbest = genetic_algorithm(fitness_func=fitness, dim=n_features, n_individuals=10, epochs=30, verbose=False)
        record['GA'].append(1.0 - fbest)

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.boxplot(list(record.values()), vert=True, patch_artist=True, labels=list(record.keys()))

    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Accuracy')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
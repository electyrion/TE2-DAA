import Greedy
import BranchAndBound
import DatasetGenerator

def main():
    # Generate a dataset
    # DatasetGenerator.main()
    
    # Read the dataset from the file
    [m, S, P] = DatasetGenerator.readFromFile('dataset/large.txt')
    
    # Run the greedy algorithm
    print('Greedy: ')
    Greedy.main(m, S, P)
    
    # Run the branch and bound algorithm
    print('Branch and Bound: ')
    BranchAndBound.main(m, S, P)

if __name__ == '__main__':
    main()
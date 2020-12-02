import graphio
import topk
from datetime import datetime
import os
import generator
from time_measure import time

def getNumChoice(msg='> '):
    while True:
        choice = input(msg)
        if not choice.isdigit():
            print("Enter a valid number!")
            continue
        else:
            return int(choice)

def printTimeTaken(timeTaken):
    print('Time taken to run: ', format(timeTaken, '.4f'), "seconds")

def loadGraphHospital():
    while True:
        print("List of Graph and Hospital Files: ")
        count = 0
        dir1 = os.listdir("./graph/")
        for x in dir1:
            count += 1
            print(str(count) + ": " + x)
            
        print()

        while True:
            choice = getNumChoice('Which graph file: ')

            if choice >= count + 1 or choice < 0:
                return None, None

            choiceH = getNumChoice('Which hospital file: ')

            if choiceH >= count + 1 or choiceH < 0:
                return None, None

            print("Loading the graph may take a few seconds...")
            node_dic, timeTaken = time(graphio.initialiseGraph, 'graph/'+ dir1[choice-1])
            printTimeTaken(timeTaken)
            print()
            hospital = graphio.initialiseHospital('graph/'+ dir1[choiceH-1], node_dic)
            print("Hospital file loaded")

            return node_dic, hospital


def search(node_dic, hospital, k):
    _, timeTaken = time(topk.BFS_from_Hospitals, hospital, node_dic, k)
    printTimeTaken(timeTaken)


def printMenu():
    print('1 - Load Graph and Hospital')
    print('2 - Generate Graph and Hospital')
    print('3 - Search for Nearest Hospitals')
    print('4 - Print Output')
    print('5 - Store Output')
    print('6 - Exit')

if __name__ == '__main__':
    print("Welcome to Hospital Locator")
    print(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    print('-----------------------')

    node_dic = None
    hospital = None

    while True:
        printMenu()

        while True:
            choice = getNumChoice()

            if choice <= 0 or choice >=  7:
                print('Error! Please enter a valid choice.')
                continue
    
            break
        
        if choice == 1:
            node_dic, hospital = loadGraphHospital()
            if node_dic == None:
                print('Graph and hospital not loaded.')
                print()

        elif choice == 2:
                name = input("Enter desired filename (# to abort): ")
                if name == '#':
                    continue
                num_of_node = getNumChoice('Enter number of nodes: ')
                degree = getNumChoice('Enter the average degree per node: ')
                numOfHospital = getNumChoice("Enter the number of hospital in graph: ")

                generator.generate(name, num_of_node, degree, numOfHospital)

        elif choice == 3:
            if node_dic == None or hospital == None:
                print("Load the graph and hospital files first!")
            else:
                choice = getNumChoice("How many nearest hospital: ")
                while choice <= 0:
                    print("Invalid! ")
                    choice = getNumChoice("How many nearest hospital: ")
                search(node_dic, hospital, choice)
                print("Done")

        elif choice == 4:
            choice = getNumChoice("All nodes (Enter 1) or Input node ID (Enter 2): ")
            if choice == 1:
                _, timeTaken = time(graphio.outputAllPath, node_dic)
                printTimeTaken(timeTaken)
            elif choice == 2:
                choice = getNumChoice("Enter node ID: ")
                _, timeTaken = time(graphio.outputPath, node_dic, choice)
                printTimeTaken(timeTaken)
            else:
                print("Invalid choice!")
        elif choice == 5:
            #name = input("Enter output file name: ")
            choice = input("Enter 1 if you want to store the shortest paths\n"+
                           "Enter 0 if you just need hospital IDs and distances")
            _, timeTaken = time(graphio.output_results, node_dic, "result.txt", int(choice))
            printTimeTaken(timeTaken)
        elif choice == 6:
            break

    print("See you again")
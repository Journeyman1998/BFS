all: main.exe

main.exe: loader.o main.o node.o
	g++ -o main.exe loader.o main.o node.o

loader.o: loader.cpp loader.hpp
	g++ -c loader.cpp

main.o: main.cpp loader.hpp
	g++ -c main.cpp

node.o:  node.cpp node.hpp
	g++ -c node.cpp
	
clean:
	del loader.o main.o main.exe node.o

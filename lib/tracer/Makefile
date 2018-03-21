


SRCS= tracer.cpp sceneloader.cpp
OBJS=$(SRCS:%.cpp=%.o)



all : trace

trace : $(OBJS) trace.cpp
	g++ -g $(OBJS) trace.cpp -o $@
	
%.o : %.cpp
	g++ -c -g $< -o $@
	
clean:
	rm -f trace.o trace
	
	
#all : trace
#
#trace : trace.o
#	g++ -g $< -o $@
#trace.o : trace.cpp
#	g++ -c -g $< -o $@
#
#	
#clean:
#	rm -f trace.o trace
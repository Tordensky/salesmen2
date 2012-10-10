CC = /opt/cilk/bin/g++

# Remove -DGRAPHICS to compile with no graphic support (e.g. for measurements)
CFLAGS = -O2 -Wall -DGRAPHICS

# Use this for SDL (change the path to sdl-config to the correct
# location if you're not running on rocks)
RRLIB = ../lib
INC = -I$(RRLIB) `sdl-config --cflags`
LIB = -L$(RRLIB) -L/usr/X11R6/lib64 -L/usr/X11R6/lib -lX11 -lgraphicsScreen -lStopWatch  `sdl-config --libs`

# and this for TinyPTC
#RRLIB  = ../lib-TinyPTC
#INC = -I$(RRLIB) 
#LIB = -L$(RRLIB) -L/usr/X11R6/lib64 -L/usr/X11R6/lib -lX11 -lgraphicsScreen -L../TinyPTC-X11-0.7.3 -ltinyptc -lStopWatch -lm

all: RaceTrap

RaceTrap: RaceTrap.c
	$(CC) $(CFLAGS) RaceTrap.c -o RaceTrap $(INC) $(LIB)

clean:
	rm -f *~ *.o core* RaceTrap


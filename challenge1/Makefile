#As minhas sources...
SRC=main.c

#O binário executável (nome do programa)
PROG=main

################################

CC=gcc
CFLAGS=-Wall

OBJ=$(SRC:.c=.o)  #macro automática para gerar os OBJ a partir das SRC

INCLUDE=    #para as header files (cabeçalhos)
LIB= -lm       #bibliotecas específicas a usar

############################################
# Regras
############################################

###########################################
# Regras relativas à compilação e linkagem

$(PROG): $(OBJ)
	$(CC) $(OBJ) -o $(PROG) $(LIB)

.c.o:
	$(CC) $(CFLAGS) -c $(INCLUDE) $< -o $@

#########################################
# Regras relativas à gestão e organização

clean:
	rm -rf $(PROG) $(OBJ)

allclean: clean
	rm -rf html latex

############################################

.PHONY: clean allclean 
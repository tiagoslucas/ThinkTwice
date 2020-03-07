#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
	int ordem = 5, valor = 5;
	FILE* input;
	FILE* output;
	input = fopen(argv[1], "r");
	if (fscanf(input, " %d %d", &ordem, &valor) != 2) {
		exit(EXIT_FAILURE);
	}
	fclose(input);

	output = fopen("result.txt", "w");
	fprintf(output, "%d", (int) pow((double)valor, 1 / (double)ordem));
	fclose(output);

	return 0;
}

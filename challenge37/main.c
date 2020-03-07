#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
	int n, result = 0;
	int vetori[10000] = { 0 };
	int vetorf[10000] = { 0 };
	FILE* input;
	FILE* output;
	input = fopen(argv[1], "r");
	if (fscanf(input, " %d", &n) != 1) {
		exit(EXIT_FAILURE);
	}
	for (int i = 0; i < (n * n * (n − 1) / 2); i++){
		fscanf(input, " %d", vetori[i]);
	}
	fclose(input);

	

	output = fopen("result.txt", "w");
	if (result == 0) {
		for (int i = 0; i < n; i++) {
			fprintf(output, "%d ", vetorf[i]);
		}
	} else {
		fprintf(output, "%s", "Incorrect Balance.");
	}
	fclose(output);

	return 0;
}

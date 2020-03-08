#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
	int n, lim, result = 0;
	int vetori[50] = { 0 };
	int vetorf[50] = { 0 };
	FILE* input;
	FILE* output;
	input = fopen(argv[1], "r");
	if (fscanf(input, " %d", &n) != 1) {
		exit(EXIT_FAILURE);
	}
	lim = n * n * (n - 1) / 2;
	for (int i = 0; i < lim; i++){
		fscanf(input, " %d", &vetori[i]);
	}
	fclose(input);

	for (int i = 0; i < lim; i++) {
		if (result == 0) {
			if (i < 1)
				vetorf[i] = 0;
			else
				vetorf[i] = vetorf[i-1] + vetori[i-1] - vetorf[i-1];
		}
		for (int j = 0; j < i; j++) {
			if (((vetorf[i] - vetorf[j]) + (vetorf[j] - vetorf[0])) != vetorf[i] - vetorf[0]) {
				result = 1;
				break;
			}
		}
	}
	
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

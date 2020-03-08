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

	for (int i = 0; i < n; i++) {
		for (int j = i - 1; j > 0; j--) {
			if ((( vetori[i] - vetori[j] ) + (vetori[j] - vetori[0])) != (vetori[i] - vetori[0]) ) {
				result = 2;
				break;
			}
		}
		if (result == 0) {
			if (i < 1)
				vetorf[i] = 0;
			else
				vetorf[i] = vetori[i] - vetorf[0];
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

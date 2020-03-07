#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
	double result;
	int k, m;
	FILE* input;
	FILE* output;

	input = fopen(argv[1], "r");
	if (fscanf(input, " %d %d", &k, &m) != 2) {
		exit(EXIT_FAILURE);
	}
	fclose(input);

	result = (k * 2);
	result = (m + k) / result;
	result = m * result;

	output = fopen("result.txt", "w");
	fprintf(output, "%d", (int) ceil(result));
	fclose(output);

	return 0;
}

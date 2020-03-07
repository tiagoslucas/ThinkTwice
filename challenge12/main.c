#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

int convert(int number,int base){
    if(number == 0 || base==10)
        return number;
    return (number % base) + 10*convert(number / base, base);
}

int main(int argc, char** argv) {
	int n, m, t, zeros, v;
	FILE* input;
	FILE* output;
	input = fopen(argv[1], "r");
	if (fscanf(input, " %d %d %d", &n, &m, &t) != 3) {
		exit(EXIT_FAILURE);
	}
	fclose(input);
	t = pow(10, t);
	n = (int) pow((double)n, (double)m);
	for (int i = 2; i <= n; i++) {
		v = convert(n, i);
		if ((v % t) == 0 && v != 0) {
			printf("%d\n", v);
			zeros++;
		}
	}

	output = fopen("result.txt", "w");
	fprintf(output, "%d", zeros);
	fclose(output);

	return 0;
}

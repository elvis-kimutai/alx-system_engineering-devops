#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - a function that runs to infinity
 * and returns nothing
 *
 * Return: 0 in the end
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - The entry point to a program that creates 5 zombie process
 *
 * Return: 0 on success
 */

int main(void)
{
	int good = 0;
	pid_t pid;

	while (good < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		good++;
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * infinite_while - creates an infinite loop
 *
 * Return: returns  an integer
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
 * main - This is the programs entry point
 *
 * Return: returns an integer
 */
int main(void)
{
	pid_t p;
	int i;

	for (i = 0; i < 5; i++)
	{
		p = fork();
		if (p == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();

	return (0);
}

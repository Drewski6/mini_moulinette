#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../libft/libft_working/libft.h"

// Careful of library path. Make sure you dont forget to set correct path to libft.h
//	a.out takes 2 arguments. 
//	First is 0 or 1 which indicates which function to use (original or 42)
//	Second is a string to pass to the function.

int main (int argc, char* argv[])
{
	char*	return_val = 0;
	int		i;
	char 	all_printable[200];
	int		len;

	i = 32;
	while(i < 128)
	{
		all_printable[i - 32] = i;
		i++;
	}
	// >=32 <= 127

	i = 0;
	len = 95;		//strlen(all_printable);
	while (i < len)
	{
		if (atoi(argv[1]) == 0)
		{
			return_val = strrchr(argv[2], all_printable[i]);
			printf("strrchr,%s,%c,%s\n", argv[2], all_printable[i], return_val);
		}
		else
		{
			return_val = ft_strrchr(argv[2], all_printable[i]);
			printf("strrchr,%s,%c,%s\n",argv[2], all_printable[i], return_val);
		}
		i++;
	}
	return (0);
}

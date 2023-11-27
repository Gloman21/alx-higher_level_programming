#include "lists.h"

/**
*check_cycle - checks if list contains a cycle
*@list: linked list to be checked
*Return: 1(Success) or 0(Failure)
*tst:test
*tmp:temp
*/
int check_cycle(listint_t *list)
{
	listint_t *tstlist = list;
	listint_t *tmplist = list;

	while (tstlist != NULL && tmplist != NULL && tmplist->next != NULL)
	{
		tstlist = tstlist->next;
		tmplist = tmplist->next->next;
		if (tstlist == tmplist)
			return (1);
	}
	return (0);
}

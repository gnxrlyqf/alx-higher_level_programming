#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks a linked list for a cycle
 * @list: head node of the linked list to check
 *
 * Return: 1 (has a cycle), 0 (doesn't)
*/

int check_cycle(listint_t *list)
{
	listint_t	*list_item;

	list_item = list;
	while (list_item->next)
	{
		if (list_item->next == list)
			return (1);
		list_item = list_item->next;
	}
	return (0);
}

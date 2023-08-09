#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *node;

	node = (listint_t *)malloc(sizeof(listint_t));
	node->n = number;
	if (!(*head) || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	current = *head;
	while (current)
	{
		if (current->next && current->next->n < number)
		{
			current = current->next;
			continue ;
		}
		node->next = current->next;
		current->next = node;
		return (node);
	}
	return (node);
}
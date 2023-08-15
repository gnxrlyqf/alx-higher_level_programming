#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to a pointer to the head node of the list
 *
 * Return: 1 if it's a palindrome, 0 if it isn't
*/

int is_palindrome(listint_t **head)
{
	int length = 1, half, top = 1, bottom, vtop, vbottom, *arr, i, j;
	listint_t *current = *head;

	if (!current)
		return (1);
	while (current->next)
	{
		current = current->next;
		length++;
	}
	half = length / 2;
	arr = malloc(half * sizeof(int));
	bottom = length;
	for (i = top; i <= half; i++)
	{
		current = *head;
		for (j = 1; j <= i; j++)
		{
			vtop = current->n;
			current = current->next;
		}
		current = *head;
		for (j = 1; j <= bottom; j++)
		{
			vbottom = current->n;
			current = current->next;
		}
		bottom--;
		if (vtop == vbottom)
			arr[i - 1] = 1;
		else
			arr[i - 1] = 0;
	}
	for (i = 0; i < half; i++)
		if (arr[i] != 1)
			return (0);
	return (1);
}

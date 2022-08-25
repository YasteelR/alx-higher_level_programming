#include "lists.h"
#include <stdlib.h>

/**
 * _realloc - Reallocates a memory block
 * @ptr: The pointer to the last node
 * @old_size: prev size 
 * @new_size: new size
 * Return: The pointer or 0
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	void *Nptr;
	unsigned int min_size = old_size < new_size ? old_size : new_size;
	unsigned int lvl;

	if (new_size == old_size)
		return (ptr);
	if (ptr != NULL)
	{
		if (new_size == 0)
		{
			free(ptr);
			return (NULL);
		}
		Nptr = malloc(new_size);
		if (Nptr != NULL)
		{
			for (lvl = 0; lvl < min_size; lvl++)
				*((char *)Nptr + lvl) = *((char *)ptr + lvl);
			free(ptr);
			return (Nptr);
		}
		free(ptr);
		return (NULL);
	}
	else
	{
		Nptr = malloc(new_size);
		return (Nptr);
	}
}

/**
 * check_cycle - checks if list has a cycle
 * @list: list head
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (list == NULL)
		return (0);

	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}

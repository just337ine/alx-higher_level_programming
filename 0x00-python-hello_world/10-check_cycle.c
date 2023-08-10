/**
 * check_cycle - a function that checks if a
 * singly linked list has a cycle in it.
 *
 * @list: struct array
 * Return: 0 if there is no cycle else 1.
 */
#include "list.h"
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0); /* No cycle if the list is empty or has only one element */
	}
	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1); /* Cycle detected */
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

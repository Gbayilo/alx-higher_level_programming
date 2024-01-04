#include "lists.h"

/**
 * check_cycle - checks if a cycle is contained in a singly-linked list
 * @list: the list to check
 *
 * Return: 0 if there is no cycle, else 1 when a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);
	slow = fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}

	return (0);
}

#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to the head node
 *
 * Return: 1 the list is a palindrom else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *other_half = NULL, *mid_node = NULL;
	listint_t *prev, *slow_ptr, *fast_ptr;
	int result = 1;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (result);

	slow_ptr = fast_ptr = *head;
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		prev = slow_ptr;
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
	{
		mid_node = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	other_half = slow_ptr;
	prev->next = NULL;

	reverse(&other_half);
	result = palindrome_help(*head, other_half);
	reverse(&other_half);

	if (mid_node != NULL)
	{
		prev->next = mid_node;
		mid_node->next = other_half;
	}
	else
		prev->next = other_half;

	return (result);
}

/**
 * reverse - reverses a linked list
 * @list: the list to reverse
 */
void reverse(listint_t **list)
{
	listint_t *next_node, *cur, *prev = NULL;

	if (*list == NULL || list == NULL)
		return;

	cur = *list;

	while (cur != NULL)
	{
		next_node = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next_node;
	}

	*list = prev;
}

/**
 * palindrome_help - a helper function to perform the palindrome check
 * @list_1: first hald of the linked list
 * @list_2: other half of the linked list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int palindrome_help(listint_t *list_1, listint_t *list_2)
{
	while (list_1 != NULL && list_2 != NULL)
	{
		if (list_1->n == list_2->n)
		{
			list_1 = list_1->next;
			list_2 = list_2->next;
		}
		else
		{
			return (0);
		}
	}

	if (list_1 == NULL && list_2 == NULL)
		return (1);

	return (0);
}

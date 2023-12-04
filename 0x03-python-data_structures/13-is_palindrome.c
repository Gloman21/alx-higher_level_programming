#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *reversed = NULL, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		add_nodeint(&reversed, slow->n);
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if (slow->n != reversed->n)

		{
			free_listint(&reversed);
			return (0);
		}
	}

	temp = reversed;
	reversed = reversed->next;
	free(temp);
	slow = slow->next;
	}

    free_listint(&reversed);
    return (1);
}

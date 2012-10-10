/* Author: Steffen Viken Valvaag <steffenv@cs.uit.no> */
#include <stdlib.h>

struct alistnode;

typedef struct alistnode alistnode_t;
struct alist;
typedef struct alist alist_t;
struct alist_iter;
typedef struct alist_iter alist_iter_t;

struct alistnode {
    alistnode_t *next;
    alistnode_t *prev;
    void *elem;
};

struct alist {
    alistnode_t *head;
    alistnode_t *tail;
    int size;
};

struct alist_iter {
    alistnode_t *node;
};

static alistnode_t *anewnode(void *elem)
{
    alistnode_t *node = (alistnode_t *) malloc(sizeof(alistnode_t));
    if (node == NULL)
	    exit(1);
    node->next = NULL;
    node->prev = NULL;
    node->elem = elem;
    return node;
}

alist_t *alist_create()
{
    alist_t *alist = (alist_t *)malloc(sizeof(alist_t));
    if (alist == NULL)
	    exit(1);
    alist->head = NULL;
    alist->tail = NULL;
    alist->size = 0;
    return alist;
}

void alist_destroy(alist_t *alist)
{
    alistnode_t *node = alist->head;
    while (node != NULL) {
	    alistnode_t *tmp = node;
	    node = node->next;
	    free(tmp);
    }
    free(alist);
}

int alist_size(alist_t *alist)
{
    return alist->size;
}

void alist_addfirst(alist_t *alist, void *elem)
{
    alistnode_t *node = newnode(elem);
    if (alist->head == NULL) {
	    alist->head = alist->tail = node;
    }
    else {
	    alist->head->prev = node;
	    node->next = alist->head;
	    alist->head = node;
    }
    alist->size++;
}

void alist_addlast(alist_t *alist, void *elem)
{
    alistnode_t *node = newnode(elem);
    if (alist->head == NULL) {
	    alist->head = alist->tail = node;
    }
    else {
	    alist->tail->next = node;
	    node->prev = alist->tail;
	    alist->tail = node;
    }
    alist->size++;
}

void *alist_popfirst(alist_t *alist)
{
    if (alist->head == NULL) {
	    exit(1);
    }
    else {
        void *elem = alist->head->elem;
	    alistnode_t *tmp = alist->head;
	    alist->head = alist->head->next;
	    if (alist->head == NULL) {
	        alist->tail = NULL;
	    }
	    else {
	        alist->head->prev = NULL;
	    }
	    alist->size--;
	    free(tmp);
	    return elem;
    }
}

void *alist_poplast(alist_t *alist)
{
    if (alist->tail == NULL) {
        exit(1);
    }
    else {
        void *elem = alist->tail->elem;
	    alistnode_t *tmp = alist->tail;
	    alist->tail = alist->tail->prev;
	    if (alist->tail == NULL) {
	        alist->head = NULL;
	    }
	    else {
	        alist->tail->next = NULL;
	    }
	    free(tmp);
	    alist->size--;
	    return elem;
    }
}


alist_iter_t *alist_createiter(alist_t *alist)
{
    alist_iter_t *iter = (alist_iter_t *) malloc(sizeof(alist_iter_t));
    if (iter == NULL)
	    exit(1);
    iter->node = alist->head;
    return iter;
}

void alist_destroyiter(alist_iter_t *iter)
{
    free(iter);
}

int alist_hasnext(alist_iter_t *iter)
{
    if (iter->node == NULL)
	    return 0;
    else
	    return 1;
}

void *alist_next(alist_iter_t *iter)
{
    if (iter->node == NULL) {
	    exit(1);
    }
    else {
	    void *elem = iter->node->elem;
	    iter->node = iter->node->next;
	    return elem;
    }
}


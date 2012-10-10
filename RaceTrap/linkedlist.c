/* Author: Steffen Viken Valvaag <steffenv@cs.uit.no> */
#include <stdlib.h>

struct listnode;

typedef struct listnode listnode_t;
struct list;
typedef struct list list_t;
struct list_iter;
typedef struct list_iter list_iter_t;

struct listnode {
    listnode_t *next;
    listnode_t *prev;
    void *elem;
};

struct list {
    listnode_t *head;
    listnode_t *tail;
    int size;
};

struct list_iter {
    listnode_t *node;
};

static listnode_t *newnode(void *elem)
{
    listnode_t *node = (listnode_t *) malloc(sizeof(listnode_t));
    if (node == NULL)
	    exit(1);
    node->next = NULL;
    node->prev = NULL;
    node->elem = elem;
    return node;
}

list_t *list_create()
{
    list_t *list = (list_t *)malloc(sizeof(list_t));
    if (list == NULL)
	    exit(1);
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
    return list;
}

void list_destroy(list_t *list)
{
    listnode_t *node = list->head;
    while (node != NULL) {
	    listnode_t *tmp = node;
	    node = node->next;
	    free(tmp);
    }
    free(list);
}

int list_size(list_t *list)
{
    return list->size;
}

void list_addfirst(list_t *list, void *elem)
{
    listnode_t *node = newnode(elem);
    if (list->head == NULL) {
	    list->head = list->tail = node;
    }
    else {
	    list->head->prev = node;
	    node->next = list->head;
	    list->head = node;
    }
    list->size++;
}

void list_addlast(list_t *list, void *elem)
{
    listnode_t *node = newnode(elem);
    if (list->head == NULL) {
	    list->head = list->tail = node;
    }
    else {
	    list->tail->next = node;
	    node->prev = list->tail;
	    list->tail = node;
    }
    list->size++;
}

void *list_popfirst(list_t *list)
{
    if (list->head == NULL) {
	    exit(1);
    }
    else {
        void *elem = list->head->elem;
	    listnode_t *tmp = list->head;
	    list->head = list->head->next;
	    if (list->head == NULL) {
	        list->tail = NULL;
	    }
	    else {
	        list->head->prev = NULL;
	    }
	    list->size--;
	    free(tmp);
	    return elem;
    }
}

void *list_poplast(list_t *list)
{
    if (list->tail == NULL) {
        exit(1);
    }
    else {
        void *elem = list->tail->elem;
	    listnode_t *tmp = list->tail;
	    list->tail = list->tail->prev;
	    if (list->tail == NULL) {
	        list->head = NULL;
	    }
	    else {
	        list->tail->next = NULL;
	    }
	    free(tmp);
	    list->size--;
	    return elem;
    }
}


list_iter_t *list_createiter(list_t *list)
{
    list_iter_t *iter = (list_iter_t *) malloc(sizeof(list_iter_t));
    if (iter == NULL)
	    exit(1);
    iter->node = list->head;
    return iter;
}

void list_destroyiter(list_iter_t *iter)
{
    free(iter);
}

int list_hasnext(list_iter_t *iter)
{
    if (iter->node == NULL)
	    return 0;
    else
	    return 1;
}

void *list_next(list_iter_t *iter)
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


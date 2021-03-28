// Implements a dictionary's functionality
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
int words=0;

// Hashes word to a number
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int temp=hash(word);
    node *cursor=table[temp];
    while(cursor!=NULL){
        if (strcasecmp(cursor->word, word) == 0) return true;
        cursor = cursor->next;
    }
    return 0;
}



// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    FILE *pointer1 = fopen(dictionary, "r");
    if(pointer1==NULL) return 0;
    char dicwords[LENGTH+1];
    while(fscanf(pointer1,"%s",dicwords)!=EOF){

        node *n = malloc(sizeof(node));
        if(n==NULL) return 0;

        strcpy(n->word,dicwords);

        int x=hash(dicwords);

        if(table[x]==NULL) {
            n->next=NULL;
            table[x]=n;}

        else {
            n->next = table[x];
            table[x]=n;
        }
        words++;
    }
    fclose(pointer1);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return words;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for(int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *temp = cursor;

        while(cursor != NULL)
        {
            cursor = cursor->next;
            free(temp);
            temp = cursor;
        }
    }
    return true;
}
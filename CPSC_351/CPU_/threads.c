#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "common_threads.h"

// shared between 2 pointers, volatile when var will be changing a lot
volatile int counter = 0;
int loops;

pthread_mutex_t lock;

void* worker(void* arg) { 
    int i;
    for (i = 0; i < loops; ++i) {
        /* ++counter means: grab, update, save/lock. EX: input == 100,000 result is indeterminate 
        add mutex to make it determinate */
        
        Pthread_mutex_lock(&lock);
        ++counter;
        Pthread_mutex_unlock(&lock); 
        }
    return NULL;
}

int main(int argc, const char* argv[]) { 
    if (argc != 2) {
        fprintf(stderr, "Usage: threads <value>\n");
        exit(1);
    }
    Pthread_mutex_init(&lock, NULL);

    // convert ascii to int
    loops = atoi(argv[1]);
    
    //_t means type; 2 threads running in parallel
    pthread_t p1, p2;
    printf("Initial value: %d\n", counter);

    // initialize p# , arg, call funct, pass arg
    Pthread_create(&p1, NULL, worker, NULL);
    Pthread_create(&p2, NULL, worker, NULL);

    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("Final value   : %d\n", counter);
    return 0;
}

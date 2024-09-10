#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, const char* argv[]) { 
    printf("hello (pid:%d)\n", (int)getpid());

    int rc = fork();
    if (rc < 0) { fprintf(stderr, "Fork failed\n"); exit(1); }
    else if (rc == 0) { // child {
        printf("\t\tCHILD: child (pid:%d)\n", (int)getpid());
    } else {
        printf("PARENT: parent of %d (pid:%d)\nParent is: (pid%d)\n", rc, (int)getpid(),
            (int)getppid());
    }
    return 0;
}

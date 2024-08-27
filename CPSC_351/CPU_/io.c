#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <fcntl.h>
#include <string.h>
#include <sys/types.h>

int main(int argc, const char* argv[]) { 
    int fd = open("hello.txt", 
                  O_WRONLY | O_CREAT | O_TRUNC,
                  S_IRWXU);
    assert(fd > -1);
    const char* msg = "Good morning sunshine, the earth says hello!";
    int rc = write(fd, msg, strlen(msg));
    assert(rc == strlen(msg));
    close(fd);

    return 0;
}

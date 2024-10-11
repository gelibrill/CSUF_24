#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/stat.h>

#define MAX_LINE 1024
#define MAX_ARGS 64

// History to store last command for !!
char last_command[MAX_LINE];

// Function to parse the input and identify spaces and pipes
void parse_input(char *input, char **args, int *is_pipe) {
    *is_pipe = 0;
    int i = 0;
    char *token = strtok(input, " ");
    
    while (token != NULL) {
        if (strcmp(token, "|") == 0) {
            *is_pipe = 1;
            args[i++] = NULL;
            printf("PIPE\n");
        }
        else {
            if (strcmp(token, " ") == 0) {
                printf("SPACE\n");
            }
            args[i++] = token;
        }
        token = strtok(NULL, " ");
    }
    args[i] = NULL;
}

// Function to handle built-in commands
int handle_builtin(char **args) {
    if (args[0] == NULL) {
        return 1;  // Empty command
    }
    
    if (strcmp(args[0], "exit") == 0) {
        exit(0);
    } else if (strcmp(args[0], "help") == 0) {
        printf("Help: Supported commands are cd, mkdir, help, exit, !!\n");
        return 1;
    } else if (strcmp(args[0], "cd") == 0) {
        if (args[1]) {
            if (chdir(args[1]) != 0) {
                perror("cd failed");
            }
        } else {
            printf("Usage: cd <directory>\n");
        }
        return 1;
    } else if (strcmp(args[0], "mkdir") == 0) {
        if (args[1]) {
            if (mkdir(args[1], 0755) != 0) {
                perror("mkdir failed");
            }
        } else {
            printf("Usage: mkdir <directory>\n");
        }
        return 1;
    } else if (strcmp(args[0], "!!") == 0) {
        if (strlen(last_command) == 0) {
            printf("No command in history.\n");
        } else {
            printf("Repeating last command: %s\n", last_command);
            strcpy(args[0], last_command);
            return 0;  // Execute last command
        }
        return 1;
    }

    return 0;  // Not a built-in command
}

// Execute a command with optional redirection or piping
void execute_command(char **args, int background, int is_pipe) {
    pid_t pid = fork();
    if (pid == 0) {
        // Child process
        if (is_pipe) {
            // Pipe handling
            int pipefd[2];
            if (pipe(pipefd) == -1) {
                perror("pipe");
                exit(EXIT_FAILURE);
            }
            
            pid_t pid2 = fork();
            if (pid2 == 0) {
                // First command: write to the pipe
                close(pipefd[0]);
                dup2(pipefd[1], STDOUT_FILENO);
                close(pipefd[1]);
                execvp(args[0], args);
                perror("execvp");
                exit(EXIT_FAILURE);
            } else {
                // Second command: read from the pipe
                close(pipefd[1]);
                dup2(pipefd[0], STDIN_FILENO);
                close(pipefd[0]);
                execvp(args[1], args + 1);  // Execute second command
                perror("execvp");
                exit(EXIT_FAILURE);
            }
        } else {
            // Handle redirection
            for (int i = 0; args[i] != NULL; i++) {
                if (strcmp(args[i], ">") == 0) {
                    int fd = open(args[i + 1], O_CREAT | O_WRONLY | O_TRUNC, 0644);
                    if (fd < 0) {
                        perror("open");
                        exit(EXIT_FAILURE);
                    }
                    dup2(fd, STDOUT_FILENO);
                    close(fd);
                    args[i] = NULL;
                    break;
                }
            }

            execvp(args[0], args);
            perror("execvp failed");
            exit(EXIT_FAILURE);
        }
    } else {
        // Parent process
        if (!background) {
            waitpid(pid, NULL, 0);
        }
    }
}

// Main function to handle shell loop
int main() {
    char input[MAX_LINE];
    char *args[MAX_ARGS];
    int is_pipe = 0;
    
    while (1) {
        printf("shell> ");
        fflush(stdout);
        
        if (fgets(input, MAX_LINE, stdin) == NULL) {
            break;  // Exit on EOF
        }
        
        // Remove trailing newline character
        input[strlen(input) - 1] = '\0';
        
        // Store the last command
        strcpy(last_command, input);
        
        parse_input(input, args, &is_pipe);
        
        // Check if ECHO is in the command
        int echo_found = 0;
        for (int i = 0; args[i] != NULL; i++) {
            if (strcmp(args[i], "ECHO") == 0) {
                echo_found = 1;
                break;
            }
        }

        if (echo_found) {
            for (int i = 0; args[i] != NULL; i++) {
                // Stop printing when "ECHO" found
                if (strcmp(args[i], "ECHO") != 0) {
                    if(strcmp(args[i], "echo") == 0){
                        i++;
                    }
                    printf("%s\n", args[i]);
                }
                else {
                    break;
                }
            }
        } else {
            if (!handle_builtin(args)) {
                execute_command(args, 0, is_pipe);
            }
        }
    }
    
    return 0;
}

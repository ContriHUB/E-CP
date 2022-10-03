# Commands

*   ```
    ecp problem <problem_link> <destination>
    ```
    Example: 
    ```
    ecp problem https://codeforces.com/contest/1739/problem/A .
    ```
    This will create a folder with the problem name, which will contain the code file, input files and expected output files which will contain sample test from the website.
    Only codeforces is supported as if now.

*   ```
    ecp config set-lang <language>
    ```
    Example: 
    ```
    ecp config set-lang python
    ```
    This will change the runtime environment. 
    Currently value of `<language>` can only be 'python' or 'cpp' are supported

*   ```
    ecp config set-proxy <username:password@ip:port>
    ```
    Example: 
    ```
    ecp config set-proxy <edcguest:edcguest@172.31.102.29:3128>
    ```
    This will change the proxy settings.

*   Change directory to the problem directory created by the first command, and then use:
    ```
    ecp run
    ```
    This will run the code file present in the folder and compare the expected and actual output.
    
    ```
    ecp run -c
    ```
    This will run the code file present in the folder and ask for custom inputs.

*   Change default template file link using:
    ```
    ecp config set-temp <dest>
    ```
    `<dest>` is the absolute template file path

*   Start a test session using:
    ```
    ecp test start <time>
    ```        
    `<time>` is the duration of the test in minutes. Default value: 30 mins
    This will start the test server. Change terminal as you further can't use the current terminal.
    You can only have one test session at any time.

*   Stop a test session using: 
    ```
    ecp test stop
    ```

*   Get remaining time duration in a test using: 
    ```
    ecp test time
    ```
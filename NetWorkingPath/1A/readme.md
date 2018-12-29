steps to execute:

```sh
netstat -tulnp
gcc server.c
./a.out 631
```
open another terminal
```sh
gcc client.c
./a.out 127.0.0.1
```

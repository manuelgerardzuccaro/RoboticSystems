# RoboticSystems



------

## *Index*

- **[Credits](#Credits)**
- **[Usage](#Usage)**
  - **[Linux](#Linux)**
  - **[WSL](#WSL)**
  - **[Docker](#Docker)**


------



## Credits

Software for the Robotic Systems Course @ UniCT by [Prof. Santoro Corrado](https://github.com/corradosantoro)



## Usage

### Linux

You can use the `init.sh` script to install all necessary package:

```bash
sudo chmod +x ./init.sh && ./init.sh
```

Then you can try some scripts inside **./tests**. 



### WSL

Download and install <a target="_blank" href="https://sourceforge.net/projects/vcxsrv/">VcXsrv</a>.

Now follow these steps:

<img src="img/01.png" style="zoom: 67%;">

<img src="img/02.png" style="zoom:67%;" >

<img src="img/03.png" style="zoom:67%;" >

<img src="img/04.png" style="zoom:67%;" >

Now use the following command:

```shell
$ cat /etc/resolv.conf
```

Take note of the nameserver.

<img src="img/05.png">

After that, you have to use these command:

```shell
$ cd ~
$ nano .bashrc
```

At the end insert:

```shell
$ export DISPLAY=<nameserver>:0.0
$ export LIBGL_ALWAYS_INDIRECT=1
```

Use `CTRL+O` and `RETURN` to save; `CTRL+X` and `RETURN` to exit.

Then use:

```shell
$ source .bashrc
```

Now, you can use the `init.sh` script to install all necessary package:

```bash
$ sudo chmod +x ./init.sh && ./init.sh
```

Then you can try some scripts inside **./tests**. 



### Docker

Download and install <a target="_blank" href="https://www.docker.com/products/docker-desktop">Docker Desktop</a> and <a target="_blank" href="https://sourceforge.net/projects/vcxsrv/">VcXsrv</a> (for [WSL](#WSL)).

Use the following commands:

```bash
$ docker-compose up -d
```

```bash
$ xhost local:root
```

```bash
$ sudo chmod +x docker_run.sh
```

Then you can try some scripts inside **./tests**:

```bash
$ ./docker_run.sh python3 tests/test_cart_plot.py
```


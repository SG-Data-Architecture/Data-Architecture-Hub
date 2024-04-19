<br>

A slice of [practice](https://github.com/thereferences/practice)

<br>

### Sphinx

Initialise a Sphinx Documentation `docs` directory via:

```bash
mkdir docs && cd docs && sphinx-quickstart
```

Build the <abbr title="HyperText Markup Language">HTML</abbr> pages via:

```bash
sphinx-build -E -b html docs/source doc/build/html
```

<br>
<br>

### Remote Development

For further development via a container, the `.devcontainer` directory has

* requirements.txt
* Dockerfile

The requirements file lists the packages/libraries required for development.  An image is built via the command:

```shell
docker build . --file .devcontainer/Dockerfile --tag transcribe
```

Subsequently, a development container is initialised via the command

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app transcribe
```

Whereby:

* [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) 
* [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) 
* [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) 
* [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 

<br>
<br>

### Local Development

Alternatively, a local virtual environment can be built via **environment.yml**; **environment.yml** uses the same 
**requirements.txt** as [Dockerfile](/.devcontainer/Dockerfile).

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

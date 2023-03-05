# App sobre Datos de Cáncer

## Objectivo
+ Crear una app sencilla con datos geográficos sobre incidencia y mortalidad de cáncer con algunas secciones sobre información con prevención y autodetección.

## Requisitos

+ Visual Studio Code
+ Github
+ Anaconda
## Ejecución

se debe tener instalado una versión de Python mayor a 3.7 y también tener instalando [Anaconda](https://www.anaconda.com/products/distribution). Para saber cual versión tienen, pueden ejecutar:

Github: [How to](https://git-scm.com/download/mac)

```
python --version
```

Luego deben crear un ambiente, para eso, el proyecto viene con un archivo `.yml` que contiene lo necesario para la ejecución correcta del proyecto. Para crear un ambiente, se ejecuta lo siguiente:

```
conda env create -f config.yml
```
Una vez que el ambiente se haya creado utilizamos 

```
conda activate cancerapp
```

para desactivarlo

```
conda deactivate cancerapp
```
Para actualizar el [ambiente](https://stackoverflow.com/questions/42352841/how-to-update-an-existing-conda-environment-with-a-yml-file)
```
conda activate myenv
conda env update --file local.yml --prune
```

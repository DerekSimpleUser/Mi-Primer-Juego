# Snaky

el clasico juego de *Snake* o la *Serpiente* en version CLI 

## Descripcion
el clasico juego de *Snake* hecho en python, el juego se juega desde la terminal detectando automaticamente las teclas presionadas sin detennerse la ejecucion del programa

## Funciones
* **Curses:** para una ventana cli interactiva.
* **Random:** para la aparicion aleatoria de manzanas.
* **Tkinter:** para la version gui del programa.

## Tecnologias
* **Lenguaje:** Python
* **OS:** Arch Linux y Void Linux
* **Editor:** Nano y Neovim

## Como ejecutar
### Movil:
si te gustaria utilizar el programa en un dispositivo movil (Android o Iphone) sigue los siguientes pasos:
- instala el programa **Termux** en **Android** o **ISH Shell** en **Iphone**
    * puedes instalar **Termux** haciendo click [aquí](https://f-droid.org/repo/com.termux_1022.apk) **NOTA:** ***NO DESCARGAR DESDE LA PLAY STORE***
    * puedes descargar **ISH Shell** desde la **App Store**
* ejecuta ``pkg update`` en **Termux** y ``apk update`` en **ISH Shell**
### descargar repositorio:
para descargar este repositorio deberás tener instalado git, puedes instalarlo asi:
* **Android:** ``pkg install git``
* **IOS:** ``apk add git``
* **MacOS:** ``xcode-select --install``
* **Windows:** abre terminal de administrador y ejecuta ``winget install --id Git.Git -e --silent``
* **Linux:** usa el gestor de paquetes de tu distribucion y descarga **git**
* *en el sistema en el que estés ejecuta estos comandos:*
``git clone https://github.com/DerekSimpleUser/snaky.git``
``cd snaky``
### instalar dependencias:
para instalar lo necesario ejecuta los siguientes comandos dependiendo tu sistema
* **Android/IOS/Linux/MacOS:** ``sh install.sh``
* **Windows:** abre una terminal de administrador y ejecuta: ``.\install.bat``
### ejecutar:
para ejecutar el programa solo ejecuta esto:
* **Android/IOS/Linux/Macos:** ``python3 serpiente_cli.py``
* **Windows:** ``python serpiente_cli.py``
### extra:
existe una version con interfaz grafica del programa solo ejecuta lo siguiente:
* **Android/IOS/Linux/MacOS:** ``python3 serpiente_gui.py``
* **Windows:** ``python serpiente_gui.py``

## Desarrollado por ***Patagonian Boy*** en conjunto de ***Binryan-void***

#!/bin/env bash

detectar_sudo() {
    if command -v sudo >/dev/null 2>&1; then
        SUDO="sudo"
    else
        SUDO=""
    fi
}

detect_base() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS_BASE="macos"
    elif [ -n "$TERMUX_VERSION" ]; then
        OS_BASE="termux"
    elif [ -f /etc/os-release ]; then
        . /etc/os-release
        OS_BASE=$(echo "${ID_LIKE:-$ID}"  | tr '[:upper:]' '[:lower:]')
    else
        echo "Error: no se pude detectar el sistema operativo."
        exit 1
    fi
}

install_packages() {
    PAQUETES="python3"
    case "$OS_BASE" in 
        *debian*)
            PAQUETES="python3 python3-tk"
            $SUDO apt update && $SUDO apt install -y $PAQUETES
            ;;
        *arch*)
            PAQUETES="python tk"
            $SUDO pacman -Sy --noconfirm $PAQUETES
            ;;
        *fedora*)
            PAQUETES="$PAQUETES python3-tkinter"
            $SUDO dnf check-update && $SUDO dnf install -y $PAQUETES && $SUDO dnf groupinstall "Development Tools"
            ;;
        *void*)
            PAQUETES="$PAQUETES python3-tkinter"
            $SUDO xbps-install -Sy $PAQUETES 
            ;;
        *alpine*)
            PAQUETES="python3 python3-tkinter"
            $SUDO apk update && $SUDO apk add $PAQUETES
            $SUDO apk add --no-cache ca-certificates
            ;;
        *termux*)
            PAQUETES="python"
	    pkg update && pkg install -y $PAQUETES
            ;;
        *macos*)
            echo "sistema MacOS detectado"
            echo "instalando paquetes..."
            xcode-select --install 2>/dev/null
            curl -O https://www.python.org/ftp/python/3.12.3/python-3.12.3-macos11.pkg
            sudo installer -pkg python-3.12.3-macos11.pkg -target / 
            "/Applications/Python 3.12/Install Certificates.command"
            ;;
        *)
            echo "Base '$OS_BASE' no soportada, favor de instalar manualmente '$PAQUETES'"
            exit 1
            ;;
    esac
}

detectar_sudo
detect_base
echo "ejecutar instalacion para sistemas base: $OS_BASE"
install_packages

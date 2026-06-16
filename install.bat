@echo off
echo Instalando Python...
winget install -e --id Python.Python.3.12 --scope machine--silent

:: Refrescar variables de entorno para esta sesión (truco para que reconozca python)
set "PATH=%PATH%;%LOCALAPPDATA%\Programs\Python\Python312\;%LOCALAPPDATA%\Programs\Python\Python312\Scripts\"

if %errorlevel% equ 0 (
    echo Python instalado correctamente.
) else (
	echo [!] Hubo un error al instalar python o ya estaba instalado.
)

echo Finalizada instalacion, ya puedes usar el programa COFB.
pause


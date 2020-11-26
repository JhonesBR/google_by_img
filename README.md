# Google by Image
All rights reserved to João Vitor Oliveira de Melo ([JhonesBR][myGit] on github)

## English
The goal of this project is to be enable to search for texts at google that are contained in images, usually because the page don't let you copy/paste the text or it can be contained at images or scanned PDF's.

>This software was made to educational purpose,
>it isn't made to search for test answers without permission,
>any use of this type is discriminable.

### Installation
In order to use this program you are going to need to install pytesseract (more instructions can be found at their [github repository][pytesseract]).

Inside the .py file there are some variables that can be ajusted for personal use, including the language of scanning (set by default to Portuguese). Rebember to include then at the tesseract instalation if you are using any language different than english).

You are going to need to install some external libraries that can be easily found with pip (using pip install <name> or python -m pip install <name>).
The program has some error policies that can be used, but it is recomended to install the libraries manualy before using the software.

| Library | Command to install |
| ------ | ------ |
| PIL | pip install pillow |
| PyAutoGUI | pip install pyautogui |
| Numpy | pip install numpy |
| Pynput Keyboard | pip install pynput |
| cv2 | pip install install opencv-python |

### Usage
While running the program, **Shift+A** set the **top left boundary**, as **Shift+B** set the **right botton** one, **Shift+C** **scan for text and search it or print it**(depending at the option configured, default to search)
| Bind | Function |
| ------ | ------ |
| Shift+A | Set top left boundary |
| Shift+B | Set botton right boundary |
| Shift+C | Execute |

## Português
O objetivo desse projeto é de possibilitar a pesquisa de textos no google que estão contidos em imagens, normalmente porque a página não permite copiar/colar ou porque está contida em imagens ou PDF's escaneados.

> Esse software foi feito para uso educacional,
> não foi feito para procurar resposta de questões sem permissão,
> qualquer uso desse tipo é discriminável.

### Instalação
Para usar esse programa você irá precisar instalar o pytesseract (mais instruções podem ser encontradas no [repositório git][pytesseract] deles).

Dentro do arquivo .py existem algumas variáveis que podem ser ajustadas para uso pessoal, incluindo a linguagem de scan (padrão em Português). Lembre-se de inclui-las na instalação do tesseract se você estiver usando outra língua diferente do inglês.

Você vai precisar instalar algumas bibliotecas externas que podem ser facilmente encontradas com o pip (usando pip install <nome> ou python -m pip install <nome>).
O programa possui algumas políticas de erro que podem ser usadas, mas é recomendado que seja feita a instalação dessas bibliotecas manualmente antes de utilizar o software.

| Biblioteca | Comando para instalar |
| ------ | ------ |
| PIL | pip install pillow |
| PyAutoGUI | pip install pyautogui |
| Numpy | pip install numpy |
| Pynput Keyboard | pip install pynput |
| cv2 | pip install install opencv-python |

### Uso
Enquanto rodando o programa, **Shift+A** define o limite **superior esquerdo**, enquanto **Shift+B** define o **direito inferior**, **Shift+C scaneia por texto e procura no google ou printa** (dependendo da opção configurada, padrão em pesquisa)

| Atalho | Função |
| ------ | ------ |
| Shift+A | Define o limite superior esquerdo |
| Shift+B | Define o limite inferior direito |
| Shift+C | Executa |



   [pytesseract]: <https://github.com/UB-Mannheim/tesseract/wiki>
   [myGit]: <https://github.com/JhonesBR>
# -*- coding: utf-8 -*-
"""dl_tuto_1_0_bienvenue_jupyter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/boscherj/a99985340011fef97b31e538ad6a59c7/dl_tuto_1_0_notebook_tutorial.ipynb

# Bienvenue à Jupyter Notebooks!

[Jupyter Notebook](https://jupyter.org) est une application Web qui permet de créer et partager des documents qui contiennent du code. 

Ce code peut être exécuté de façon interactive. 
Toutes les leçons présentées sur notre site, lorsqu'il s'agit de code, doivent être lues dans des notebooks. 

Vous avez plusieurs options pour lire les cours, c'est à dire les notebooks :
- soit directement sur le site [deep-learning.website](https://www.deep-learning.website) car il y a un embed des gist 
- soit avec Google Colaboratory 
- soit avec le nbviewer de Jupyter

Le plus simple est avec Google Colaboratory.

Ce cours, reprend la lesson 0_notebook_tutorial.ipynb de  [fastai](https://course.fast.ai/videos/?lesson=1), @[jeremyphoward](https://twitter.com/jeremyphoward)

## Section 1: le b.a.-ba

### Introduction

La documentation de Jupyter Notebook est [ici](https://jupyter-notebook.readthedocs.io/en/stable/). L'essentiel à savoir est qu'il existe des cellules de différents types (code, texte, en-tête de section). Les 2 derniers types étant similaires.

Pour exécuter une cellule de code, il faut faire Shift+Enter. 
Si vous êtes perdu(e), il y a la Palette de Commandes dans Outils, ou l'Aide.

Par exemple :
"""

1+1

"""Si la documentation ne vous suffit pas, il y a des livres sur Jupyter.

Par exemple : 
- Beginning Data Science with Python and Jupyter de Alex Galea (2018)
- Jupyter Cookbook de Dan Toomey (2018)

Mais il n'est pas sûr qu'il soit très utile de lire un livre pour apprendre Jupyter car c'est quand même très facile...

### Ecrire

Depuis la création du tuto  0_notebook_tutorial de fastai, les menus Jupyter ont été légèrement modifiés. Il est toujours possible de code avec le [Markdown](https://daringfireball.net/projects/markdown/) mais l'intérêt est limité.

Notez que vous pouvez mettre du Html dans vos cellules de type Text mais qu'il n'est pas garanti que pour du code un peu complexe, celui-ci soit repris dans vos Gists GitHub.

### Autres Considerations Importantes

Le noteboook est sauvé toutes les120 seconds par défaut. 

Pour enregistrer (si vous utilisez Colab) vous pouvez le faire dans votre Drive, dans un Gist ou sous Github.

## Section 2: Pour aller plus loin

Inutile de vous casser la tête à apprendre les tags qui permettent de mettre en italiques, gras, ... puisque vous pouvez désormais le faire avec les commandes du menu

### Cellules de type Code

Un exemple de code qui affiche une image 
Notez qu'il n'est pas nécessaire d'importer fastai pour afficher une image, il existe de nombreuses librairies qui le font
"""

# On importe les librairies Python
# Evidemment elles doivent avoir été installées au préalable
# C'est le cas dans Colab pour fastai
from fastai.vision import * 
import matplotlib.pyplot as plt

"""[Matplotlib](https://matplotlib.org) is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

[Pillow](https://he-arc.github.io/livre-python/pillow/index.html) est une bibliothèque de traitement d’image, qui est un fork et successeur du projet PIL (Python Imaging Library). Elle est conçue de manière à offrir un accès rapide aux données contenues dans une image, et offre un support pour différents formats de fichiers tels que PPM, PNG, JPEG, GIF, TIFF et BMP.
"""

from PIL import Image

a = 1
b = a + 1
c = b + a + 1
d = c + b + a + 1
a, b, c ,d

"""plt est très fréquemment utilisée en DL lorsqu'il s'agit d'afficher des graphiques
autre librairie qu'on lui associe : [seaborn](https://seaborn.pydata.org)
"""

plt.plot([a,b,c,d])
plt.show()

!ls ../usr

"""On peut aussi afficher des images. 

Auparavant, vous l'importez dans Colab de cette façon :
"""

from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

Image.open("GoogleNet-like-architecture.png")

"""### En local

On peut exécuter les Jupyter Notebooks sur sa propore machine mais ce n'est pas recommandé, sauf pour les logiciels qui ne nécessitent pas trop de calculs.

Dans le cas où c'est ce que vous souhaitez, installez Anaconda

#### Quelques trucs utiles à savoir
"""

from fastai import*
from fastai.vision import *

"""`?function-name`: pour voir la définition d'une fonction"""

?ImageDataBunch

"""`??function-name`: Shows the source code for that function"""

??ImageDataBunch

"""`doc(function-name)`: Shows the definition, docstring **and links to the documentation** of the function
(only works with fastai library imported)
"""

doc(ImageDataBunch)

"""#### Line Magics

iPython a quelques commandes "[magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html)" qu'on utilise presque systématiquement dans les Notebooks.

`%matplotlib inline`: To enable the inline backend for usage with the IPython Notebook:

`%reload_ext autoreload`, `%autoreload 2`: Reload all modules before executing a new line. If a module is edited, it is not necessary to rerun the import commands, the modules will be reloaded automatically.

Ces commandes commencent les Notebooks
"""

# %matplotlib inline
# %reload_ext autoreload
# %autoreload 2

"""`%timeit`: 

Time execution of a Python statement or expression
Par défaut, la commande est répétée 7 fois mais on peut lui demander de répéter 1000 fois si on veut
"""

# %timeit [i+1 for i in range(1000)]

"""`%debug`: Activate the interactive [debugger](https://ipython.readthedocs.io/en/stable/interactive/magics.html)"""

for i in range(1000):
    a = i+1
    b = 'string'
    c = b+1

# %debug


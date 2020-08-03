# **Elevator Software**
---

- ### **Sujet**
    Votre client vous propose de développer un software pour faire fonctionner des ascenseurs.<br/>
    Les différents hardwares qui équiperont ces ascenseurs possèdent 2 commandes : goUp() et goDown().<br/>
    Ecrire dans le langage serveur de votre choix le software permettant de faire fonctionner les ascenseurs équipés de ces hardwares.<br/>

- ### **Usage**
    python3 main.py config.json

- ### **Configuration**
    Il est possible de modifier différentes variables dans le fichier de configuration <br/>
    Ces variables sont :<br/>
    - La position initiale de l'ascenseur ("start Floor")<br/>
    - La hauteur maximale ou l'ascenseur peut se rendre("max Floor")<br/>
    - La profondeur maximale ou l'ascenseur peut se rendre("min Floor")<br/>
    Il serait facile de rajouter d'autres fonctionnalités telles que le poids maximal, la gestion des portes etc. <br/>


- ### **Exemple**

    - up 5 (l'ascenseur montera alors de 5 étages si il le peut)
    - down 8 (l'ascenseur descendera alors de 8 étages si il le peut)
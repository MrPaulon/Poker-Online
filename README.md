# 🃏 Poker Online

Un jeu de **Poker multijoueur en ligne**, entièrement développé en **Python** avec **Pygame**. Rejoins une table, bluffe tes amis, et remporte la mise !

![Poker Banner](img/back.jpg)

---

## 🎯 Fonctionnalités

- ♠️ Jeu multijoueur en réseau via sockets TCP
- ♥️ Interface graphique interactive avec **Pygame**
- ♦️ Implémentation des règles du **Texas Hold'em**
- ♣️ Serveur centralisé avec gestion des connexions
- 🔄 Prise en charge de plusieurs clients simultanés

---

## 🧰 Technologies utilisées

- Python 3.x
- Pygame
- Socket (TCP)
- Threading (multithreading)

---

## ⚙️ Installation et utilisation

### 1. Cloner le projet

```bash
git clone https://github.com/MrPaulon/Poker-Online.git
cd Poker-Online
```

### 2. Installer les dépendances

```bash
pip install pygame
```

### 3. Utilisation

Lancer un serveur
```
python server.py
```
Puis pour chaque client:
```bash
python client.py
python game.py
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues !
Voici comment proposer des modifications :
	1.	Fork ce dépôt
	2.	Crée une branche : git checkout -b feature/ma-fonction
	3.	Commit tes modifications : git commit -m "Ajout d'une nouvelle fonctionnalité"
	4.	Push la branche : git push origin feature/ma-fonction
	5.	Crée une Pull Request

---

 ## 📄 Licence

Ce projet est sous licence MIT, ce qui signifie que tu peux l’utiliser, le modifier et le redistribuer librement.
Voir le fichier LICENSE pour plus d’informations.

---


## 🙋 FAQ

Puis-je jouer avec des amis à distance ?
Oui, si le serveur est accessible via Internet ou sur un réseau local.

Puis-je personnaliser ou modifier le jeu ?
Absolument ! Le code est open source et modifiable librement.

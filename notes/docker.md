# Notes Docker

## Commandes utiles

| Commande | Rôle |
|---|---|
| `docker pull <image>` | télécharger une image depuis un registre |
| `docker images` | lister les images locales |
| `docker run --rm <image> <cmd>` | lancer un conteneur, le supprimer quand il s'arrête |
| `docker run -it --name <n> <image> sh` | shell interactif dans un conteneur nommé |
| `docker ps -a` | lister tous les conteneurs, y compris arrêtés |
| `docker rm <name>` | supprimer un conteneur arrêté |

## Concepts

### Général

- **Image** : modèle en lecture seule (comme un programme).
- **Conteneur** : instance d'une image qui tourne (comme un processus). Plusieurs conteneurs peuvent venir d'une même image.
- **Registre** : serveur qui stocke et distribue des images (Docker Hub est le registre public par défaut ; aussi GHCR, AWS ECR).
- Les données d'un conteneur vivent dans une couche modifiable : elles survivent à l'arrêt (`exit`) et sont supprimées par `docker rm`.

### Dockerfile

- `FROM` : l'image de base sur laquelle on construit (ici `python:3.12-slim`).
- `WORKDIR` : le dossier de travail dans l'image. Il est créé s'il n'existe pas, et les instructions suivantes s'y exécutent.
- `COPY` : copie des fichiers de ma machine vers l'image.
- `RUN` : exécute une commande pendant la construction de l'image (ex. `pip install`). Le résultat est enregistré dans une couche.
- `CMD` : commande par défaut au démarrage du conteneur. Elle ne s'exécute pas pendant la construction, et on peut la remplacer au lancement.

> [!NOTE]
> **Règle de cache :** Quand une étape change, Docker refait
> cette étape et toutes celles qui la suivent. On place donc
> en haut ce qui change rarement (les dépendances) et en bas
> ce qui change souvent (le code).
>
> Mesure : 17,6 s avec `COPY` de tout d'un coup avant `pip install`, 6,2 s avec `requirements.txt` copié avant `pip install` et `main.py` après.

Commandes : [docker-demo](../labs/docker-demo)

```sh
docker build -t demo:1 .
docker run --rm demo:1
docker run --rm -e NAME=Karim demo:1
docker run --rm demo:1 pwd
```

- `-t demo:1` : donne le nom `demo` et le tag `1` à l'image.
- `.` : le contexte de build, c'est-à-dire le dossier envoyé à Docker pour construire l'image.
- `-e NAME=Karim` : passe la variable d'environnement `NAME` au conteneur.
- `pwd` : remplace la `CMD` du Dockerfile, donc `main.py` ne se lance pas ; le conteneur affiche `/app` (le `WORKDIR`) puis s'arrête.

## Problèmes rencontrés

### `pip install` échoue pendant le build

- **Erreur :** `Temporary failure in name resolution` à l'étape `RUN pip install`.
- **Cause :** le second DNS de la VM est une adresse IPv6. Les conteneurs n'ont pas d'IPv6 par défaut, donc ils ne peuvent pas l'atteindre. La VM, elle, résolvait bien les noms.
- **Test :** `docker run --rm alpine nslookup pypi.org` expirait, alors que `ping 8.8.8.8` depuis le conteneur marchait (réseau OK, DNS cassé).
- **Correction :** dans `/etc/docker/daemon.json` :
  ```json
  { "dns": ["1.1.1.1", "8.8.8.8"] }
  ```
  puis `sudo systemctl restart docker`. Ce fichier configure la VM, il ne va pas dans le dépôt.

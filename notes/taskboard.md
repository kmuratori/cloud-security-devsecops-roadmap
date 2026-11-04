# Taskboard : conteneurisation

- **Tailles** : 133 Mo (classique) contre 124 Mo
  (multi-stage). Gain minimum : la base `python:3.12-slim`
  pèse presque tout.

- **`host="0.0.0.0"`** : sinon Flask n'écoute que dans le
  conteneur et `-p` ne marche pas.

- **`debug=False`** : le mode debug permet d'exécuter du
  code depuis le réseau.

- **`/data` donné à `user0`** : `user0` n'est pas root, il
  doit posséder `/data` pour créer `tasks.db`.

- **uid fixe 4200** : évite de tomber sur un compte de
  l'hôte (999 = `vboxadd`).

- **Volume** : `tasks.db` survit à `docker rm -f tb`.

- **Trivy** : 45 HIGH, 0 CRITICAL, tous dans la base Debian,
  aucun avec correctif. Mise à jour avec `docker build
  --pull`.

```sh
docker build -t tb:multi .
docker run -d --name tb -v data1:/data -p 5000:5000 tb:multi
docker save tb:multi -o multi.tar
docker run --rm               \
  -v "$PWD":/work             \
  -v trivy-cache:/root/.cache \
  aquasec/trivy:latest image  \
  --input /work/multi.tar     \
  --severity HIGH,CRITICAL    \
  --no-progress
```
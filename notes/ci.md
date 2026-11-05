# Intégration Continue (CI)

## Jobs
- `tests` : installe Python et les dépendances, lance `pytest`.
- `docker-build` : build l'image, puis lance le smoke test.
- `needs: tests` : `docker-build` attend `tests`.
- Sans `needs`, les deux jobs tournent en même temps.
- Chaque job a son runner : il refait son `checkout`.

## Dépendance des jobs
- Si `job1` dépend de `job0`, il est omis si `job0` échoue.

## Tests
- Un test doit pouvoir échouer, sinon il ne prouve rien.

## `git revert`
- Ajoute un commit qui annule l'ancien.
- On ne réécrit pas l'historique déjà poussé.
- `reset` réécrit l'historique : il force un `push --force`.
- Avec `revert`, l'historique reste complet.
- On peut même annuler un revert si nécessaire.

## `--exclude`
- La version de l'interpréteur du Dockerfile change selon l'outil.
- `# syntax=` impose la même version partout.
- Fix : `# syntax=docker/dockerfile:1.19` en première ligne.

## Environnement neuf
- Ma machine garde un historique : outils mis à jour, fichiers
  non commités, caches.
- Le runner repart de zéro à chaque run.
- Il n'a que ce qui est dans Git et son image de base.
- Le CI révèle donc le "ça marche chez moi".

## Smoke test
- Le build prouve que l'image se construit.
- Le smoke test prouve qu'elle démarre et répond.
- Boucle de 5 essais : l'app n'est pas prête tout de suite.
- `curl -f` : une erreur HTTP fait échouer le script.
- `trap` : le conteneur est supprimé même en cas d'échec.
- Un script doit aussi être vu échouer (port faux, code `1`).

## Limites
- Attente de 5 s max : un runner lent pourrait échouer à tort.
- Une seule route testée, en lecture.

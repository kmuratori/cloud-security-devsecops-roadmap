# GitHub Actions

## premier workflow
- Un workflow est un fichier YAML dans `.github/workflows/`.
- `checkout` est une **action** prédéfinie
  (`actions/checkout@v4`). Elle est appelée dans un **step**
  et clone le dépôt dans le runner.
- Sans `checkout`, le dossier de travail du runner est vide.

## déclencheurs et permissions
- On choisit les événements qui lancent le workflow (`push`,
  `pull_request`, `workflow_dispatch`, ...).
- `push` et `pull_request` sont des événements différents,
  chacun a ses propres filtres.
- Dans `push`, `branches` désigne la branche poussée. Dans
  `pull_request`, elle désigne la branche **cible** de la
  PR.
- `workflow_dispatch` permet de lancer le workflow à la
  main.
- Permissions minimales (`contents: read`) : chaque job ne
  reçoit que les droits dont il a besoin.
- Limiter les permissions réduit les dégâts d'une **Pwn
  Request**. Si un attaquant prend le contrôle du workflow,
  il peut compromettre la production, car le CI/CD a souvent
  des accès critiques (clés cloud, registres, jetons).
- **Job vs step** :
  - un job s'exécute sur son propre runner, les jobs sont
    indépendants (et peuvent tourner en parallèle) ;
  - un job contient des steps, qui s'exécutent à la suite
    sur le même runner et partagent le même dossier de travail.

## variables, secrets, artefacts
- **Variable** : valeur non sensible, visible dans les logs
  (`env:`).
- **Secret** : valeur sensible, chiffrée dans les réglages
  GitHub, masquée dans les logs, jamais écrite dans le YAML
  (sinon elle reste dans l'historique Git).
- **Artefact** : fichier produit par un job et gardé après
  le run. C'est le moyen de passer un fichier d'un job à un
  autre, car rien n'est partagé par défaut.
- On n'affiche jamais un secret (`echo`) : le masquage ne
  cherche que la valeur exacte, donc un secret transformé
  (base64, coupé en morceaux) apparaît en clair dans les
  logs.

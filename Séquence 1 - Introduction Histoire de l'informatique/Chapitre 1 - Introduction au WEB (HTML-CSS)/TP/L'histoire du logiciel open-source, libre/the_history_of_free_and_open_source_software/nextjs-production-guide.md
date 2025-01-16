# Guide de déploiement local pour Next.js

Ce guide explique comment construire et servir localement votre site Next.js en mode production.

## Prérequis

- Node.js installé sur votre machine
- Votre projet Next.js

## Étapes

### 1. Construction du site

Pour créer une version de production optimisée de votre site :

```bash
npm run build
```

Cette commande va compiler votre application et créer les fichiers de production dans le dossier `.next`.

### 2. Lancement du serveur de production

Après la construction, pour servir votre site en mode production :

```bash
npm run start
```

Cette commande démarre un serveur Node.js qui sert votre application en mode production.

### 3. Visualisation du site

Ouvrez votre navigateur et allez à :

```
http://localhost:3000
```

Vous devriez maintenant voir votre site fonctionner en mode production.

## Notes supplémentaires

### Exportation statique (optionnel)

Si votre site est entièrement statique, vous pouvez générer des fichiers HTML statiques :

1. Ajoutez cette ligne dans la section "scripts" de votre `package.json` :

```json
"scripts": {
  "export": "next build && next export"
}
```

2. Exécutez la commande :

```bash
npm run export
```

Cela créera un dossier `out` contenant une version statique de votre site.

### Différences avec le mode développement

- Le mode production (`npm run start`) n'inclut pas le rechargement à chaud et d'autres fonctionnalités de développement.
- Les performances sont optimisées pour la production.

### Déploiement

- Pour un déploiement sur des plateformes comme Vercel, vous pouvez simplement pousser votre code sur GitHub.
- Pour d'autres hébergeurs, vous devrez généralement transférer le contenu du dossier `.next`, ainsi que les fichiers `package.json` et `next.config.js`.

## Dépannage

Si vous rencontrez des problèmes :

1. Assurez-vous que toutes les dépendances sont installées (`npm install`).
2. Vérifiez les logs de construction et de démarrage pour d'éventuelles erreurs.
3. Assurez-vous que le port 3000 n'est pas déjà utilisé par une autre application.


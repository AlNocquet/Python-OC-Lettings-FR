# Mise en ligne sur Read the Docs

## 1. Build local

Windows PowerShell :

```powershell
pip install -r docs/requirements.txt
cd docs
.\make.bat html
```

macOS / Linux :

```bash
pip install -r docs/requirements.txt
cd docs
make html
```

Vérifier `docs/build/html/index.html`.

## 2. Import du dépôt

1. Se connecter à Read the Docs avec GitHub.
2. Choisir **Import a Project** / **Importer un dépôt**.
3. Sélectionner `AlNocquet/Python-OC-Lettings-FR`.
4. Finaliser l'import.

Le dépôt contient `.readthedocs.yaml`, qui pointe vers `docs/source/conf.py`.

## 3. Premier build

Lancer ou attendre le premier build et vérifier qu'il réussit.

## 4. Vérifier l'autobuild

1. Noter l'URL publique.
2. Faire une petite modification documentaire.
3. Commit + push.
4. Vérifier qu'un nouveau build démarre automatiquement.
5. Vérifier que la modification apparaît sur le site public.

## 5. README

Remplacer le placeholder Read the Docs dans `README.md` par l'URL publique définitive.

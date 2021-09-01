# GitHub Tips'n'Tricks

Her dokumenterer jeg github ting :smile:

# Dagligdagse kommandoer

Hente eksisterende repository: 

- `git clone <url-kopiet-fra-github>`

Synkronisere med origin (det som er på github.com)
- `git pull`

Når jeg har gjort endringer
- `git add <sti-til-endrede-filer>` (<.> for alle filer)
- `git commit -m "Her er en kommentar"`
- `git commit` hvor det er masse beskrivelsestekst
- `git push`

Se på git historie
- `git log --oneline`

Se på forskjeller
- `git diff`
- `git diff --staged` alt som er addet, men ikke commitet
- `git diff <ref> <ref>` der ref er enten branch eller commit id (alså den gule koden på starten av linjene når man skriver git log --oneline)
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
- `git commit --amend` fikse på gammel commit
- `git push`

Se på git historie
- `git log --oneline`

Se på forskjeller
- `git diff`
- `git diff --staged` alt som er addet, men ikke commitet
- `git diff <ref> <ref>` der ref er enten branch eller commit id (alså den gule koden på starten av linjene når man skriver git log --oneline)
- `git diff enbranch` sammenligner den du står i med enmaster. Det som er der du står men ikke i enbranch er grønt. Motsatt blir rødt. Alt som er felles er hvitt. 
- `git diff origin/master` sammenligner der du står opp mot det som er lagret på master på nett

# Branch

Lag ut ny branch
- `git checkout -b mybranch`

Sjekk hvilken branch vi er på
- `git branch`

Gå til eksisterende branch
- `git checkout mybranch`


# Se på gamle versjoner
Se på en gammel versjon
- `git checkout commitid` Dette er bare for å se på hvordan en gammel versjon ser ut - ikke gjør noen endringer her, det blir bare rot.

Hopp tilbake til den versjonen du jobbet i
- `git checkout denbranchendujobbeti`

# Reset
Gå tilbake til en tidligere versjon slik at denne gamle versjonen blir den gjeldene nyeste versjonen. Man sletter alt som har skjedd etter den gamle versjonen man tilbakestiller til. 
- `git reset commitid` 

# Merge
Hent endringer fra branch inn i en annen branch, f.eks. master. Man må stå i den branchen man vil hente endringer inn i. 
- `git merge mybranch`


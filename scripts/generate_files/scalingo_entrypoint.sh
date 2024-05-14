# Branch to checkout
BRANCH=test-auto

echo "> git clone barometre-resultats.git"
git clone --quiet https://github.com/DITP-pilotage/barometre-resultats.git barometre-resultats -b $BRANCH --depth 1
cd barometre-resultats/scripts/generate_files
python3 main.py

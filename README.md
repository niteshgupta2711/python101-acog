# python101
```
pyenv install --list
```
The above command lets you have all the list that lets a individual create environments

```
pyenv virtualenv 3.8.0 my-data-project
```
creating environments with pyenv

```
activate the env with 

```
pyenv shell my-data-project
```
```
initialize pyenv with pyenv init
```
```
# Load pyenv automatically by appending
# the following to 
~/.zprofile (for login shells)
and ~/.zshrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Restart your shell for the changes to take effect.
```
```
python3 -m pip install --user --upgrade pip

python3 -m pip --version

```
Using python3 for virtual environments
```
python3 -m venv env
```
```
source env/bin/activate
```
```
which python
```
The above command is used to check the which python interpreter are we using





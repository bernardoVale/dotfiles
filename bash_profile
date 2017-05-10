
# Load Variables
source ~/.variables
# Load Custom Alias
source ~/.aliases
# Mac OSX
source ~/.macos
# import docker alias
. ~/wsi_workstation_config.sh

if command -v brew >/dev/null && [ -f `brew --prefix`/etc/autojump.sh ]; then
  . `brew --prefix`/etc/autojump.sh
fi


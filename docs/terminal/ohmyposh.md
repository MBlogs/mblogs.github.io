https://ohmyposh.dev/docs/installation/macos
`brew install oh-my-posh`

# .zshrc
`which oh-my-posh`
The file path needs to be export in .zshrc
`export PATH=$PATH:/opt/homebrew/bin`

# Plugins

`git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

Then in ~/.zshrc
```
export ZSH="$HOME/.oh-my-zsh"
plugins=( 
    # other plugins...
    zsh-autosuggestions
)
source $ZSH/oh-my-zsh.sh
```

`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`









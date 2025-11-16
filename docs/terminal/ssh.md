
# Setting up for Github
1. Go to a folder to put keys
```
cd ~/.ssh
mkdir keys
cd keys
```
2. Generate public and private key
`ssh-keygen -t ed25519 -C "email@gmail.com"`
3. Add to keychain: start process
`eval "$(ssh-agent -s)"`
4. If first time, create config file
`touch ~/.ssh/config`
5. Add a block per host to the config file; here the key is called mblogs
`vim config`
```
Host *.github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/mblogs
```
6. Add private key to Apple keychain
`ssh-add --apple-use-keychain ~/.ssh/mykeys`
8. Validate its been added
`ssh-add -l -E sha256`
9. Copy the public key to clipboard:
`pbcopy < ~/.ssh/mykeys.pub`
10. Add to Github account as per:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account  

# Check Github Auth
`git remote -v`
ssh-keygen -t ed25519 -C "hychn@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519


cat ~/.ssh/id_ed25519.pub
#add the output to the github ssh key

git clone ssh://git@github.com/hychnh/notes
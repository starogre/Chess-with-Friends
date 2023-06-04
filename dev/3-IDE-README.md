# IDE README

## nvim

The first time you type nvim, it will start installing/configuring all of the plugins, once complete, you can :q
The next time you open nvim you will have access to some cool features

<space> s f - search for files (fuzzy find)

<space> / (inside a file) - nice version of just regular /

`:Telescope` - a nice feature for viewing commits, stash, buffers, git status, and much more

`:LspInfo` - view currently configured servers list

`:Mason` - add / update language servers

`:0G` - vim fugitive (alternatively you can :G but :0G gives you fullscreen fugitive). Fugitive allows for really easy staging/unstaging files. Use `-` when hovered over a file to stage, and `-` when it is staged to remove it from the staging area. Vim hotkeys work in fugitive as well, so entering visual mode, then `-` will stage or unstage multiple files.

`:Git commit -m "commit message"` - another nice fugitive feature

`:Git push`

`g d` - inside a file to jump to definition (uses Lsp)

`g r` - pulls up references inside a file

These are just a few of the nice features this nvim config offers

A note on nvim between exiting/entering the container:

Unfortunately everytime you exit/enter container, nvim will need to repull/build plugins/configurations, persisting this across exits/enters/rebuilds would be a lot of files, so to save space for the more important ssh/git repos I left this out

It's not a huge deal I think but if its annoying having to wait for nvim to repull configs after you have left and then re-entered the container I can change it

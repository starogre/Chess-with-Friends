# IDE README

## nvim

The first time you type nvim, it will start installing/configuring all of the plugins, once complete, you can :q
The next time you open nvim you will have access to some cool features

<space> s f - search for files (fuzzy find)
<space> / (inside a file) - nice version of just regular /
:Telescope - a nice feature for viewing commits, stash, buffers, git status, and much more
:LspInfo - view currently configured servers list
:Mason - add / update language servers
:0G - vim fugitive (alternatively you can :G but :0G gives you fullscreen fugitive). Fugitive allows for really easy staging/unstaging files. Use `-` when hovered over a file to stage, and `-` when it is staged to remove it from the staging area. Vim hotkeys work in fugitive as well, so entering visual mode, then `-` will stage or unstage multiple files.

(unfortunately everytime you exit/enter container, nvim will need to repull/build plugins/configurations, persisting this across exits/enters/rebuilds would be a lot of files, so to save space for the more important ssh/git repos I left this out)



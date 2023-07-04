# IDE README

## Neovim (nvim)

This configuration provides an enhanced experience for Neovim with several handy features.

### Initial Setup

When you run `nvim` for the first time, it will start installing and configuring all of the plugins. This process is automatic, and you can exit once it's complete using `:q`. The next time you open Neovim, all the features will be available.

### Key Features

- `<space> s f`: Search for files (fuzzy find).
- `<space> /`: Enhanced search within a file.
- `:Telescope`: A powerful tool for viewing commits, stash, buffers, git status, and more.
- `:LspInfo`: View the currently configured servers list.
- `:Mason`: Add or update language servers.
- `:0G`: Fullscreen Vim Fugitive, an easy-to-use tool for staging and unstaging files. Use `-` to stage/unstage files. Vim hotkeys work here as well, allowing you to stage or unstage multiple files in visual mode.
- `:Git commit -m "commit message"`: Commit changes with a message.
- `:Git push`: Push changes to the repository.
- `g d`: Jump to definition inside a file (uses LSP).
- `g r`: Pull up references inside a file.

### Note on Persistence

Every time you exit and re-enter the container, Neovim will need to repull and rebuild plugins and configurations. Persisting these files across sessions would consume a significant amount of space, which is prioritized for more critical features such as SSH and Git repositories. If waiting for Neovim to repull configurations becomes a nuisance, adjustments can be made.


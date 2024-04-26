# Modal Editing on Sublime Text 4

A heavily customized fork of https://github.com/meow-edit/sublime-meow

![Logo](meow-subl.svg)

# Keymap

| --- | --- |
| `s` |  Start insert mode |
| `a` |  Start insert mode (append) |

| --- | --- |
| `h` |  Move left by 1 character |
| `l` |  Move right by 1 character |
| `j` |  Move down by 1 line |
| `k` |  Move up by 1 line |
| `H` |  Add 1 char to the left to selection |
| `L` |  Add 1 char to the right to selection  |
| `J` |  Extend selection to line below |
| `K` |  Extend selection to line above |

| --- | --- |
| `o` |  Add next word to selection |
| `O` |  Move to next word |
| `i` |  Add previous word to selection |
| `I` |  Move to previous word |

| --- | --- |
| `u` |  Move to the beginning of line |
| `U` |  Select to the beginning of line |
| `p` |  Move to the end of line |
| `P` |  Select to the end of line |
| `e` |  Insert blank line below |
| `E` |  Insert blank line above |
| `y` |  Join lines |

| --- | --- |
| `alt+j` | Move down by page |
| `alt+k` | Move up by page |
| `g`, `g` | Move to the beginning of file  |
| ` `, `g`, `g` | Select to the beginning of file  |
| `G` | Move to the end of file  |
| ` `, `G` | Select to the end of file  |

| --- | --- |
| `;` | Select whole line (repeat to add next line to selection)  |
| `:` | Select whole line (repeat to add previous line to selection)  |
| `w` | Select word under cursor (repeat to add next occurance to selection)  |
| `m` | Smart expand selection |
| `b` | Create cursor below  |
| `B` | Create cursor above  |

| --- | --- |
| `.` | Insert space character |

| --- | --- |
| `d` | Delete selection |
| `f` | Change selection |
| `x` | Cut selection |
| `c` | Copy selection |
| `C` | Copy line |
| `v` | Paste |
| `V` | Duplicate line  |
| `z` | Undo |
| `Z` | Redo  |

| --- | --- |
| `/` | Search  |
| `q` | Toggle comment  |
| `>` | Indent |
| `<` | Unindent  |

| --- | --- |
| `,` | Switch to next pane  |
| `g`, `v` | Split current pane vertically  |
| `g`, `s` | Split current pane horizontally  |
| `g`, `c` | Close current pane  |
| `g`, `n` | Go to the next tab  |
| `g`, `p` | Go to the previous tab |

| --- | --- |
| ` `, `f` | Open "Goto anything" panel  |
| ` `, `;` | Open command palette  |
| ` `, `e` | Open sidebar  |
| `g`, `d` | Goto definition |
| `g`, `b` | Jump back  |

# Development Guide

Link this project to `~/.config/sublime-text/Packages/`.

Sublime will reload plugins automatically after you make any changes.

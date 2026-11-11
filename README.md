# Kitty configuration

Personal Kitty terminal configuration with a Kanagawa theme, custom key bindings,
custom tab-bar rendering, and a relative-resize kitten.

## Requirements

- [Kitty](https://sw.kovidgoyal.net/kitty/) 0.50 or newer
- Neovim available as `nvim` on `PATH`
- JetBrains Mono and JetBrainsMono Nerd Font installed for the configured font

## Installation

Kitty loads its configuration from `~/.config/kitty`. To use this repository,
clone it there or link the files into that directory:

```sh
git clone <your-repository-url> ~/.config/kitty
```

Restart Kitty after installation. The main configuration is `kitty.conf`.

## Included configuration

- `kitty.conf` — fonts, window behavior, scrollback, tab bar, theme, and shell integration
- `keymap.conf` — keyboard shortcuts, including relative pane resizing
- `relative_resize.py` — Kitty kitten for resizing the active window
- `tab_bar.py` — custom tab-bar renderer
- `kanagawa.conf` and `catppuccin-macchiato.conf` — color schemes
- `kitty-quick-access-terminal.conf` — quick-access terminal settings

## Customization

Edit `kitty.conf` to change the active theme, fonts, editor, or window behavior.
Edit `keymap.conf` to change shortcuts. Kitty resolves included files relative
to the configuration directory, so keep included filenames and their casing
unchanged on case-sensitive systems.

## Validation

The repository's GitHub Actions workflow compiles the Python extensions and
checks that referenced configuration files exist and that personal session
content is not tracked.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

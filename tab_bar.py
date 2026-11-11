#!/usr/bin/env python
# License: GPL v3 Copyright: 2018, Kovid Goyal <kovid at kovidgoyal.net>


from kitty.fast_data_types import get_boss
from kitty.tab_bar import DrawData

AGENTS = {"codex": "codex", "claude": "claude", "pi": "pi"}
SSH = {"ssh": "ssh", "sftp": "sftp"}
TITLE_LENGTH = 20


def draw_title(draw_data: DrawData) -> str:
    tab = draw_data["tab"]
    tab_id = draw_data["tab_id"]
    tab_title = draw_data["title"]
    sup = draw_data["sup"]
    fmt = draw_data["fmt"]
    index = draw_data["index"]
    agent = AGENTS.get(tab.active_exe)
    ssh = SSH.get(tab.active_exe)
    cwd = tab.active_wd.split("/")[-1]
    # tab_t = tab_title.split("|")[0][0:20] if agent else tab_title
    tab_t = tab_title
    if agent:
        t = tab_title.split("|")[0]
        if len(t) > TITLE_LENGTH:
            tab_t = f"{t[0:TITLE_LENGTH]}..."
        else:
            tab_t = t
    else:
        t = tab_t
        if len(t) > TITLE_LENGTH:
            tab_t = f"{t[0:TITLE_LENGTH]}..."
        else:
            tab_t = t

    tab_boss = get_boss().tab_for_id(draw_data["tab_id"])
    active_tab = get_boss().active_tab
    tab_data = (
        tab_boss.data_for_tab_bar(tab_id == active_tab.id) if tab_boss else False
    ) or False
    is_active = tab_data.is_active if tab_data else False
    title = [
        f"󰘳 {index}",
        ":",
        fmt.fg.tab,
        fmt.italic,
        fmt.nobold,
        tab_t,
        fmt.noitalic,
    ]

    title.extend(
        [
            "\n",
            cwd,
            "\x07",
        ]
    )

    # Agent
    if agent:
        agent_color = fmt.fg._447ff5 if is_active else fmt.fg._284c93
        title.extend([fmt.bold, agent_color, f" [{agent}]", fmt.nobold, fmt.fg.tab])

    # SSH
    if ssh:
        agent_color = fmt.fg._cc9704 if is_active else fmt.fg._694d00
        title.extend([fmt.bold, agent_color, f" [{ssh}]", fmt.nobold, fmt.fg.tab])

    # Number of windows also stays superscript
    title.append(sup.num_windows)

    return "".join(title)

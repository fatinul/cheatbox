<div align="center">
<table>
  <tr>
    <td valign="center">
<pre>
       ________               __  ___,               
   / ____/ /_  ___  ____ _/ /_/ __ )____  _  __
  / /   / __ \/ _ \/ __ `/ __/ __  / __ \| |/ /
/ /___/ / / /  __/ /_/ / /_/ /_/ / /_/ />  <`
\____/_/ /_/\___/\__,_/\__/_____/\____/_/|__|
</pre>
    </td>
    <td valign="center">
      <h3>Fastfetch inspired movie reviews</h3>
      <p><em>Catalogue your own movie review inside your terminal.</em></p>
      <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python">
      <img src="https://img.shields.io/github/license/fatinul/mvw" alt="License">
      <br><br>
      <code>pipx install cheatbox</code>
      <br><br>
    </td>
  </tr>
</table>
</div>

<div align="center">
  <h2>CheatBox Showcase</h2>
  <p>See more at: <a href="CHEATSHEET.md">CHEATSHEET.md</a></p>
  <img width="900" src="https://raw.githubusercontent.com/fatinul/cheatbox/master/images/linux.png">
</div>

---

## Features

| Features | Notes |
| :----- | :------ |
| **List Down Cheatsheet** | Using [pick](https://github.com/aisk/pick.git) to list down all available cheatsheet |

## Motivation

I am currently in my job hunting phase. When scrolling on Linkedin, I keep on seeing these _Linux Cheatsheet post_. 

Since a lot of them have different and unconsistent style, I think I can remake them using my own style - aka. terminal style.  

> P/S: If you want to connect, this is my Linkedin -> [Fatinul](www.linkedin.com/in/fatinul)

## Guide
> NOTE: Have `uv` installed

<details>
<summary>👣 Steps</summary>

  1. Clone the repo first

```bash
git clone https://github.com/fatinul/cheatbox
cd cheatbox
uv sync
uv run cheatbox
```

> NOTE: You should see every available cheatsheets after run the code above

2. Create a json file with the domain name `(linux.json, docker.json, ..)` inside the `data/` directory

3. Edit the template below.

<details>
  <summary>📋 JSON template</summary>

  
| Key | Note |
| :----- | :------ |
| **LOGO** | The logo of the cheatsheet, only edit the string inside `[..]` of `"ascii"`. It uses [rich](https://rich.readthedocs.io/en/stable/appendix/colors.html) for color |
| **TITLE** | Similar guide with the LOGO, however not recommend to add any color |
| **STYLE** | `command_width`: left column of each box, `outer_width`: overall bento box width, `primary_color`: Overall color of border, TITLE, etc.. |
| **COMMAND** | Can see the boilerplate of Linux Basic Command. Just change the `command` & `description`. Can add as many as you want but recommended to have around 6 box/subdomain/category |

  
```
{
  "LOGO": [
    {
      "ascii": [
        "    [bold black].--. [/]",
        "   [bold black]|[white]o[/][yellow]_[/][white]o[/] |[/]",
        "   [bold black]|[yellow]:_/[/] |[/]",
        "  [bold black]/[white]/   \\ [/]\\ [/]",
        " [bold black]([white]|     |[/] )[/]",
        "[yellow]/'\\_   _/`\\ [/]",
        "[yellow]\\___)=(___/[/]"
      ]
    }
  ],
  "TITLE": [
    {
      "ascii": [
        "    __    _                 ",
        "   / /   (_)___  __  ___  __",
        "  / /   / / __ \\/ / / / |/ /",
        " / /___/ / / / / /_/ />   <  ",
        "/_____/_/_/ /_/\\__,_/__/|__|  "
      ]
    }
  ],
  "STYLE": {
    "command_width": 8,
    "outer_width": 120,
    "primary_color": "yellow"
  },
  "Basic Commands": [
    {
      "command": "ls",
      "description": "List directory contents"
    },
    {
      "command": "cd",
      "description": "Change directory"
    },
    {
      "command": "pwd",
      "description": "Print working directory"
    }
  ],
  "File Operations": [
    {
      "command": "cat",
      "description": "Concatenate and display file contents"
    },
    {
      "command": "less",
      "description": "View file contents one screen at a time"
    },
    {
      "command": "grep",
      "description": "Search for text within files"
    }
  ]
}
```
</details>


4. After finish editing the `.json` file, run `uv run cheatbox` to choose your json file name

5. **FINISH**. Post on Linkedin or do whatever you want! Have a pull request so others can share your cheatsheet too!

</details>


## Inspiration

`cheatbox` is inspired by the common cheatsheet posts in the Linkedin feed and also [BENTOBOX](https://www.google.com/search?q=bento).

## Running the Application Globally

Install once, then run `cheatbox` from any directory.

**Install**

- pipx (recommended):
  ```bash
  pipx install cheatbox
  ```
- From a cloned repo:
  ```bash
  uv tool install .
  ```

**Set PATH**

- Windows (PowerShell): ensure `C:\Users\<you>\.local\bin` is on PATH. One-time helper:
  ```powershell
  uv tool update-shell
  ```
  Current session only:
  ```powershell
  $env:PATH = "C:\Users\<you>\.local\bin;$env:PATH"
  ```
- Linux/macOS (bash/zsh): ensure `~/.local/bin` is on PATH:
  ```bash
  export PATH="$HOME/.local/bin:$PATH"
  ```

**Run**

```bash
cheatbox
```

## License

GPL-3.0

<div align="center">
  <h3>Drop some star ⭐, would be really appreciated!</h3>
</div>





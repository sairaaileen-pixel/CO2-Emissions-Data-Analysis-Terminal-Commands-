# Foundations Project: Data Literacy Field Notes

Saira Burgos 

**New here?** Start with `PROJECT_OVERVIEW.md` for what you're building and
why. This file (`README.md`) is where the step-by-step setup lives — you're
already in the right place.

**Due:** 2 days (this first project is intentionally short — a couple of
focused days right after this module's content phase, not a full week, since
it's meant to get you moving, not to be a big lift), plus a share-out
during TIP this week. See
`CHECKLIST_TIMELINE.md` for a suggested day-by-day pace and the full
submission checklist.

This repo is a **GitHub template** — a starting point, not something you edit
directly on Marcy's copy of it. This is the first project of the whole
program, so this doc assumes you've never done any of this before. Everyone
in this cohort is on **macOS** — these directions only cover that, on
purpose, so there's no cross-platform noise to wade through.

## Getting started

### Step 1: Get your own copy

On this repo's GitHub page, you'll see two buttons that both sound like "make
a copy" but do different things:

- **"Use this template"** ← use this one. It creates a brand-new, independent
  repository under *your* GitHub account, with no visible link back to this
  template. That's what you want for something that becomes part of your
  portfolio.
- **"Fork"** — creates a copy that stays linked to this one (GitHub will show
  "forked from marcy-lab-school/..." on your repo forever). Fork is the right
  tool when you intend to contribute changes back to the original project —
  that's not this. Don't use Fork here.

Click **"Use this template" → "Create a new repository,"** name it something
like `data-literacy-field-notes`, keep it **public** (the assignment requires
a public repo), and create it.

### Step 2: Set up your tools

Tools for this module (all free):

- **Terminal** — already on your Mac (Applications → Utilities → Terminal, or
  `Cmd+Space` and type "Terminal").
- **Git** — check if it's already installed: open Terminal and run `git
  --version`. If it's not installed, macOS will prompt you to install the
  Xcode Command Line Tools — accept that prompt.
- **GitHub** — free tier, unlimited public repos. Create an account if you
  don't have one.
- **VS Code** — download from https://code.visualstudio.com (the macOS
  `.dmg` build), drag it into Applications. You'll use it to edit Markdown
  files and open a terminal — not to write or run any Python code this
  project; there is none.

### Step 3: Clone your new repo locally

Open **Terminal** (`Cmd+Space`, type "Terminal," hit Enter). On your own new
repo's page (not this template), click the green **Code** button, copy the
HTTPS URL, then:

```bash
git clone <the URL you copied>
cd <your-repo-name>
```

### Step 4: Set up your environment yourself

This module is literally about learning git, GitHub, and the terminal — so
unlike some later projects, this template does **not** come with a
`.gitignore` already made. Creating it yourself is part of the assignment:

- **Create a `.gitignore`.** A `.gitignore` is a plain-text list of files and
  folders git should never track. From the terminal (inside your repo
  folder):
  ```bash
  touch .gitignore
  ```
  Then open `.gitignore` in VS Code, paste in exactly these lines, and save:
  ```
  # macOS creates this hidden file in every folder you open in Finder
  .DS_Store

  # VS Code's per-folder editor settings — personal, not part of the project
  .vscode/

  # Python and Jupyter leftovers — you won't make these in this project,
  # but you will in later modules, so ignore them from day one
  __pycache__/
  .ipynb_checkpoints/
  ```
  Lines starting with `#` are comments — git skips them. A name ending in
  `/` means "ignore this whole folder." You'll be asked about what's in your
  `.gitignore` during share-out, so read the comments rather than just
  pasting.
- **Make your first commit.** Once your `.gitignore` is saved:
  ```bash
  git add .gitignore
  git commit -m "add gitignore"
  git push
  ```

You do **not** need to add a `LICENSE` file for this project.

You should already have `git init`-equivalent setup from cloning (cloning
sets up the local repo and connects the remote for you) — if you're not sure
`git status` and `git remote -v` both work cleanly in this folder, that's the
first thing to check before moving on.

### What your repo should look like once this step is done

```
your-repo-name/
├── .gitignore          ← you create this
├── README.md           ← already here
├── PROJECT_OVERVIEW.md ← already here
├── CHECKLIST_TIMELINE.md ← already here
├── data/               ← already here (the dataset you'll inspect)
└── starter/
    └── field_notes.md  ← already here (what you'll fill in)
```

### Writing bash commands (you'll need this)

Anywhere in this project you write down a terminal command — in
`starter/field_notes.md`, this file, anywhere — write it in a **fenced code
block tagged `bash`**, like this:

````
```bash
git status
```
````

Three backticks, the word `bash`, your command, three backticks to close.
This is the standard way commands are shown in any real README or docs
site — it renders with syntax highlighting and makes the command
copy-pasteable, instead of just sitting in a paragraph as plain text.

## Dataset

Everyone in this cohort uses the same dataset — already included at
`data/co2_emissions_2022.csv`, no download needed. It's a small, curated
slice (254 rows, 6 columns, the year 2022) of OWID's full public CO2 and
Greenhouse Gas Emissions dataset. See `data/SOURCE.md` for exactly how it
was derived and its license (CC BY 4.0, Our World in Data).

Don't substitute a different dataset — using the same one across the cohort
keeps everyone's grading consistent and means classmates can actually compare
notes on what they found.

## What to do

See `starter/field_notes.md` — one file for everything: every section tells
you which terminal command to run, and you fill in the real output you got
plus your answer, starting from a setup log at the top and ending with a
real error you hit along the way (start filling it in from Step 1, don't
reconstruct it at the end). It's where you log commands as you actually run
them, not reconstructed from memory at the end. `CHECKLIST_TIMELINE.md` has
the suggested pace across the 2 days and the full step-by-step checklist.
Your instructor shares the grading rubric separately through the
classroom — not this repo.

Along the way, you're going to hit at least one confusing terminal error —
everyone does. When it happens: read the error message, don't just retype
the command hoping it works. That's exactly what section 9 of
`starter/field_notes.md` is for.

**Where's the exact bar for "done," and what are the optional stretch
goals?** Everything required is in `CHECKLIST_TIMELINE.md`, and the
optional stretch goals are the **Above & Beyond** list at the bottom of
that same file. For the minimum bar in one short list, use the MVP
checklist in the LMS, or go back to the original template repo you created
yours from and switch to its `project-scope` branch to read `MVP.md` (it's
on the *template's* GitHub page, not your own copy — kept off `main` so it
doesn't end up sitting in your portfolio repo).

**Share-out:** this week during TIP, we'll share out your data-quality
questions, how you used AI, and any reflections from the project — so come
ready to talk about your project.



# CO2 Emissions Data Analysis (2022)

## What this project is about
This project is an exploratory first pass at an undocumented climate and energy dataset (`co2_emissions_2022.csv`). As an analyst working for a nonprofit, I needed to check what's actually inside the file using only terminal commands (no Python yet) before trusting it to make community-protection decisions.

## Key Insights
- **Structure:** The dataset is organized in a table (structured CSV), but it has logical mix-ups: it puts real countries right next to continents (like Africa), income groups, and transport sectors like international aviation and shipping.
- **Missing Data:** Running terminal checks showed 36 blank `iso_code` rows and 89 missing `gdp` values.

## My Data Quality Question
Should non-country rows like international aviation (row 122), international shipping (row 127), and missing country rows (76 to 81) be filtered out when calculating emissions for individual countries?

## AI Reflection
Using AI without checking the facts can cause hallucinations or missed data errors. My personal rule to prevent this is: always ask the AI for its sources or references so I can double-check the information myself.
# CO2 Emissions Data Analysis (2022)

## Scenario & Questions
A climate-and-energy nonprofit needs to decide where to direct community-protection and climate-support efforts using a country-level energy and emissions dataset (`data/co2_emissions_2022.csv`) that landed with zero documentation. 

Before building any decisions on top of this data, I set out to answer key questions using terminal commands only:
- What does each column actually hold and what data type is it?
- Is this dataset structured or unstructured?
- Are there missing values or suspicious rows that should make someone cautious?
- What specific question should be asked of the data's source before trusting it?

## Dataset Source
- **Source:** Country-level energy and emissions dataset (`data/co2_emissions_2022.csv`).

## What I Found
Using terminal tools (`head`, `cut`, `grep`), I inspected the raw file and discovered:
- **Structure:** The dataset is structured because it is organized in a table where each data type has its respective column and row. However, it mixes real countries with continents (like Africa), income groups, and transport categories like international aviation and shipping.
- **Column Types:** `country` (String), `iso_code` (String), `year` (Integer), `population` (Integer), `gdp` (Integer), and `co2` (Float).
- **Missing Values:** Running terminal checks revealed 36 blank `iso_code` rows and 89 missing `gdp` values.

## Data Quality Question
Should non-country rows like international aviation (row 122), international shipping (row 127), and missing country rows (76 to 81) be filtered out when calculating emissions for individual countries?

## Reflection & AI-Literacy
- **Risks:** Trusting an AI assistant without checking it yourself can lead to risks like hallucinations or bias/underrepresentation of minorities.

- **My Rule:** Always ask the AI to provide the sources or references so I can check the information myself.
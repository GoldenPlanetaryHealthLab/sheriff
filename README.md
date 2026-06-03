# 🤠 The Sheriff

## 🌵 On the Frontier

Out on **The Frontier**, not everyone who wanders in is supposed to be there.

Data has value. Work has meaning. And the integrity of the system depends on one simple question:

> Are you actually part of **The Frontier**?

The `Sheriff` is the one who asks.

Before any work begins—before data is touched, before 
pipelines run, before claims are made—the `Sheriff` checks your 
papers. Why? Well, in a system built on reproducibility and trust, 
every action must trace back to the same shared ground.

The `Sheriff` doesn’t much care what you’re building.
It doesn’t judge your methods. It only cares that you’re standing inside **The Frontier**.

No Frontier, no work.

⸻

## 🛂 System Role

The `Sheriff` package provides a minimal enforcement layer that 
verifies whether a user is operating within a valid Frontier 
environment.

It establishes a simple contract:

`A user is considered a Frontier citizen if a valid frontier.yml file can be located.`

This validation is performed in two steps:

1. Environment Variable Check
    The `Sheriff` looks for a `FRONTIER` environment variable.
    * If set, it must point to a valid frontier.yml file.
2. Working Directory Check
    If the environment variable is not set, the `Sheriff` inspects the current working directory.
    * It verifies that the path includes the configured Frontier directory name (default: frontier)
    * It then checks for the presence of frontier.yml at the expected root location

If either check succeeds:

* **The Frontier** path is resolved
* The user is validated as a citizen

If both checks fail:

* Validation fails
* Execution should not proceed in Frontier-dependent workflows

This is intentionally minimal.

The `Sheriff` does not enforce data standards, workflow structure, or code quality.
It only establishes that you are (or are not) operating inside a recognized Frontier workspace.

## ⚙️ Installation

We recommend installing the `Sheriff` using `uv`, "An extremely fast Python package and project manager, written in Rust," at the user-level:

```bash
# anywhere in the terminal on FASRC
curl -LsSf https://astral.sh/uv/install.sh | sh

# verify your installation by running "uvx"
# which means "run this in an ephemeral, temporary environment"
uvx pycowsay 'hello world!'
```

Install the `Sheriff`:
```bash
uv tool install https://github.com/GoldenPlanetaryHealthLab/sheriff.git
```

Finally, as the `Sheriff` to check your papers:

```bash
sheriff
```

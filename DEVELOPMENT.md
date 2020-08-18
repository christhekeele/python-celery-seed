Development
===========

Required Software
-----------------

The `.tool-versions` file specifies the languages, databases, and their versions required to work on this project.

If you have [`asdf`](https://github.com/asdf-vm/asdf) installed, running `asdf install` in this project directory will download them for you.

Dependencies
------------

We use `pipenv` as the dependency manager, not just for installation but also to isolate packages installed for this project from others in the system. Any command that needs acces to them should be prefixed with `pipenv run` to make sure they are found correctly.

The `bin/install` and `bin/setup` scripts will install `pipenv`. Additionally, once installed, all other `bin` scripts have an alias in our [`Pipfile`](Pipfile), so you can execute *ex.* `pipenv run format` instead of `pipenv run bin/format`.

Environment
-----------

Many environment variables are required to exist for this project to run. They are documented in [`.env.example`](.env.example) file and available at runtime via the [`app.config`](app/config.py) python module.

You can set these environment variables in your local `.env` file. Prefacing any command with `pipenv run` will ensure the command is executed with these environment variables set.

Tooling
-------

The [`bin`](bin) folder contains tooling scripts to assist with day-to-day development. Generally they should be executed as `pipenv run <tool> args...` instead of `bin/<tool> args...`, with the exception of `bin/install`.

### Setup

- [`bin/install`](bin/install)

  Installs the `pipenv` python dependency manager and all required dependencies it knows about in the [`Pipfile`](Pipfile).

- [`bin/setup`](bin/setup)

  Installs the `pipenv` all development dependencies `pipenv` knows about from the [`Pipfile`](Pipfile).

  Also installs all required git hooks into the project.

### Execution

- [`bin/console`](bin/console)

  Starts a bpython REPL in the project for you to import and execute code manually.

- [`bin/task`](bin/task)

  Executes celery tasks, locally or remotely. Arguments are forwarded to the task.

    - `bin/task local <task> ...args` executes tasks (and their subtasks) locally, synchronously
    - `bin/task remote <task> ...args` runs tasks (and their subtasks) via rabbitMQ queueing
    - `bin/task help` explains these options further

### Operation

- [`bin/migrate`](bin/migrate)

  Exercises database migrations against the configured database.

  Forwards arguments to the `alembic` CLI.

- [`bin/scheduler`](bin/scheduler)

  Starts up a process to trigger regularly scheduled tasks.

  Forwards arguments to the `celery` CLI.

- [`bin/worker`](bin/worker)

  Starts up a process to handle enqueued tasks.

  Forwards arguments to the `celery` CLI.

### Code quality

- [`bin/format`](bin/format)

  Automatically modifies files to a consistent coding standard.

    - `bin/format changed` (default) only operates on files you have modified
    - `bin/format all` runs on all files in the project
    - `bin/format help` explains these options further

- [`bin/lint`](bin/lint)

  Statically checks for common coding issues within the project.

    - `bin/lint changed` (default) only operates on files you have modified
    - `bin/lint all` runs on all files in the project
    - `bin/lint help` explains these options further

#### Pre-commit hook

Following setup instructions will install a git pre-commit hook in this repository that enforces certain code style and quality checks.

This pre-commit hook is equivalent to running [`bin/format`](bin/format) and [`bin/lint`](bin/lint) in succession.

When the pre-commit tool runs, it stashes any un-staged changes and operates just upon the code changes you are trying to introduce into a commit.

The formatter will try to correct as many things as possible that would cause the linter to reject the changes, then the linter runs to make sure no other un-auto-correctable issues are lurking in the changes.

If the formatter modifies your code, or the linter detects other problems with it, the commit is aborted. All staged changes are left staged, all auto-formatted changes are placed unstaged into your index, and then anything stashed at the beginning of the commit is re-introduced.

This forces you to review any changes the formatter made, and address any of the issues the linter detected, by intentionally staging formatter changes into your commit, addressing linter issues, and re-committing.

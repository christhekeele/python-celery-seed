# Development

## Required Software

The `.tool-versions` file specifies the languages, databases, and their versions required to work on this project.

If you are not planning to develop in docker, you will need to have all of them installed. If you are working exclusively in docker, python alone will suffice.

If you have [`asdf`](https://github.com/asdf-vm/asdf) installed, running `asdf install` in this project directory will download them for you.

## Dependencies

We use `pipenv` as the dependency manager, not just for installation but also to isolate packages installed for this project from others in the system. Any command that needs acces to them should be prefixed with `pipenv run` to make sure they are found correctly.

The `bin/install` and `bin/setup` scripts will install `pipenv`. Additionally, once installed, all other `bin` scripts have an alias in our [`Pipfile`](Pipfile), so you can execute _ex._ `pipenv run format` instead of `pipenv run bin/format`.

## Environment

Many environment variables are required to exist for this project to run. They are documented in [`.env.template`](.env.template) file and available at runtime via the [`config`](app/config.py) python module.

You can set these environment variables in your local `.env` file. Prefacing any command with `pipenv run` will ensure the command is executed with these environment variables set.

To get started, it is suggested you `cp .env.template .env` and fill out values. As new required environment variables are added to the project, you will see the app fail to start until you define them in your local `.env`. The easiest way to determine what they should be is to look up the new value in `.env.template` and read the comments concerning it.

## Tooling

The [`bin`](bin) folder contains tooling scripts to assist with day-to-day development. Generally they should be executed as `pipenv run <tool> args...` instead of `bin/<tool> args...`, with the exception of `bin/setup` and `bin/install`.

### Setup

- [`bin/setup`](bin/setup)

  Installs the `pipenv` python dependency manager.

- [`bin/install`](bin/install)

  Installs all required dependencies from the [`Pipfile`](Pipfile).

- [`bin/dev/install`](bin/dev/install)

  Installs all development dependencies from the [`Pipfile`](Pipfile).

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

- [`bin/db/migrate`](bin/db/migrate)

  Exercises database migrations against the configured database.

  Forwards arguments to the `alembic` CLI.

- [`bin/task/scheduler`](bin/task/scheduler)

  Starts up a process to trigger regularly scheduled tasks.

  Forwards arguments to the `celery` CLI.

- [`bin/task/worker`](bin/task/worker)

  Starts up a process to handle enqueued tasks.

  Forwards arguments to the `celery` CLI.

### Code quality

- [`bin/checks/format`](bin/checks/format)

  Automatically modifies files to a consistent coding standard.

  - `bin/checks/format changed` (default) only operates on files you have modified
  - `bin/checks/format all` runs on all files in the project
  - `bin/checks/format help` explains these options further

- [`bin/checks/lint`](bin/checks/lint)

  Statically checks for common coding issues within the project.

  - `bin/checks/lint changed` (default) only operates on files you have modified
  - `bin/checks/lint all` runs on all files in the project
  - `bin/checks/lint help` explains these options further

#### Pre-commit hook

Following setup instructions will install a git pre-commit hook in this repository that enforces certain code style and quality checks.

This pre-commit hook is equivalent to running [`bin/checks/format`](bin/checks/format) and [`bin/checks/lint`](bin/checks/lint) in succession.

When the pre-commit tool runs, it stashes any un-staged changes and operates just upon the code changes you are trying to introduce into a commit.

The formatter will try to correct as many things as possible that would cause the linter to reject the changes, then the linter runs to make sure no other un-auto-correctable issues are lurking in the changes.

If the formatter modifies your code, or the linter detects other problems with it, the commit is aborted. All staged changes are left staged, all auto-formatted changes are placed unstaged into your index, and then anything stashed at the beginning of the commit is re-introduced.

This forces you to review any changes the formatter made, and address any of the issues the linter detected, by intentionally staging formatter changes into your commit, addressing linter issues, and re-committing.

## Running in Docker

While the setup above is needed to work on the project, there is a docker-compose file to let you stand up all the supporting services en masse, rather than install and run all of them locally via `asdf` or similar.

The initial run can take up to 15 minutes to set up, as all these services and dependencies need to be installed. Once in place, it only takes about 30 seconds to turn them all on. With everything running in Docker, it consumes about 0.5 GB of RAM and about 1.5 GB of disk space.

<!-- usage instructions here -->

<!-- login instructions to browsers here -->

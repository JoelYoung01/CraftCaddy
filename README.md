# Vue + FastAPI Application

This is an web application built with Vue 3 and FastAPI.

## Tech Stack

- Vue 3
- Vuetify
- FastAPI
- SQLite
- Docker
- GitHub Actions

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Project Setup

### Step 1 - Clone

CD to the directory you want to clone the repo to and run the following command to clone the repo from GitHub:

```bash
git clone git@github.com:JoelYoung01/VueStaticSiteTemplate.git <project_name_here>
```

### Step 2 - Setup Environment

> This repo has a Task that will run the following steps for you: `Initial Setup`

Copy `.envtemplate` to a new file, `.env`, and fill out applicable values

Setup the backend by creating a venv.

```bash
# Add venv
py -m venv venv
```

When using VSCode, you should have the option to set this venv as your default python interpreter. If the option did not pop up, you can set this opening the cmd palette `Ctrl` + `Shift` + `P` and typing `Python: Select Interpreter` or something similar.

> When setting your venv python as your default interpreter, you will have to reload VSCode before your terminals switch to using that python instance.

Once your venv is active, `echo $env:VIRTUAL_ENV` should return your venv's path.

### Step 3 - Install Dependencies

Install dependencies

```bash
# Install Vite Deps
pnpm i

# Activate venv (only if not already active)
./venv/Scripts/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Run / Build / Deploy

#### Compile and Hot-Reload for Development

> Related Task: `Run Local Dev`

```bash
# Run Vite Dev Server
pnpm dev

# Run FastAPI Dev Server
fastapi dev api/main.py
```

#### Type-Check, Compile and Minify for Production

> Related Task: `pnpm: build`

```bash
pnpm build
```

#### Lint with [ESLint](https://eslint.org/)

> Related Task: `pnpm: lint`

```bash
pnpm lint
```

#### Test Build for Deployment

To test your build, here are the steps:

1. Lint and Build front-end
2. Build Docker Image
3. Run Docker Image

> Related Task: `Test Build for Deployment`

```bash
# Lint and Build front-end
pnpm lint
pnpm build

# Build Docker Image, pulling latest base image
docker build --pull --rm -f Dockerfile -t craft-caddy:latest .

# Run Docker Image
docker run --rm -d -p 8000:8000/tcp --env-file .env -e ENVIRONMENT=staging --name craft-caddy craft-caddy:latest
```

## Deployment

This repo will build your image and push it to your user's ghcr each time you push to the main branch. From here, it is rather up to you how you deploy the image.

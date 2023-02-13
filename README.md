# SideProject-EchoLineBot

## About The Project

Implement echo line bot to get request message from line bot and reply with the same message text.
LineBotSdk, FastApi and GoogleAppEngine are used in this repository.

## Getting Started
### Prerequisites
To setup the environment, install `pipenv` by running the following script (if you use Mac). For other devices, the instruction is in the [link](https://github.com/pypa/pipenv).
```shell
  brew install pipenv
```

#### Setup line bot api service
To access line APIs, implement the following steps, and make sure to record the `Channel Secret` and `Channel Access Token`.

1. Sign up for line developer account api through [official website](https://developers.line.biz/en/) to access APIs.

2. Go to [console](https://developers.line.biz/console/) and create new provider.

3. Enter provider page and create new channel with "Messaging API".

4. In the basic settings page, scroll down to the bottom and get `Channel Secret`.

5. In the messaging api page, scroll down to the bottom and get `Channel Access Token`.

6. In the messaging api page, find the section "Webhook settings" and fill in the url where your server at, and turn on "Use Webhook".

6. Record the `Channel Secret` and `Channel Access Token`.

#### Setup google app engine (optional)
To access [google cloud service](https://cloud.google.com/sdk/gcloud), implement the following steps.

1. Download gcloud-cli install package based on device's platform from https://cloud.google.com/sdk/docs/install

2. Extract the archive by opening the downloaded `.tar.gz` archive file directly.

3. Run the following script to install `google-cloud-sdk`.
```shell
./google-cloud-sdk/install.sh
```

4. Run the following script to initialize the gcloud CLI.
```shell
gcloud init
```

5. Link the project where to deploy the server.
```shell
gcloud config set project <PROJECT_ID>
```

### Installation
To create the environment, run the following script from the root of your project’s directory (where it includes the file `pipfile.lock`).
```shell
  pipenv install
```

To activate the environment, run the following script from the root of your project’s directory (where it includes the file `pipfile.lock`).
```shell
  pipenv shell
```

To run it on google app engine, run the following script to create `requirements.txt`.
```shell
  pipenv lock -r
```

## Usage
### Local Server
1. To select a deploy environment, run the following script in pipenv.
```bash
export ENVIRONMENT=development
export ENVIRONMENT=production
```

2. To set necessary environment variables, run the following scripts in pipenv.
```shell
# Line API Configs
export LINE_CHANNEL_ACCESS_TOKEN="line-channel-access-token"
export LINE_CHANNEL_SECRET="line-channel-secret"
```

3. To deploy the server, run the following scripts from the root of your project’s directory (where it includes the file `main.py`).
```shell
uvicorn main:app --reload
```

4. You will get `500 Internal Server Error` since you do not have the correct `X-Line-Signature` in the headers.

### Google App Engine
1. To select a deploy environment and set necessary environment variables, add `env.yaml` under from the root of your project’s directory (where it includes the file `app.yaml`).
```yaml
env_variables:
  ENVIRONMENT: production

  # Line API Configs
  LINE_CHANNEL_ACCESS_TOKEN: line-channel-access-token
  LINE_CHANNEL_SECRET: line-channel-secret
```

2. To deploy on the app engine, run the following scripts from the root of your project’s directory (where it includes the file `app.yaml`).
```shell
gcloud app deploy
```

3. Get the url and fill in the blank in your line developer, messaging api console.

## Authors
Scarlett Tseng

## License
Theis is released under the under terms of the  [MIT License](https://github.com/tseng1026/SideProject-EchoLineBot/blob/master/LICENSE) .

## FAQ
### Problem: I can run on my local machine, but fail to deploy on app engine.
1. Install the gunicorn by running the following script.
```shell
pip install gunicorn
```

2. Generate the `requirements.txt` by running the following script. Note that `Pipfile` and `Pipfile.lock` is not accepted.
```shell
  pipenv lock -r
```

3. Set configure in `app.yaml` with the following configs.
```yaml
runtime: python39
entrypoint: gunicorn -w=2 -k=uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080 main:app
env_variables:
  ENVIRONMENT: production
includes:
  - env.yaml
```

4. Set configure in `env.yaml` with the following configs.
```yaml
env_variables:
  # Line API Configs
  LINE_CHANNEL_ACCESS_TOKEN: line-channel-access-token
  LINE_CHANNEL_SECRET: line-channel-secret
```

5. Setup `.gcloudignore` to avoid uploading unnecessary files, especially the following files.
```
.gcloudignore
.git
.gitignore
Pipfile
Pipfile.lock
```

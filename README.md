# snow-vue

Aggregate ski weather data, snow conditions, webcam feeds and road conditions.

## Gitlab CI/CD

To create a new runner for a project, use the [gitlab docs](https://docs.gitlab.com/runner/register/index.html)

## Getting Started

### Install Software

Follow the links below to install software needed for this project.

#### Project Wide

- [Yarn](https://yarnpkg.com/en/docs/install)
- `yarn global add appium`
- `yarn global add appium-doctor`

#### iOS Configuration

- install XCode (download iPhone 6 simulator with iOS 12.2)
- `brew install carthage`
- run `appium-doctor --ios` to ensure there are no warnings that require fixing. You can ignore the "Optional" fixes.

#### Android Configuration

- install Android Studio
- export ANDROID_HOME=/Users/dev1/Library/Android/sdk
- export ANDROID_SDK_ROOT=/Users/dev1/Library/Android/sdk
- export PATH=$PATH:$ANDROID_HOME/tools:\$ANDROID_HOME/platform-tools

#### Application

https://nodejs.org/en/download/ 12.13.1
npm install -g vue-cli
vue init webpack my-project

Link to App dynamics dashboard:
https://wwt.saas.appdynamics.com/controller/#/location=EUM_WEB_MAIN_DASHBOARD&timeRange=last_30_minutes.BEFORE_NOW.-1.-1.30&application=4212185

#### Json Mock Server

https://github.com/typicode/json-server
Used to mock response from Api while we figure out all CORS and access issues
yarn global add json-server
This will allow us to run "yarn fake" that will setup a mock web server in http://localhost:3000.

- services/snow-data.js has http://localhost:3000 hard-coded for now. Eventually we should make that be configurable (12/20/2019)

#### API

## Commands

`yarn workspace api unittest`


## Commands

### `yarn install`

Install dependencies for the project.

### `yarn start`

Start the `development` api and the `development` application.

### `yarn start:api`

Start a single run test suite for the `development` api.

### `yarn start:app`

Start the `development` app.

### `yarn test`

Start a single run test suite for the `development` api and the `development` application.

### `yarn test:api`

Start a single run test suite for the `development` api.

### `yarn test:api`

Start a single run test suite for the `development` application.

### `yarn e2e`

Runs e2e tests for web. Make sure `appium` is not running.

### `yarn e2e-ios`

Runs e2e tests for iOS. You must run `appium` in a separate terminal before running this.

### `yarn build`

Build the `production` api and the `production` application.

### `yarn build:api`

Build the `production` api.

### `yarn build:app`

Build the `production` application.

### `yarn deploy`

Deploy the `production` api and the `production` application.

> NOTE: Run `yarn build` before this command.

### `yarn deploy:api`

Deploy the `production` api.

> NOTE: Run `yarn build:api` before this command.

### `yarn build:app`

Deploy the `production` application.

> NOTE: Run `yarn build:app` before this command.

### Wireframes on Zeplin

`https://app.zeplin.io/project/5df157f99d1b34a69f44d7b2`
Login with Google - benchsquadproject@gmail.com, password: Wearebenchsquad

### API endpoints

> Currently hitting on Keystone Data

- https://5kn6ac4359.execute-api.us-east-1.amazonaws.com/dev/traffic?location=80202
- https://5kn6ac4359.execute-api.us-east-1.amazonaws.com/dev/weather

## Heimdall

To log into AWS, use [Heimdall](https://heimdall.asynchrony.com/Project/View?ProjectId=proj-1678)

- Click the `Management Console`
- Navigate to API Gateway
- Navigate to Lambda

## AWS Console

Login to [AWS](https://console.aws.amazon.com/console/home?region=us-east-1)

- Account: 963760208122
- Federated Login: heimdall-admin/firstname.lastname

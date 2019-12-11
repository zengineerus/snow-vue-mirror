# snow-vue

Aggregate ski weather data, snow conditions, webcam feeds and road conditions.

## Getting Started

### Install Software

Follow the links below to install software needed for this project.

#### Project Wide

- [Yarn](https://yarnpkg.com/en/docs/install)
- npm install -g appium
- npm install -g appium-doctor

#### iOS Configuration

- install XCode
- run `appium-doctor --ios` to ensure there are no warnings that require fixing. You can ignore the "Optional" fixes.

#### Android Configuration

- export ANDROID_HOME=/Users/dev1/Library/Android/sdk
- export ANDROID_SDK_ROOT=/Users/dev1/Library/Android/sdk
- export PATH=$PATH:$ANDROID_HOME/tools:\$ANDROID_HOME/platform-tools

#### Application

https://nodejs.org/en/download/ 12.13.1
npm install -g vue-cli
vue init webpack my-project

Link to App dynamics dashboard:
https://wwt.saas.appdynamics.com/controller/#/location=EUM_WEB_MAIN_DASHBOARD&timeRange=last_30_minutes.BEFORE_NOW.-1.-1.30&application=4212185

#### API

TBD

## Commands

### `yarn install`

Install dependencies for the project.

### `yarn start`

Start the `development` api and the `development` application.

### `yarn start:api`

Start the `development` api.

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

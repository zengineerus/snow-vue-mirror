# Front End Snow Vue Quick Start Guide and Notes Please add to and Keep update to date as much as possible

> Running Website  
install yarn  
`yarn`  
`yarn start`

> Testing  App  
`yarn test`  
install java (https://www.oracle.com/technetwork/java/javase/downloads/index.html)  
add java to environment variables  
`yarn e2e`  


//not sure if this command was needed  
yarn global add web-driver



Some resources we followed during the development of this app:  
Vue ionic cordova integration:  
https://www.joshmorony.com/learning-vue-for-ionic-angular-developers-part-5/


HOW TO FIX JAVA_HOME
Find Java 1.8 (not 1.13) and it to
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
export PATH=$PATH:$JAVA_HOME/bin
#!/bin/bash

# "set -e" tells bash to abort the shell script if any
# of the commands below fails
set -e

#complie test project
#xcodebuild \
#  -project /Users/dongdaqing/SVN/uplayer/branches/UPlayer_iOS/youku/tags/youku_original/3.0/YoukuiPhone.xcodeproj \
#  -configuration Release \
#  -sdk iphonesimulator \
#  CONFIGURATION_BUILD_DIR=config_path/YoukuiPhone \
#  TARGETED_DEVICE_FAMILY=1 \
#  build

#run test script
instruments \
  -t ../config_path/YoukuiPhone.tracetemplate \
  -D ../uitest_results/Trace \
  ../config_path/YoukuiPhone/YoukuiPhone.app \
  -e UIARESULTSPATH ../uitest_results \
  -e UIASCRIPT ../../UIAutomation/YoukuiOSTest/uitest/TestSuite.js \
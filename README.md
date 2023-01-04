# ros-test

Project for ROS development within a Docker container using VSCode.


## Clone the repo

Clone this repository to your local development client (eg. Windows laptop) 

```yaml
       git clone https://github.com/kbriankulig/ros-test.git
```


## Setup VSCode

### Install Local Software

Install the following software packages locally: [Docker Desktop](https://docs.docker.com/engine/install/), [VScode](https://code.visualstudio.com/), and [VSCode Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### Run an ROS Container in VSCode

This repository contains a `.devcontainer` folder which defines an ROS container configuration for VSCode.  To run this container:

1. Open the Command Pallate `F1` in VSCode
2. Choose: `Dev Container: Open Folder in Container...`
3. Navigate to and select the `ros-test` folder which contains `.devcontainer`
4. Wait about 1 minute for the container to get created.

To see which VSCode extensions are needed for this project and other container settings look at [.devcontainer/devcontainer.json](https://github.com/kbriankulig/ros-test/blob/vscode/.devcontainer/devcontainer.json)


### Confirm Container Setup

To verify the container was setup corretly:

1. Verify the local repo folder `ros-test` was mounted within the container to `/root/ros-test`
2. Verify that `build` and `devel` folders were created within `/root/ros-test/my_ws`



## Development and Testing

### Run a Unit Test

To run a unit test, setup the shell environment for ROS using [new.bash](https://github.com/kbriankulig/ros-test/blob/vscode/new.bash), then run a unit test script from `my_pkg/test`.  For example to run the unit test for `/scripts/listener.py`:

```yaml
       cd /root/ros-test
       source new.bash
       /root/ros-test/my_ws/src/my_pkg/test/test_listener.py
```

### Run an Integration Test

To run an integration test, setup the shell environment for ROS using [new.bash](https://github.com/kbriankulig/ros-test/blob/vscode/new.bash), then launch a test using a launch script and `rostest`. For example:

```yaml
       cd /root/ros-test
       source new.bash
       rostest my_pkg pub_sub_test.test
```


### Run a Continuous Integration (CI) Test

To add unit and integration tests to the continuous integration workflow, call the tests from the git Actions workflow file [.github/workflows/test-pub-sub-actions.yml](https://github.com/kbriankulig/ros-test/blob/vscode/.github/workflows/test-pub-sub-actions.yml)

To add a unit test:
1. Create a python script in `my_pkg/test` starting with `test_` to define the test.
2. Add an extra line calling the test directly under the "Run unit tests" step in [test-pub-sub-actions.yml](https://github.com/kbriankulig/ros-test/blob/vscode/.github/workflows/test-pub-sub-actions.yml)
3. Push the code to github to run the test.

To add an integration test:
1. Create a python script in `my_pkg/test` to define the test.
2. Create a corresponding launch script in `my_pkg/test`.  Eg. [pub_sub_test.test](https://github.com/kbriankulig/ros-test/blob/unit_tests/my_ws/src/my_pkg/test/pub_sub_test.test)
3. Add the test to the bottom of [my_pkg/CMakeLists.txt](https://github.com/kbriankulig/ros-test/blob/unit_tests/my_ws/src/my_pkg/CMakeLists.txt)
4. Add an extra line calling the launch script under the "Run pub sub test" step in [test-pub-sub-actions.yml](https://github.com/kbriankulig/ros-test/blob/vscode/.github/workflows/test-pub-sub-actions.yml)
5. Push the code to github to run the test.

## Exercise Description

In this exercise will will pre-onboard the same actions but using `wskdeploy` tool this time. We will go over the process of definitn them, importing them under predefined project. And then exporting the assets of that project to the local filesystem.

### Describe the assets

We are going to describe these actions and tag them via `project:name` key. Our yaml file will look like this:

```
project:
  name: pingpong_project
packages:
  exercises:
    version: 1.0
    actions:
      ping:
        function: ../exercise5/ping.py
        runtime: python:2
      pong:
        function: ../exercise5/pong.py
        runtime: python:2
```

### Import the file to Openwhisk

At all-in-one UI open "Lean OW Web CLI".

```
cd FaaS-VIM-Exercises/exercise5b/
```

Invoke the following

```
wskdeploy sync -m manifest.yaml
```

### Verify actions got created

Verify actions got create with special annotations that associate them under the given project.

```
wsk -i action get /guest/exercises/ping
```

```
wsk -i action get /guest/exercises/pong
```

### Export the newly deployed pingpong project

Invoke the following to export the assets to the local filesystem

```
wskdeploy export --projectname pingpong_project -m new_manifest.yaml
```

An `exercise` folder will get created to contain the action assets as well as an additional manifest yaml file to desribe them.


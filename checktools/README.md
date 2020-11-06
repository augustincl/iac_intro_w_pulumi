### Prerequisite

```bash
$source venv/bin/activate
```

## Scenario 1

### Description

We will use the real deployment on the cloud as the backend to use the checktool

* Noted! Please prepare the deployment based on this project with GCP

### Usage

1. Please refer to README of this project to create your own webserver on GCP

2. generate your sshkey

```bash
$ssh-keygen -t rsa -f [name-of-keyfile] -C [your-name-in-this-project]
## please press 'Enter' for all prompted message

```

3. setup your sshkey

<pre>
i. move your keys to checktools folder
ii. open GCP console and enter the page of the target vm instance
iii. press 'Edit'
iv. scroll your page and find ssh option
v. add your public key
</pre>

4. run `pytest --ssh-identity-file=./[your-keyfile] --hosts='ssh://[your-name-in-this-project]@external_instance_ip' test_created_instance.py`

## Scenario 2

### Description

This scenario will not leverage any cloud resource. We just use the local running container as our backend to execute the check tool

### Usage

1. run `docker run -dit --name trynginx nginx:stable`

2. run `pytest -s --hosts='docker://trynginx' checktools/test_created_instance.py`




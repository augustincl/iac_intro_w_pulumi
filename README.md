# Start your first Pulumi with tests

This project includes a basic webserver hosted by ngnix with GCP!
Instance type: e2-small
Region       : asia-east1
network      : premium

This project will leverage the context to provide the examples for unit tests and property tests.
It introduce a tiny tool called [testinfra](https://testinfra.readthedocs.io/). Based on this tool, we could make some convenient for us to check the infrastructure.

Enjoy it!

## Prerequisite

* This project leverages GCP. Please setup your [gcloud SDK](https://cloud.google.com/sdk/docs/install#deb)
* Python 3.7+
* [Pulumi](https://www.pulumi.com/docs/get-started/install/)

## Running the App

1. Download and initialize your environment

    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```
    
2.  Create a new stack:

    ```
    $ pulumi stack init dev
    ```

3.  Configure the project:

    ```
    $ pulumi config set gcp:project YOURGOOGLECLOUDPROJECT
    $ pulumi config set gcp:zone asia-east1-a
    ```

4.  Try the unit tests!

    ```
    $pytest -s --disable-pytest-warnings
    ```

5.  Run `pulumi up --policy-pack policy_tests` to preview and deploy changes:

    ``` 
    $ pulumi up -y
    Previewing update (dev):
        Type                     Name                    Plan       Info
    +   pulumi:pulumi:Stack      iac_intro_w_pulumi-dev  create
    +   ├─ gcp:compute:Address   addr-4-intro            create
    +   ├─ gcp:compute:Network   network-4-intro         create
    +   ├─ gcp:compute:Firewall  firewall-4-intro        create
    +   └─ gcp:compute:Instance  instance-4-intro        create

    Resources:
        + 5 create

    Policy Packs run:
        Name                               Version
        intro-policy-check (policy_tests)  (local)

    Updating (dev):
        Type                     Name                    Status      Info
    +   pulumi:pulumi:Stack      iac_intro_w_pulumi-dev  created
    +   ├─ gcp:compute:Address   addr-4-intro            created
    +   ├─ gcp:compute:Network   network-4-intro         created
    +   ├─ gcp:compute:Firewall  firewall-4-intro        created
    +   └─ gcp:compute:Instance  instance-4-intro        created

    Outputs:
        instance_external_ip  : "35.206.226.215"
        instance_name: {...

    Resources:
        + 5 created
    
    Policy Packs run:
        Name                               Version
        intro-policy-check (policy_tests)  (local)

    Duration: 1m3s
    ```

6.  Curl the HTTP server:

    ```
    $ curl $(pulumi stack output instance_external_ip)
    <html>
        <body>
            <h1>Welcome to KSWS today!<h1>
        </body>
    </html>
    ```

7. Cleanup

    ```
    $ pulumi destroy
    $ pulumi stack rm
    ```
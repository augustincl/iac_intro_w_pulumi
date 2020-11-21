# 開始你的第一個 Pulumi 程式，並且為它撰寫測試案例! 

本專案將透過 GCP 提供採用 ngnix 所架設的簡單網頁伺服器!
| 項目     | 設定       |
| -------- | ---------- |
| 運算實例 | e2-small   |
| 區域     | asia-east1 |
| 採用網路 | standard   |

本專案會基於上述提供的雲端資源環境，來建立單元測試(unit test)與屬性測試(property test)範例。另外，也將介紹一個便利的小工具[testinfra](https://testinfra.readthedocs.io/)。此工具可以讓使用者很簡便地建立一些基於虛擬環境的檢測工具。

讓我們開始體驗吧!

## 專案前置

* 此專案是基於 Google 的雲端服務，為了完成整個佈署，請安裝 [gcloud SDK](https://cloud.google.com/sdk/docs/install#deb)
* Python 3.7+ :warning: 請勿安裝2.x的版本
* [Pulumi](https://www.pulumi.com/docs/get-started/install/)

:mega: 
1. 本專案所有操作都是基於 **LINUX**。
2. 如果是 Windows 的使用者，一些操作指令可能不適用! 請稍加調適。
3. gcloud與pulumi的設置請參考官網，而Python則請用anaconda建立執行環境

## 執行此專案

1. 下載並且初始你的環境

:warning: Windows 使用者請利用 Anaconda 建立虛擬環境，再利用指令安裝 requirements.txt 即可!

    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```
    
2.  建立一個新的堆疊:

    ```
    $ pulumi stack init dev
    ```

3.  設定專案組態屬性:

    ```
    $ pulumi config set gcp:project YOURGOOGLECLOUDPROJECT
    $ pulumi config set gcp:zone asia-east1-a
    ```

4.  執行單元測試!

    ```
    $pytest -s --disable-pytest-warnings tests/*
    ```

5.  執行 `pulumi up --policy-pack policy_tests` 來確認專案程式符合屬性測試的要求，並且開始佈署:

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

6.  Curl 佈署的網頁:

    ```
    $ curl $(pulumi stack output instance_external_ip)
    <html>
        <body>
            <h1>Welcome to KSWS today!<h1>
        </body>
    </html>
    ```

7. 清除環境

:warning: 若建立的網路資源不再使用，請記得刪除所有的網路資源!

    ```
    $ pulumi destroy
    $ pulumi stack rm
    ```

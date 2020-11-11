### 專案前置

```bash
$cd [PROJECT_ROOT]
$source venv/bin/activate
```

## 操作範例一

### 描述

使用真實佈署於 GCP 的網路服務來執行檢測

:mega: 注意! 請基於 GCP 使用本專案所佈署的網路環境!

### 步驟

1. 請參閱本專案的主要 README 在 GCP 上建立網路資源，並且將所在資料夾切換到 checktools 資料夾

2. 產生 sshkey

```bash
$ssh-keygen -t rsa -f [name-of-keyfile] -C [your-name-in-this-project]
## 請對指令執行後的所有提問，直接按 "輸入鍵" 

```

1. 設定產生的公鑰

<pre>
  i. 開啟 GCP 的 VM 資源頁面，並且選取方才建立的虛擬實體
 ii. 點擊 'Edit'
iii. 往下滾動網頁至 ssh 相關的設定
 iv. 將公鑰([name-of-keyfile].pub) 內容複製，並且填入欄位，進行新增
  v. 點擊 'Save'
</pre>

1. 執行 `pytest --ssh-identity-file=./[name-of-keyfile] --hosts='ssh://[your-name-in-this-project]@external_instance_ip' test_created_instance.py`

## 操作範例二

### 描述

此操作不會基於雲端環境，改採用本地端運行的容器作為對象，執行檢測!

### 步驟

1. 執行 `cd PROJECT_ROOT`

2. 執行 `docker run -dit --name trynginx nginx:stable`

3. 執行 `pytest -s --hosts='docker://trynginx' checktools/test_created_instance.py`




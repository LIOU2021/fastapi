# fastapi

## Ref
- [FastAPI](https://fastapi.tiangolo.com/)
- [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)

## Requirements

Python 3.6+

FastAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> for the web parts.
* <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> for the data parts.

## process
- 當uvicorn運行 --reload 模式時，fastapi開啟的進程只會有一個，也無法使用<a hre="https://fastapi.tiangolo.com/de/deployment/server-workers/#uvicorn-with-workers">--workers</a>參數
- 當uvicorn運行production模式時(uvicorn main:app --host 0.0.0.0 --port 80)，此時的進程數將根據機器的CPI計算且分配。<a href="https://fastapi.tiangolo.com/deployment/docker/#number-of-processes-on-the-official-docker-image">參考</a>

```
運行下列指令可以查看目前有幾個uvicorn進程在運作。範例是1個，pid 7。
root@3abac1a6cece:/app# ps -axu
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2416   572 pts/0    Ss+  06:52   0:00 /bin/sh -c uvicorn main:app --host 0.0.0.0 --port 80
root         7  0.2  0.2 150252 35272 pts/0    Sl+  06:52   0:01 /usr/local/bin/python /usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 80
root        12  0.0  0.0   5988  3776 pts/1    Ss   06:52   0:00 bash
root        19  0.0  0.0   8588  3292 pts/1    R+   06:58   0:00 ps -axu
```

## uvicorn
在正式環境下運行時，欲更新環境代碼

```
先查看uvicorn目前占用的進程ID

root@3abac1a6cece:/app# ps -a
  PID TTY          TIME CMD
    7 pts/0    00:00:00 uvicorn
   18 pts/1    00:00:00 ps
```

```
kill該進程ID
root@3abac1a6cece:/# kill 7
root@3abac1a6cece:/#

此時會退出python容器，uvicorn在剛剛運行了shutdown and start
```

```
重新進入python容器
PS C:\Users\jing\Desktop\testdocker\fastapi\fastapi_docker> docker-compose exec python bash
```

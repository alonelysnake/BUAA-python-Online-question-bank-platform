全部基于paddleocr使用, 环境配置步骤如下:
`conda create -n paddle38 python=3.8`  

`pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple`  

然后是安装shapely，但是需要先从[这儿](https://www.lfd.uci.edu/~gohlke/pythonlibs/)下载shapely安装包, 我下载的是Shapely‑1.8.2‑cp38‑cp38‑win_amd64.whl

`pip install Shapely‑1.7.1‑cp38‑cp38‑win_amd64.whl`
`pip install -r requirements.txt`

具体代码可见`infer.ipynb`
# Set up

* nvidia toolkit
* ssh key
* git
* python3
* python venv
* pip
* docker
* veracrypt
* vscode
* comfyui
  - manager
  - install nodes
  - install models

# Terminal

## Find

* find . -name 'Comfy*'
* find . -name 'LTXVideo*'
* find . -name '*' -exec file {} \; | grep -o -P '^.+: \w+ image'
* find . -cmin -5
* find -type f -exec grep -lr "Stable Diffusion WebUI Docker" {} \;

## Docker

* docker ps -l
* docker rm
* docker system prune

# Structure

* checkpoints
  * ltx
  * rp
* clip
  * clip_l
  * t5xxl
  * llava_llama3
* diffusion_models
  * flux
  * hunyuan
* LLM
  * florence2-base
  * llava_llama3 text encoder (þarf þetta?)
* vae
  * flux
  * hunyuan
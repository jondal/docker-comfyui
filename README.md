# Stable Diffusion WebUI Docker

* https://github.com/AbdBarho/stable-diffusion-webui-docker

# Terminal

* find . -name 'Comfy*'
* find . -name 'LTXVideo*'
* find . -name '*' -exec file {} \; | grep -o -P '^.+: \w+ image'
* find . -cmin -5
* find -type f -exec grep -lr "Stable Diffusion WebUI Docker" {} \;
#!/bin/bash

set -Eeuo pipefail

mkdir -vp /stable-diffusion/models/clip/clip-vit-large-patch14
mkdir -vp /stable-diffusion/models/LLM/llava-llama-3-8b-text-encoder-tokenizer

#ln -sf /data/models/clip/clip-vit-large-patch14 /stable-diffusion/models/clip/
#ln -sf /data/models/LLM/llava-llama-3-8b-text-encoder-tokenizer /stable-diffusion/models/LLM/

#cp -r /data/models/clip/clip-vit-large-patch14 /stable-diffusion/models/clip/
#cp -r /data/models/LLM/llava-llama-3-8b-text-encoder-tokenizer /stable-diffusion/models/LLM/

#mkdir -vp /data/config/comfy/custom_nodes
#mkdir -vp /data/user/default/workflows

# declare -A MOUNTS

# MOUNTS["/root/.cache"]="/data/.cache"
# MOUNTS["${ROOT}/input"]="/data/config/comfy/input"
# #MOUNTS["${ROOT}/output"]="/output/comfy"

# for to_path in "${!MOUNTS[@]}"; do
#   set -Eeuo pipefail
#   from_path="${MOUNTS[${to_path}]}"
#   rm -rf "${to_path}"
#   if [ ! -f "$from_path" ]; then
#     mkdir -vp "$from_path"
#   fi
#   mkdir -vp "$(dirname "${to_path}")"
#   ln -sT "${from_path}" "${to_path}"
#   echo Mounted $(basename "${from_path}")
# done

# # install requirements for custom nodes
# for dir in /data/config/comfy/custom_nodes/*/; do
#  if [ -d "$dir" ]; then
#   echo "Install requirements: $dir"
#   (cd "$dir" && pip install -qq -r requirements.txt)
#  fi
# done

# copy workflows
#cp /data/user/default/workflows/* "${ROOT}/user/default/workflows/"

# # startup
# if [ -f "/data/config/comfy/startup.sh" ]; then
#   pushd ${ROOT}
#   . /data/config/comfy/startup.sh
#   popd
# fi

exec "$@"

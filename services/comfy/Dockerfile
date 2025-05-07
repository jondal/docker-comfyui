#FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime
FROM pytorch/pytorch:2.4.1-cuda12.4-cudnn9-runtime

ENV DEBIAN_FRONTEND=noninteractive PIP_PREFER_BINARY=1

# Install libraries
RUN apt-get update && apt-get install -y git && apt-get clean
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ENV ROOT=/stable-diffusion
#RUN --mount=type=cache,target=/root/.cache/pip \
#  git clone https://github.com/comfyanonymous/ComfyUI.git ${ROOT} && \
#  cd ${ROOT} && \
#  git checkout master && \
#  git reset --hard 276f8fce9f5a80b500947fb5745a4dde9e84622d && \
#  pip install -r requirements.txt

# Fetch ComfyUI
RUN --mount=type=cache,target=/root/.cache/pip \
  git clone https://github.com/comfyanonymous/ComfyUI.git ${ROOT} && \
  cd ${ROOT} && \
  git checkout master && \
  pip install -r requirements.txt

WORKDIR ${ROOT}

# Copy from services folder into the container
COPY . /docker/
RUN chmod u+x /docker/entrypoint.sh && cp /docker/extra_model_paths.yaml ${ROOT}

ENV NVIDIA_VISIBLE_DEVICES=all PYTHONPATH="${PYTHONPATH}:${PWD}" CLI_ARGS=""
EXPOSE 7860
ENTRYPOINT ["/docker/entrypoint.sh"]

# Workflows
COPY workflows/*.json /stable-diffusion/user/default/workflows/

# Custom nodes
COPY ./custom_nodes/. /stable-diffusion/custom_nodes/
RUN pip install -r /stable-diffusion/custom_nodes/comfy-image-saver/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfy-mtb/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfy-mtb/extern/GFPGAN/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-cogvideoxwrapper/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-custom-scripts/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-florence2/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-hunyuanvideowrapper/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-kjnodes/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/ComfyUI-LTXVideo/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-manager/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-tensorops/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/comfyui-videohelpersuite/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/efficiency-nodes-comfyui/requirements.txt
RUN pip install -r /stable-diffusion/custom_nodes/rgthree-comfy/requirements.txt

# Custom Python stuff
#RUN pip install GitPython

# CogVideoX (needs to be copied)
#COPY ./CogVideo/. /stable-diffusion/models/CogVideo/

# Run
CMD python -u main.py --listen --port 7860 ${CLI_ARGS}

#&>/dev/null

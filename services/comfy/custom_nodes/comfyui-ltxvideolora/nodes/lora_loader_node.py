import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

def standardize_lora_key_format(lora_sd, ltxv_loader_as_input):
    new_sd = {}
    for k, v in lora_sd.items():
        if ltxv_loader_as_input:
            k = 'diffusion_model.' + k
        else:
            k = k.replace('transformer.', 'diffusion_model.')
        new_sd[k] = v
    return new_sd

class LTXVLoRALoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (
                    "MODEL",
                    {"tooltip": "The model to apply the LoRA to."},
                ),
                "ltxv_loader_as_input": (
                    "BOOLEAN",
                    {
                        "default": False,
                        "tooltip": "True to use the official LTXV Loader as input.",
                    },
                ),
            },
            "optional": {
                "lora": ("LTXVLORA", {"default": None}),
            }
        }
    
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "lora_loader"
    CATEGORY = "LTXVideoLoRA"
    TITLE = "LTXV LoRA Loader"

    def lora_loader(self, model, ltxv_loader_as_input, lora):

        if lora is not None:
            from comfy.sd import load_lora_for_models
            from comfy.utils import load_torch_file
            for l in lora:
                log.info(f"Loading LoRA: {l['name']} with strength: {l['strength']}")
                lora_path = l["path"]
                lora_strength = l["strength"]
                lora_sd = load_torch_file(lora_path, safe_load=True)
                lora_sd = standardize_lora_key_format(lora_sd, ltxv_loader_as_input)
                model, _ = load_lora_for_models(model, None, lora_sd, lora_strength, 0)

        return (model,)
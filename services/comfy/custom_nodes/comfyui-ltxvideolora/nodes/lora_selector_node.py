import folder_paths

class LTXVLoRASelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
               "lora": (folder_paths.get_filename_list("loras"), {"tooltip": "LoRA models are expected to be in ComfyUI/models/loras with .safetensors extension"}),
                "strength": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.0001, "tooltip": "LoRA strength, set to 0.0 to unmerge the LoRA"}),
            },
            "optional": {
                "previous_lora":("LTXVLORA", {"default": None, "tooltip": "For loading multiple LoRAs"}),
                "blocks":("SELECTEDBLOCKS", ),
            }
        }
    
    RETURN_TYPES = ("LTXVLORA",)
    RETURN_NAMES = ("lora", )
    FUNCTION = "get_lora_path"
    CATEGORY = "LTXVideoLoRA"
    TITLE = "LTXV LoRA Selector"
    DESCRIPTION = "Select a LoRA model from ComfyUI/models/loras"

    def get_lora_path(self, lora, strength, blocks=None, previous_lora=None, fuse_lora=False):
        loras_list = []
        lora = {
            "path": folder_paths.get_full_path("loras", lora),
            "strength": strength,
            "name": lora.split(".")[0],
            "fuse_lora": fuse_lora,
            "blocks": blocks
        }
        if previous_lora is not None:
            loras_list.extend(previous_lora)
        loras_list.append(lora)
        return (loras_list,)
from .nodes.lora_loader_node import LTXVLoRALoader
from .nodes.lora_selector_node import LTXVLoRASelector
from .nodes.lora_block_node import LTXVLoRABlockEdit

NODE_CLASS_MAPPINGS = {
    "LTXVLoRALoader": LTXVLoRALoader,
    "LTXVLoRASelector": LTXVLoRASelector,
    "LTXVLoRABlockEdit": LTXVLoRABlockEdit,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LTXVLoRALoader": "LTXV LoRA Loader",
    "LTXVLoRASelector": "LTXV LoRA Selector",
    "LTXVLoRABlockEdit": "LTXV LoRA Block Edit",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
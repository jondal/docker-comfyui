class LTXVLoRABlockEdit:
    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        arg_dict = {}
        argument = ("BOOLEAN", {"default": True})

        for i in range(28):
            arg_dict["blocks.{}.".format(i)] = argument

        return {"required": arg_dict}

    RETURN_TYPES = ("SELECTEDBLOCKS", )
    RETURN_NAMES = ("blocks", )
    FUNCTION = "selected_blocks"
    CATEGORY = "LTXVideoLoRA"
    TITLE = "LTXV LoRA Block Edit"
    OUTPUT_TOOLTIPS = ("The modified diffusion model.",)

    def selected_blocks(self, **kwargs):
        selected_blocks = {k: v for k, v in kwargs.items() if v is True}
        print("Selected blocks: ", selected_blocks)
        return (selected_blocks,)
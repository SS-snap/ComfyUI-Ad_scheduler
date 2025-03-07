import comfy.utils
import comfy.sample
import comfy.samplers
import torch

class AD_Scheduler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "scheduler": (comfy.samplers.SCHEDULER_NAMES,),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                "step_ratio": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("SIGMAS",)
    CATEGORY = "Snap Processing"
    FUNCTION = "get_sigmas"

    def get_sigmas(self, model, scheduler, steps, denoise, sigmas_ratio):

        total_steps = steps
        if denoise < 1.0:
            if denoise <= 0.0:
                return (torch.FloatTensor([]),)
            total_steps = int(steps / denoise)

        sigmas = comfy.samplers.calculate_sigmas(
            model.get_model_object("model_sampling"),
            scheduler,
            total_steps
        ).cpu()

        sigmas = sigmas[-(steps + 1):]

        steps_count = max(sigmas.shape[-1] - 1, 0)
        total_steps_split = round(steps_count * sigmas_ratio)

        sigmas2 = sigmas[-(total_steps_split + 1):]

        return (sigmas2,)

NODE_CLASS_MAPPINGS = {
    "AD_Scheduler": AD_Scheduler
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "AD_Scheduler": "AD_Scheduler"
}

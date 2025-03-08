## Node Introduction
This node is used to enhance image details. We can add a latent space image and introduce any amount of noise. Then, we can start denoising at any timestep. This allows us to add more details to the image while maintaining overall consistency as much as possible.

## How to control?
In the example workflow, there are three recommended adjustment parameters. Ratio controls the step at which we start denoising. For example, if the total number of steps is 30 and we set it to 0.1, it means denoising starts at step 30 × 0.1, which is the 3rd step, leaving 27 steps for denoising. Denoise controls the denoising strength during this period. Inject_noise controls the amount of noise to be added.

Different images will not have the same parameters, but we can determine the limits of an image through testing. For example, in the image below

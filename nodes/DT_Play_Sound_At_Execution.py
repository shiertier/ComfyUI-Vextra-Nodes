import subprocess, sys, os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
try:
    from pygame import mixer
except ModuleNotFoundError:
    # install pixelsort in current venv
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    from pygame import mixer

try:
    mixer.init()
except pygame.error as e:
    if 'ALSA: Couldn\'t open audio device: No such file or directory' in str(e):
        print("Failed to open audio device, from ComfyUI\custom_nodes\ComfyUI-Vextra-Nodes\nodes\DT_Play_Sound_At_Execution.py")
        sys.exit(1)

def PlaySound(path, volume):
    mixer.music.load(path)
    mixer.music.set_volume(volume)
    mixer.music.play()

class Play_Sound_RealTime():
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),
                "path": ("STRING", {"default": 'change_me.mp3'}),
                "volume": ("FLOAT", {"default": 1, "min": 0.0, "max": 1.0, "step": 0.01}),
                },
            "optional": {
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_sound"
    
    OUTPUT_NODE = True

    CATEGORY = "VextraNodes"

    def do_sound(self, images, path, volume):
        PlaySound(path, volume)
        return {
            "result": (images, ),
        }

NODE_CLASS_MAPPINGS = {
    "Play Sound At Execution": Play_Sound_RealTime
}

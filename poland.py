# ok so i made this on a crappy phone so dont expect ts to be good or work
import moviepy
video = VideoFileClip("./ScreenRecording_08-08-2025 21-36-28_1.mov")
words = ["blue", "red", "green", "economically viable", "conservative", "liberal", "evil", "sigma", "brainrotted", "Messi", "Canadian", "European", "Playboi Carti", "British", "small content creator", "TikTok", "male", "crazy", "forsaken fan", "roblox fan", "fnaf", "environmentally friendly", "unemployed", "American", "rapper"]
for likeword in words:
    for commentword in words:
        zetext = TextClip{
            text = f"which is better: \n {likeword}: like the video \n or \n {commentword}: comment on the video \n \n im trying to revive this sound, \n remix the video to help me!"
        }
        final = CompositeVideoClip(
            [video, zetext]
        )
        final.write_videofile(f"./{likeword}{commentword}")
    
        
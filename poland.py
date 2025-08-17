# ok so i made this on a phone so dont expect ts to be good or work
from moviepy.editor import VideoFileClip , TextClip, CompositeVideoClip
video = VideoFileClip("./ScreenRecording_08-08-2025 21-36-28_1.mov")
words = ["blue", "red", "green", "economically viable", "conservative", "liberal", "evil", "sigma", "brainrotted", "Messi", "Canadian", "European", "boring", "British", "small content creator", "TikTok", "male", "crazy", "forsaken fan", "roblox fan", "fnaf", "environmentally friendly", "unemployed", "American", "rapper", "don't click the sound", "do click the sound", "thank you gamer-guy12 (github) for helping", "loving"]
for likeword in words:
    for commentword in words:
        zetext = TextClip(
            f"which is better: \n {likeword} polen: like the video \n or \n {commentword} polen: comment on the video \n \n im trying to revive this sound, \n remix the video to help me!",
            fontsize=50
            ).set_duration(12).set_position('center')
        final = CompositeVideoClip(
            [video, zetext]
        )
        final.write_videofile(f"./videos/{likeword} #polen or {commentword} polen.mp4", codec='mpeg4')
    
        

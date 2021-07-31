from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

video = VideoFileClip("wol-dev.mp4")


def text_clip(text: str, duration: int, start_time: int = 0):
    """Return a description string on the bottom-left of the video

    Args:
        text (str): Text to show
        duration (int): Duration of clip
        start_time (int, optional): Time in video to start at (in seconds).
        Defaults to 0.

    Returns:
        moviepy.editor.TextClip: A instance of a TextClip
    """
    return (TextClip(text, font="Arial", fontsize=24, color='black')
            .set_position((20, video.h - 44))
            .set_duration(duration)
            .set_start(start_time))


# Make the text. Many more options are available.
text_clip_one = text_clip("Create tasks and subtasks", 3)
text_clip_two = text_clip("Sort subtasks by table header", 3, 3)
text_clip_three = text_clip("View goals", 3, 6)

# Overlay text on video
result = CompositeVideoClip(
    [video, text_clip_one, text_clip_two, text_clip_three])
result.write_videofile("wol_dev_edited.mp4", fps=25)
result.write_gif("wol_dev_edited.gif", fps=8)
video.write_gif("original.gif", fps=8)

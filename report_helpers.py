# **************************************************************
# ***************** Report Helper Functions ********************
# **************************************************************
from pathlib import Path
from pyautogui import size, screenshot, position # ignore
from numpy import array
import cv2
import base64
import json
import allure # ignore



def attach_images_to_report(baseline_dir_path: str, actual_dir_path: str) -> None:
    """ Attach baseline/actual image to the allure report

    Args:
        baseline_dir_path: baseline image directory path
        actual_dir_path: actual image directory path
    """
    # read the files and encode to base64
    baseline: base64 = base64.b64encode(Path(baseline_dir_path).read_bytes()).decode()
    actual: base64 = base64.b64encode(Path(actual_dir_path).read_bytes()).decode()
    # diff = base64.b64encode(Path("diff.png").read_bytes()).encode()

    # wrap is a JSON obj, then encode as bytes
    content: base64 = json.dumps({
        "expected": f"data:image/png;base64, {baseline}",
        "actual": f"data:image/png;base64, {actual}"
    }).encode()
    # "diff": f"data:image/png;base64, {diff}"

    # attach to the report
    allure.attach(content, name="Screenshot diff", attachment_type="application/vnd.allure.image.diff")


def capture_screen_video(output_file_dir: str, stop_event: str, fps: int = 20) -> None:
    """Captures the screen video and writes it to the specified output file.

    Args:
        output_file_dir (str): The directory where the output video file will be saved.
        stop_event (threading.Event): An event to signal when to stop
        fps (int): Frames per second for the video. Defaults to 20.
    """

    codec: int = cv2.VideoWriter.fourcc(*"mp4v") # coded for MP4 format
    screen_size: tuple[int, int] = size() # Get the size of the primary monitor
    writer: cv2.VideoWriter = cv2.VideoWriter(output_file_dir, codec, fps, screen_size)

    while not stop_event.is_set():
        screenshot: object = pyautogui.screenshot()
        frame: array = cv2.cvtColor(array(screenshot), cv2.COLOR_RGB2BGR)

        # Get current mouse position
        x_coord, y_coord = position()
        cursor_radius: int = 5
        cv2.circle(frame, (x_coord, y_coord), cursor_radius, (0, 255, 0) -1) # draw cursor

        writer.write(frame) # write the frame to the video file
    writer.release()
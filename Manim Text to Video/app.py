from manim import *
import json

# Load the JSON object
with open('your_file.json') as f:
    data = json.load(f)

class TextAnimation(scene): # type: ignore
    def render_text(self, text_data):
        # Create a Paragraph object for text wrapping
        text_obj = Paragraph(*text_data['text'].split('\n'), line_spacing=1)

        # Calculate the initial font size
        initial_font_size = 48  # You can adjust this value

        # Scale the text object to fit within 80% of the screen width
        target_width = config.frame_width * 0.8

        # Adjust font size until the text fits within the target width
        while text_obj.width > target_width:
            initial_font_size *= 0.9  # Decrease font size by 10%
            text_obj.scale(0.9)

        # Center the text object
        text_obj.move_to(ORIGIN)

        # Add the text object to the scene
        self.add(text_obj)

        # Wait for the specified duration
        self.wait(text_data['duration'])

        # Remove the text object from the scene
        self.remove(text_obj)

    def construct(self):
        # Render each text sequentially
        for text_data in data:
            self.render_text(text_data)

# Render the scene
if __name__ == "__main__":
    scene = TextAnimation()
    scene.render()
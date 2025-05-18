from manim import *

class TransformerScene(Scene):
    def construct(self):
        # Create the transformer components
        primary_coil = Circle(
            radius=2,
            color=RED,
            fill_opacity=0.5,
            stroke_width=2
        ).shift(LEFT * 3)
        
        secondary_coil = Circle(
            radius=2,
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=2
        ).shift(RIGHT * 3)
        
        core = Rectangle(
            width=2,
            height=4,
            color=GREY,
            fill_opacity=0.8,
            stroke_width=1
        )
        
        # Create labels
        primary_label = Text(
            "Primary Coil",
            font_size=24,
            color=YELLOW
        ).shift(LEFT * 3).shift(UP * 3)
        
        secondary_label = Text(
            "Secondary Coil",
            font_size=24,
            color=YELLOW
        ).shift(RIGHT * 3).shift(UP * 3)
        
        core_label = Text(
            "Core",
            font_size=24,
            color=YELLOW
        ).shift(UP * 2)
        
        # Create energy flow arrow
        arrow = Arrow(
            start=LEFT * 4,
            end=RIGHT * 4,
            color=YELLOW,
            stroke_width=2
        )
        
        # Construct the scene
        self.play(
            Create(primary_coil),
            Create(secondary_coil),
            Create(core),
            Create(primary_label),
            Create(secondary_label),
            Create(core_label)
        )
        
        # Animate energy flow
        self.play(
            primary_coil.animate.scale(1.1).set_color(RED),
            secondary_coil.animate.scale(1.1).set_color(BLUE),
            arrow.animate.pulse(),
            rate_func=smooth_bounce,
            run_time=2
        )
        
        self.play(
            arrow.animate.pulse(),
            rate_func=smooth_bounce,
            run_time=1
        )
        
        self.play(
            primary_coil.animate.scale(0.9).set_color(RED),
            secondary_coil.animate.scale(0.9).set_color(BLUE),
            rate_func=smooth_bounce,
            run_time=1
        )
        
        self.wait(2)
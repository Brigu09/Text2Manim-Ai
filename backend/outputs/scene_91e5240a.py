from manim import *

class CPUScene(Scene):
    def construct(self):
        # Create CPU shape
        cpu = Rectangle(
            color="#1a73e8",
            fill_opacity=0.8,
            width=4,
            height=3
        ).shift(ORIGIN)

        # Add internal components
        die = Rectangle(
            color="#e91e63",
            fill_opacity=0.8,
            width=2,
            height=1.5
        ).shift(ORIGIN)

        # Add pins
        pins = VGroup(
            *[
                Line(
                    start=ORIGIN,
                    end=DOWN,
                    color="#00bc00"
                ).shift( (i*0.5, -1.5, 0) )
                for i in range(8)
            ]
        )

        # Add pin labels
        pin_label = Text(
            "Pins",
            color=WHITE,
            font_size=20
        ).shift( (3.5, -1.5, 0) )

        # Add labels
        cpu_label = Text(
            "CPU",
            color=WHITE,
            font_size=24
        ).shift( (0, 1.5, 0) )

        die_label = Text(
            "Die",
            color=WHITE,
            font_size=20
        ).shift( (0, 0.75, 0) )

        # Add title
        title = Text(
            "Central Processing Unit (CPU)",
            color=WHITE,
            font_size=28
        ).shift( (0, 3, 0) )

        # Animation sequence
        self.add(title)
        self.play(FadeIn(cpu), run_time=1)
        self.wait(1)
        self.play(FadeIn(die), run_time=1)
        self.wait(1)
        self.play(FadeIn(pins), FadeIn(pin_label), run_time=1)
        self.wait(1)
        self.play(FadeIn(cpu_label), FadeIn(die_label), run_time=1)
        self.wait(2)
        self.play(FadeOut(cpu), FadeOut(die), FadeOut(pins), FadeOut(pin_label),
                 FadeOut(cpu_label), FadeOut(die_label), FadeOut(title), run_time=2)
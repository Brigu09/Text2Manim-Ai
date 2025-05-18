from manim import *
from manim.color import *

class CPUBlocksScene(Scene):
    def construct(self):
        # Create CPU block
        cpu = Rectangle(
            width=4.0,
            height=2.5,
            corner_radius=0.3,
            color=BLUE,
            fill_opacity=0.8
        ).shift(ORIGIN)
        
        # Create thread blocks
        thread_block1 = Rectangle(
            width=0.8,
            height=1.0,
            corner_radius=0.2,
            color=BLUE_E,
            fill_opacity=0.8
        ).next_to(cpu, RIGHT, buff=0.2)
        
        thread_block2 = Rectangle(
            width=0.8,
            height=1.0,
            corner_radius=0.2,
            color=BLUE_E,
            fill_opacity=0.8
        ).next_to(thread_block1, RIGHT, buff=0.2)
        
        thread_block3 = Rectangle(
            width=0.8,
            height=1.0,
            corner_radius=0.2,
            color=BLUE_E,
            fill_opacity=0.8
        ).next_to(thread_block2, RIGHT, buff=0.2)
        
        thread_block4 = Rectangle(
            width=0.8,
            height=1.0,
            corner_radius=0.2,
            color=BLUE_E,
            fill_opacity=0.8
        ).next_to(thread_block3, RIGHT, buff=0.2)
        
        # Create labels
        cpu_label = Text("CPU", font_size=40, color=BLACK).next_to(cpu, UP, buff=0.1)
        threads_label = Text("Threads", font_size=30, color=BLACK).next_to(thread_block1, UP, buff=0.1)
        
        thread_labels = [
            Text(f"Thread {i+1}", font_size=15, color=BLACK)
            .scale(0.7)
            .next_to(block, DOWN, buff=0.1)
            for i, block in enumerate([thread_block1, thread_block2, thread_block3, thread_block4])
        ]
        
        # Animation sequence
        self.play(
            Create(cpu),
            Create(cpu_label),
            run_time=1.5
        )
        
        for block, label in zip([thread_block1, thread_block2, thread_block3, thread_block4], thread_labels):
            self.play(
                Create(block),
                Create(label),
                run_time=0.8
            )
        
        self.play(
            Create(threads_label),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # Highlight animation
        self.play(
            cpu.animate.scale(1.05).set_color(BLUE_DARK),
            run_time=0.8
        )
        
        self.wait(2.0)
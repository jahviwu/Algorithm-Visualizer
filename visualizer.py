import tkinter as tk

# Global control variables
is_running = False
current_step = 0
animation_id = None   # stores the after() callback so we can cancel it


def draw_bars(canvas, arr, highlight1, highlight2, canvas_width, canvas_height):
    canvas.delete("all")
    bar_width = canvas_width / len(arr)
    max_val = max(arr)

    for i, val in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - (val / max_val) * (canvas_height - 20)
        x1 = (i + 1) * bar_width
        y1 = canvas_height

        color = "orange" if i == highlight1 or i == highlight2 else "skyblue"

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text(x0 + bar_width/2, y0 - 10, text=str(val), font=("Arial", 10))


def animate(canvas, steps, canvas_width, canvas_height, speed_scale):
    global current_step, is_running, animation_id

    if not is_running:
        return  # paused

    if current_step < len(steps):
        arr, h1, h2 = steps[current_step]
        draw_bars(canvas, arr, h1, h2, canvas_width, canvas_height)

        current_step += 1

        delay = int(speed_scale.get())  # slider controls speed
        animation_id = canvas.after(delay, animate, canvas, steps, canvas_width, canvas_height, speed_scale)


def start_animation(canvas, steps, canvas_width, canvas_height, speed_scale):
    global is_running, current_step
    if not is_running:
        is_running = True
        animate(canvas, steps, canvas_width, canvas_height, speed_scale)


def stop_animation(canvas):
    global is_running, animation_id
    is_running = False
    if animation_id:
        canvas.after_cancel(animation_id)


def reset_animation(canvas):
    global current_step, is_running
    is_running = False
    current_step = 0
    canvas.delete("all")


def run_visualizer(steps):
    root = tk.Tk()
    root.title("Sorting Visualizer")

    canvas_width = 800
    canvas_height = 400

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Speed slider
    speed_scale = tk.Scale(root, from_=10, to=1000, orient="horizontal",
                           label="Animation Speed (ms per step)")
    speed_scale.set(200)
    speed_scale.pack()

    # Buttons
    start_btn = tk.Button(root, text="Start", command=lambda: start_animation(canvas, steps, canvas_width, canvas_height, speed_scale))
    start_btn.pack(side="left", padx=10, pady=10)

    stop_btn = tk.Button(root, text="Stop", command=lambda: stop_animation(canvas))
    stop_btn.pack(side="left", padx=10, pady=10)

    reset_btn = tk.Button(root, text="Reset", command=lambda: reset_animation(canvas))
    reset_btn.pack(side="left", padx=10, pady=10)

    root.mainloop()

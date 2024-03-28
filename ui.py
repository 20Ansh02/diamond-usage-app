import tkinter as tk
from tkinter import messagebox
from diamond_optimizer import DiamondManager, NecklaceDesignManager, DiamondUsageOptimizer

class DiamondOptimizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Diamond Optimizer")

        self.label = tk.Label(master, text="Total Necklaces Crafted:")
        self.label.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.run_button = tk.Button(master, text="Run Optimization", command=self.run_optimization)
        self.run_button.pack()

    def run_optimization(self):
        total_necklaces_crafted = DiamondUsageOptimizer.optimize_usage()
        self.result_label.config(text=str(total_necklaces_crafted))
        messagebox.showinfo("Optimization Complete", f"Total necklaces crafted: {total_necklaces_crafted}")

def main():
    # Initialize DiamondManager and NecklaceDesignManager with sample data
    DiamondManager.add_diamond(size=0.5)
    DiamondManager.add_diamond(size=0.75, status='returned')
    DiamondManager.add_diamond(size=1.0)
    NecklaceDesignManager.create_necklace_design(name='Simple Necklace', required_diamonds={0.5: 1, 1.0: 2})
    NecklaceDesignManager.create_necklace_design(name='Fancy Necklace', required_diamonds={0.75: 3, 1.0: 1})

    # Create Tkinter root window and launch the app
    root = tk.Tk()
    app = DiamondOptimizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import *
import webview


root = tk.Tk()
def circuits():
    root.geometry('700x700')
    webview.create_window('CIRCUITS','https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html')
    webview.start()

def chem():
    root2 = tk.Tk()
    root2.geometry('700x700')
    webview.create_window('PERIODIC TABLE','https://artsexperiments.withgoogle.com/periodic-table/')
    webview.start()

def skeleton():
    root3 = tk.Tk()
    root3.geometry('700x700')
    webview.create_window('SKELETAL SYSTEM','https://www.artec3d.com/3d-models/human-skeleton-hd')
    webview.start()
import sys
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, scrolledtext
import openpyxl

# === Optional: DPI Awareness for Windows High-DPI Displays ===
if sys.platform == "win32":
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(2)  # Per-monitor DPI awareness
    except Exception:
        pass

def get_numeric_values_from_excel(excel_file):
    """
    Loads the Excel file and returns a list of all numeric values found
    (scanning the active worksheet).
    """
    wb = openpyxl.load_workbook(excel_file, data_only=True)
    ws = wb.active

    values = []
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, (int, float)):
                values.append(cell.value)
    return values

def find_best_subset(numbers, target, tolerance=0.01):
    """
    Dynamic programming approach to find ONE subset whose sum is
    closest to 'target'. We store possible sums (rounded to 2 decimals)
    in a dictionary: dp[sum] = subset leading to that sum.

    Returns (best_subset, best_sum).

    Because we're rounding to 2 decimals, we might lose some tiny precision,
    but it keeps the DP table from exploding due to float drift.
    """
    if not numbers:
        return ([], 0.0)

    # dp[s] = list of numbers that produce sum s
    dp = {0.0: []}  # start with sum=0.0 from an empty subset

    for num in numbers:
        current_dp = dict(dp)  # copy existing sums

        for existing_sum, subset in dp.items():
            new_sum = existing_sum + num
            # Round to 2 decimals to avoid too many float duplicates
            rounded_sum = round(new_sum, 2)

            # If we haven't encountered this sum yet, store the subset
            if rounded_sum not in current_dp:
                current_dp[rounded_sum] = subset + [num]

        dp = current_dp  # update dp with newly formed sums

    # At this point, dp contains all possible sums (rounded).
    # Let's find the sum closest to our target.
    best_sum = None
    best_subset = []
    min_diff = float("inf")

    for possible_sum, subset in dp.items():
        diff = abs(possible_sum - target)
        if diff < min_diff:
            min_diff = diff
            best_sum = possible_sum
            best_subset = subset

    # If you'd like to strictly enforce the ±tolerance, you could check:
    # if min_diff > tolerance: return (None, None)

    return (best_subset, best_sum)

def show_result_popup(root, subset, target, subset_sum):
    """
    Displays the best subset and sum in a scrollable text area
    so the user can highlight and copy the text.
    """
    top = tk.Toplevel(root)
    top.title("Best Subset")

    # Create a ScrolledText widget so the user can scroll, select, and copy
    text_area = scrolledtext.ScrolledText(top, width=60, height=15, wrap=tk.WORD)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    if not subset:
        # Means we either had no numbers or couldn't find a subset
        content = (
            f"No valid subset found, or no numeric cells. \n"
            f"Target was: {target}"
        )
        subset_sum = 0.0
    else:
        diff = abs(subset_sum - target)
        content = (
            f"Target: {target}\n"
            f"Closest Sum: {subset_sum} (diff = {round(diff, 2)})\n\n"
            f"Subset:\n{subset}\n\n"
            f"Sum of subset = {round(subset_sum, 2)}"
        )

    # Insert the text into the text_area
    text_area.insert(tk.END, content)

    # Disable editing but still allow highlighting
    text_area.config(state=tk.DISABLED)

    # A Close button
    btn_close = tk.Button(top, text="Close", command=top.destroy)
    btn_close.pack(pady=5)

def main():
    root = tk.Tk()
    root.withdraw()

    # Step 1: Ask user for Excel file
    excel_path = filedialog.askopenfilename(
        title="Select an Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if not excel_path:
        return

    # Step 2: Ask user for target number
    target_str = simpledialog.askstring(
        "Target Number",
        "Enter the target number (e.g. 100.00):",
        parent=root
    )
    if not target_str:
        return

    try:
        target = float(target_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")
        return

    # Step 3: Ask user for tolerance (not strictly enforced in the DP final step,
    #         but you could filter out sums beyond ±tolerance if you wish)
    tol_str = simpledialog.askstring(
        "Tolerance",
        "Enter a margin of error (e.g. 0.01). \n(This influences rounding in DP.)",
        parent=root
    )
    if not tol_str:
        return
    try:
        tolerance = float(tol_str)
    except ValueError:
        tolerance = 0.01

    # Step 4: Get numeric cells from Excel
    numbers = get_numeric_values_from_excel(excel_path)
    if not numbers:
        messagebox.showinfo("No Numbers", "No numeric cells found in the file.")
        return

    # Step 5: Find best subset
    subset, subset_sum = find_best_subset(numbers, target, tolerance)

    # Step 6: Show results in a scrollable, selectable text popup
    show_result_popup(root, subset, target, subset_sum)

    root.mainloop()

if __name__ == "__main__":
    main()

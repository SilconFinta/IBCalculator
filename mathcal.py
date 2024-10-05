import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate_missing_value():
    try:
        timescal()
        principal = entry_principal.get()
        annual_rate = entry_annual_rate.get()
        months = entry_months.get()
        monthly_payment = entry_monthly_payment.get()
        final_balance = entry_remaining_balance.get()

        if principal.lower() != 'none':
            principal = float(principal)
        else:
            principal = None

        if annual_rate.lower() != 'none':
            annual_rate = float(annual_rate) / 100
        else:
            annual_rate = None

        if months.lower() != 'none':
            months = float(months)
        else:
            months = None

        if monthly_payment.lower() != 'none':
            monthly_payment = float(monthly_payment)
        else:
            monthly_payment = None

        if final_balance.lower() != 'none':
            final_balance = float(final_balance)
        else:
            final_balance = None

        if principal is None:
            principal = (monthly_payment * (1 - (1 + annual_rate / c_d) ** -(months*c_d)) + final_balance * (
                        1 + annual_rate / c_d) ** -(months*c_d)) / (annual_rate / c_d)
            result = f"Calculated Principal: {principal:.2f}"
        elif annual_rate is None:
            result= f"Calculated Annual Interest Rate: I found that you are an idoit, it could not be none"
        elif months is None:
            months = -math.log(1 - principal * (annual_rate / c_d) / monthly_payment) / math.log(1 + annual_rate / c_d)
            months = months/c_d
            result = f"Calculated Duration: {months:.0f} months"
        elif monthly_payment is None:
            monthly_payment = (principal * (annual_rate / c_d) - final_balance * (annual_rate / c_d) * (
                        1 + annual_rate / c_d) ** -(months*c_d)) / (1 - (1 + annual_rate / c_d) ** -(months*c_d))
            result = f"Calculated Monthly Payment: {monthly_payment:.2f}"
        elif final_balance is None:
            final_balance = principal * (1 + annual_rate / c_d) ** (months*c_d) - monthly_payment * (
                        (1 + annual_rate / c_d) ** (months*c_d) - 1) / (annual_rate / c_d)
            result = f"Calculated Final Balance: {final_balance:.2f}"
        else:
            result = "All values are provided. No calculation needed."

        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def calculate_savings():
    try:
        timescal()
        principal = entry_principal.get()
        rate = entry_annual_rate.get()
        duration = entry_months.get()
        future_value = entry_monthly_payment.get()

        if principal.lower() != 'none':
            principal = float(principal)
        else:
            principal = None

        if rate.lower() != 'none':
            rate = float(rate) / 100
        else:
            rate = None

        if duration.lower() != 'none':
            duration = float(duration)
        else:
            duration = None

        if future_value.lower() != 'none':
            future_value = float(future_value)
        else:
            future_value = None

        if principal is None:
            principal = future_value / ((1 + rate/c_d) ** duration*c_d)
            result = f"Calculated Principal: {principal:.2f}"
        elif rate is None:
            rate = (future_value / principal) / (duration)
            result = f"Calculated Annual Interest Rate: {rate * 100:.2f}%"
        elif duration is None:
            duration = math.log(future_value / principal) / math.log(1 + rate/c_d)
            duration = duration/c_d
            result = f"Calculated Duration: {duration:.2f} years"
        elif future_value is None:
            future_value = principal * ((1 + rate/c_d) ** duration/c_d)
            result = f"Calculated Future Value: {future_value:.2f}"
        else:
            result = "All values are provided. No calculation needed."

        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def calculate_arithmetic_sequence():
    try:
        first_term = entry_first_term.get()
        common_difference = entry_common_difference.get()
        n = entry_n.get()
        sum_n_terms = entry_sum_n_terms.get()
        nth_term = entry_nth_term.get()

        if first_term.lower() != 'none':
            first_term = float(first_term)
        else:
            first_term = None

        if common_difference.lower() != 'none':
            common_difference = float(common_difference)
        else:
            common_difference = None

        if n.lower() != 'none':
            n = int(n)
        else:
            n = None

        if sum_n_terms.lower() != 'none':
            sum_n_terms = float(sum_n_terms)
        else:
            sum_n_terms = None

        if nth_term.lower() != 'none':
            nth_term = float(nth_term)
        else:
            nth_term = None

        if first_term is None:
            first_term = nth_term - (n - 1) * common_difference
            result = f"Calculated First Term (a1): {first_term:.2f}"
        elif common_difference is None:
            common_difference = (nth_term - first_term) / (n - 1)
            result = f"Calculated Common Difference (d): {common_difference:.2f}"
        elif n is None:
            n = ((nth_term - first_term) / common_difference) + 1
            result = f"Calculated Number of Terms (n): {n:.0f}"
        elif nth_term is None:
            nth_term = first_term + (n - 1) * common_difference
            result = f"Calculated n-th Term: {nth_term:.2f}"
        elif sum_n_terms is None:
            sum_n_terms = (n / 2) * (2 * first_term + (n - 1) * common_difference)
            result = f"Calculated Sum of the first {n} terms (S_n): {sum_n_terms:.2f}"
        else:
            result = "All values are provided. No calculation needed."

        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def calculate_geometric_series():
    try:
        first_term = entry_first_term.get()
        common_ratio = entry_common_ratio.get()
        n = entry_n.get()
        sum_n_terms = entry_sum_n_terms.get()
        nth_term = entry_nth_term.get()

        if first_term.lower() != 'none':
            first_term = float(first_term)
        else:
            first_term = None

        if common_ratio.lower() != 'none':
            common_ratio = float(common_ratio)
        else:
            common_ratio = None

        if n.lower() != 'none':
            n = int(n)
        else:
            n = None

        if sum_n_terms.lower() != 'none':
            sum_n_terms = float(sum_n_terms)
        else:
            sum_n_terms = None

        if nth_term.lower() != 'none':
            nth_term = float(nth_term)
        else:
            nth_term = None

        if first_term is None:
            first_term = nth_term / (common_ratio ** (n - 1))
            result = f"Calculated First Term (a1): {first_term:.2f}"
        elif common_ratio is None:
            common_ratio = (nth_term / first_term) ** (1 / (n - 1))
            result = f"Calculated Common Ratio (r): {common_ratio:.2f}"
        elif n is None:
            n = math.log(nth_term / first_term) / math.log(common_ratio) + 1
            result = f"Calculated Number of Terms (n): {n:.0f}"
        elif nth_term is None:
            nth_term = first_term * (common_ratio ** (n - 1))
            result = f"Calculated n-th Term: {nth_term:.2f}"
        elif sum_n_terms is None:
            if common_ratio == 1:
                sum_n_terms = first_term * n
            else:
                sum_n_terms = first_term * (1 - common_ratio ** n) / (1 - common_ratio)
            result = f"Calculated Sum of the first {n} terms (S_n): {sum_n_terms:.2f}"
        else:
            result = "All values are provided. No calculation needed."

        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
def calcircle():
    try:
        r = entry_radius.get()
        a = entry_angle.get()
        r=float(r)
        if a == "0" or a == "360":
            a = 360
        else:
            a = abs(float(a))
        len = r*2*3.14
        lena = len*a/360
        are = r*r*3.14
        area = are*a/360
        result = f"Calculated Length: {len}, Calculated length for angle: {lena}, Calcuated area: {are}, Calculated area for angle: {area}"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "David ate your brain!")
def suvatcal():
    s = entry_s.get()
    u = entry_u.get()
    v = entry_v.get()
    a = entry_a.get()
    t = entry_t.get()

    if s != 'none':
        s = float(s)
    else:
        s = None
    if u != 'none':
        u = float(u)
    else:
        u = None
    if v != 'none':
        v = float(v)
    else:
        v = None
    if a != 'none':
        a = float(a)
    else:
        a = None
    if t != 'none':
        t = float(t)
    else:
        t = None

def david():
    messagebox.showinfo("DavidDavidDavid", "WoWoWaWa,you found this?! Why and How?")
def calculator():
    mode = mode_var.get()
    if mode == "loan":
        calculate_missing_value()
    elif mode == "saving":
        calculate_savings()
    elif mode == "arithmetic":
        calculate_arithmetic_sequence()
    elif mode == "geometric":
        calculate_geometric_series()
    elif mode =="david":
        david()
    elif mode == "suvat":
        suvatcal()
    elif mode == "circle":
        calcircle()
    else:
        messagebox.showerror("Input Error", "Please select a valid mode.")

def timescal():
    global c_d
    compound_cycle=compound_c.get()
    if compound_cycle == 'Yearly':
        c_d=1
    elif compound_cycle == 'Monthly':
        c_d=12
    elif compound_cycle == 'Quarterly':
        c_d=4
    else:
        c_d == int(compound_cycle)

def update_fields(*args):
    global entry_first_term
    global entry_common_difference
    global entry_n
    global entry_sum_n_terms
    global entry_nth_term
    global entry_common_ratio
    global entry_principal
    global entry_annual_rate
    global entry_months
    global entry_monthly_payment
    global entry_remaining_balance
    global times_per_y
    mode = mode_var.get()
    for widget in input_frame.winfo_children():
        widget.destroy()
    if mode == 'loan':
        tk.Label(input_frame, text="Principal:").grid(row=0, column=0)
        entry_principal = tk.Entry(input_frame)
        entry_principal.grid(row=0, column=1)
        if mode == 'loan':
            tk.Label(input_frame, text="not non").grid(row=1,column=3)

        tk.Label(input_frame, text="Annual Interest Rate (%):").grid(row=1, column=0)
        entry_annual_rate = tk.Entry(input_frame)
        entry_annual_rate.grid(row=1, column=1)

        tk.Label(input_frame, text="Duration (Years):").grid(row=2, column=0)
        entry_months = tk.Entry(input_frame)
        entry_months.grid(row=2, column=1)

        tk.Label(input_frame, text="Monthly Payment:").grid(row=3, column=0)
        entry_monthly_payment = tk.Entry(input_frame)
        entry_monthly_payment.grid(row=3, column=1)

        tk.Label(input_frame, text="Remaining Balance:").grid(row=4,column=0)
        entry_remaining_balance = tk.Entry(input_frame)
        entry_remaining_balance.grid(row=4, column=1)

        tk.Label(app, text="Compound Duration:").grid(row=1, column=2)
        times_per_y = ttk.Combobox(app, textvariable=compound_c)
        times_per_y['values'] = ("Yearly", "Monthly", "Quarterly")
        times_per_y.grid(row=1, column=3)
    elif mode == "saving":
        tk.Label(input_frame, text="Principal:").grid(row=0, column=0)
        entry_principal = tk.Entry(input_frame)
        entry_principal.grid(row=0, column=1)

        tk.Label(input_frame, text="Annual Interest Rate (%):").grid(row=1, column=0)
        entry_annual_rate = tk.Entry(input_frame)
        entry_annual_rate.grid(row=1, column=1)

        tk.Label(input_frame, text="Duration (Years):").grid(row=2, column=0)
        entry_months = tk.Entry(input_frame)
        entry_months.grid(row=2, column=1)

        tk.Label(input_frame, text="Result").grid(row=3, column=0)
        entry_monthly_payment = tk.Entry(input_frame)
        entry_monthly_payment.grid(row=3, column=1)

        tk.Label(app, text="Compound Duration:").grid(row=1, column=2)
        times_per_y = ttk.Combobox(app, textvariable=compound_c)
        times_per_y['values'] = ("Yearly", "Monthly", "Quarterly")
        times_per_y.grid(row=1, column=3)

    elif mode == "arithmetic":
        tk.Label(input_frame, text="First Term (a1):").grid(row=0, column=0)
        entry_first_term = tk.Entry(input_frame)
        entry_first_term.grid(row=0, column=1)

        tk.Label(input_frame, text="Common Difference (d):").grid(row=1, column=0)

        entry_common_difference = tk.Entry(input_frame)
        entry_common_difference.grid(row=1, column=1)

        tk.Label(input_frame, text="Number of Terms (n):").grid(row=2, column=0)

        entry_n = tk.Entry(input_frame)
        entry_n.grid(row=2, column=1)

        tk.Label(input_frame, text="Sum of the first n terms (S_n):").grid(row=3, column=0)

        entry_sum_n_terms = tk.Entry(input_frame)
        entry_sum_n_terms.grid(row=3, column=1)

        tk.Label(input_frame, text="n-th Term:").grid(row=4, column=0)

        entry_nth_term = tk.Entry(input_frame)
        entry_nth_term.grid(row=4, column=1)
    elif mode == "geometric":
        tk.Label(input_frame, text="First Term (a1):").grid(row=0, column=0)
        entry_first_term = tk.Entry(input_frame)
        entry_first_term.grid(row=0, column=1)

        tk.Label(input_frame, text="Common Ratio (r):").grid(row=1, column=0)
        entry_common_ratio = tk.Entry(input_frame)
        entry_common_ratio.grid(row=1, column=1)

        tk.Label(input_frame, text="Number of Terms (n):").grid(row=2, column=0)
        entry_n = tk.Entry(input_frame)
        entry_n.grid(row=2, column=1)

        tk.Label(input_frame, text="Sum of the first n terms (S_n):").grid(row=3, column=0)
        entry_sum_n_terms = tk.Entry(input_frame)
        entry_sum_n_terms.grid(row=3, column=1)

        tk.Label(input_frame, text="n-th Term:").grid(row=4, column=0)
        entry_nth_term = tk.Entry(input_frame)
        entry_nth_term.grid(row=4, column=1)
    elif mode == "suvat":
        tk.Label(input_frame, text="S(Distance):").grid(row=1,column=0)
        global entry_s
        entry_s = tk.Entry(input_frame)
        entry_s.grid(row=1,column=1)

        tk.Label(input_frame, text="U(Original Speed):").grid(row=2,column=0)
        global entry_u
        entry_u = tk.Entry(input_frame)
        entry_u.grid(row=2,column=1)

        tk.Label(input_frame,text="V(final Speed):").grid(row=3,column=0)
        global entry_v
        entry_v = tk.Entry(input_frame)
        entry_v.grid(row=3,column=1)

        tk.Label(input_frame,text="A(acceleration):").grid(row=4,column=0)
        global entry_a
        entry_a = tk.Entry(input_frame)
        entry_a.grid(row=4,column=1)

        tk.Label(input_frame,text="T(time):").grid(row=5,column=0)
        global entry_t
        entry_t = tk.Entry(input_frame)
        entry_t.grid(row=5,column=1)
    elif mode == "nSolve":
        tk.Label(input_frame, text="I don't know what to do").grid(row=1,column=0)
    elif mode == "circle":
        tk.Label(input_frame,text="Radius of circle:").grid(row=1,column=0)
        global entry_radius
        entry_radius = tk.Entry(input_frame)
        entry_radius.grid(row=1,column=1)

        tk.Label(input_frame,text="Angle of sector:").grid(row=2,column=0)
        global entry_angle
        entry_angle = tk.Entry(input_frame)
        entry_angle.grid(row=2,column=1)



app = tk.Tk()
app.title("The Ultimate IB Math/Physics Calculator by Silcon Finta")

compound_c = tk.StringVar()
mode_var = tk.StringVar()
mode_var.trace("w", update_fields)

tk.Label(app, text="Select Mode:").grid(row=0, column=0)
tk.Label(app, text="use 'none' to represent the value to be find").grid(row=0,column=2)
mode_menu = ttk.Combobox(app, textvariable=mode_var)
mode_menu['values'] = ("loan", "saving", "arithmetic", "geometric","suvat","nSolve","circle")
mode_menu.grid(row=0, column=1)

input_frame = tk.Frame(app)
input_frame.grid(row=1, column=0, columnspan=2)

tk.Button(app, text="Calculate", command=calculator).grid(row=2, column=0, columnspan=2)

label_result = tk.Label(app, text="")
label_result.grid(row=3, column=0, columnspan=2)

app.mainloop()

import tkinter

window = tkinter.Tk()
window.title("BMI Calculator by Tatar")
window.minsize(350,350)
window.config(padx=50,pady=50)


weightLabel= tkinter.Label(text="Enter your weight (kg)", font=3)
weightLabel.pack(padx=6,pady=6)

weight = None
weightEntry = tkinter.Entry()
weightEntry.pack(padx=6,pady=6)


heightLabel= tkinter.Label(text="Enter your height (cm)", font=3)
heightLabel.pack(padx=6,pady=6)


height = None
heightEntry = tkinter.Entry()
heightEntry.pack(padx=10,pady=10)
bmi=0
status = None
printLabel = tkinter.Label(text="", font=3)
printLabel.pack(padx=6, pady=6)
def commitfunction():
    weight = weightEntry.get()
    height = heightEntry.get()
    try:
        bmi = float(weight) / ((float(height)/100)**2)
        bmi = round(bmi,2)
        if bmi <18.5:
            status = "underweight"
        elif 18.5 <= bmi <24.9:
            status = "normal"
        elif 25 <= bmi <29.9:
            status = "overweight"
        elif 30 <= bmi <34.9:
            status = "obese"
        elif 35 <= bmi <39.9:
            status = "severely obese"
        elif bmi>40:
            status="morbidly obese"
        printLabel.config(text=f"Your BMI is {bmi}. You are {status}.")
    except:
        if weight == "" or height == "":
            printLabel.config(text=f"Enter both weight and height!.")
        else:
            printLabel.config(text=f"Enter a valid number!")



commitButton = tkinter.Button(text="Calculate", command = commitfunction)
commitButton.pack()


window.mainloop()
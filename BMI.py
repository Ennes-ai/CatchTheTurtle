import tkinter as tk

window = tk.Tk()
window.title("BMI Calculator!")
window.minsize(width=600,height=400)
window.configure(bg="light blue")

MyHeightLabel = tk.Label(border=5,text="Enter your height :",font=("Arial",15,"bold"),bg="light blue")
MyHeightLabel.grid(row=1,column=0,padx=5,pady=10)

MyHeightEntry = tk.Entry(width=20,border=5)
MyHeightEntry.grid(row=1,column=1)

MyWeightLabel = tk.Label(border=5,text="Enter Your Weight :",font=("arial",15,"bold"),bg="light blue")
MyWeightLabel.grid(row=2,column=0,padx=5,pady=10)

MyWeightEntry = tk.Entry(width=20,border=5)
MyWeightEntry.grid(row=2,column=1)


MyLastLabel = tk.Label(text="",bg="light blue",font=("arial",15,"bold"))
MyLastLabel.grid(row=4,column=0)

def ButonClicked():
    HeightEntry = MyHeightEntry.get()
    WeightEntry = MyWeightEntry.get()
    try:
        if  int(HeightEntry and WeightEntry):

            HeightEntry = float(HeightEntry)
            WeightEntry = float(WeightEntry)

            HeightEntry = HeightEntry/100
            calculated = WeightEntry/(HeightEntry**2)

            if calculated < 18.5:
                MyLastLabel.config(text="You are so weak that it might be dangerous.")
            elif 18.5 <= calculated < 25:
                 MyLastLabel.config(text="You are normal thats good for you.")
            elif 25 <= calculated < 35:
                MyLastLabel.config(text="You are a first-degree obese person; that is not good.")
            elif 35 <= calculated < 40:
                MyLastLabel.config(text="You are a second-degree obese person; that is not good.")
            elif 40 <= calculated:
                MyLastLabel.config(text="You are a third-degree obese person; that is not good.")

    except:
        MyLastLabel.config(text="Invalid height and weight input!")

MyButton = tk.Button(text="Calculate",width=15,height=1,command=ButonClicked,font=("arial",10,"bold"))
MyButton.grid(row=3,column=1)

window.mainloop()
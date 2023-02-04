import flet as ft
import math as m
def main(page:ft.Page):
    page.title="SCIENTIFIC CALCULATOR"
    calc = Calculator()
    page.add(calc)

class Calculator(ft.UserControl):
    def build(self):
        self.reset()
        self.result = ft.Text(value = "0", color = ft.colors.WHITE, size = 20)
        return ft.Container(
            width=420,
            bgcolor= ft.colors.BLACK,
            border_radius = ft.border_radius.all(20),
            padding=20,
            content= ft.Column(
                controls=[
                    ft.Row(controls = [self.result],alignment="end"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="sin",bgcolor=ft.colors.AMBER,color=ft.colors.WHITE, on_click=self.button_clicked,data ="sin"),
                            ft.ElevatedButton(text="cos",bgcolor=ft.colors.AMBER,color=ft.colors.WHITE, on_click=self.button_clicked,data ="cos"),
                            ft.ElevatedButton(text="tan",bgcolor=ft.colors.AMBER,color=ft.colors.WHITE, on_click=self.button_clicked,data ="tan"),
                            ft.RadioGroup(content = ft.Column([
                                ft.Radio(value = "DEG", label = "Deg",data="deg"),
                                ft.Radio(value = "RAD", label = "RAD", data = "rad"),
                            ])),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="sin-1",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="sin1"),
                            ft.ElevatedButton(text="cos-1",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="cos1"),
                            ft.ElevatedButton(text="tan-1",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="tan1"),
                            ft.ElevatedButton(text="⫪",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="pie"),
                            ft.ElevatedButton(text="e",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="e"),            
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="xy",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="xy"),
                            ft.ElevatedButton(text="x3",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="x3"),
                            ft.ElevatedButton(text="x2",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="x2"),
                            ft.ElevatedButton(text="ex",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="ex"),
                            ft.ElevatedButton(text="10x",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="10x"),     
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="y√x",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="y_root_x"),
                            ft.ElevatedButton(text="3√x",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="three_root_x"),
                            ft.ElevatedButton(text="√x",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="root_x"),
                            ft.ElevatedButton(text="ln",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="ln"),
                            ft.ElevatedButton(text="log",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="log"),
                            
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="(",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="("),
                            ft.ElevatedButton(text=")",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data=")"),
                            ft.ElevatedButton(text="1/x",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="1/x"),
                            ft.ElevatedButton(text="%",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="%"),
                            ft.ElevatedButton(text="n!",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="n!"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="7",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="7"),
                            ft.ElevatedButton(text="8",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="8"),
                            ft.ElevatedButton(text="9",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="9"),
                            ft.ElevatedButton(text="+",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="+"),
                            ft.ElevatedButton(text="Back",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="back"),
                        ]
                    ),
                    ft.Row(
                        controls=[ 
                            ft.ElevatedButton(text="4",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="4"),
                            ft.ElevatedButton(text="5",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="5"),
                            ft.ElevatedButton(text="6",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="6"),
                            ft.ElevatedButton(text="-",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="-"),
                            ft.ElevatedButton(text="Ans",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="ans"),
                        ]
                    ),   
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="1",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="1"),
                            ft.ElevatedButton(text="2",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="2"),
                            ft.ElevatedButton(text="3",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="3"),
                            ft.ElevatedButton(text="*",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="*"),
                            ft.ElevatedButton(text="M+",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="m+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="0",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="0"),
                            ft.ElevatedButton(text=".",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="."),
                            ft.ElevatedButton(text="EXP",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="exp"),
                            ft.ElevatedButton(text="/",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="/"),
                            ft.ElevatedButton(text="M-",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="m-"),            
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="±",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="+-"),
                            ft.ElevatedButton(text="RND",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="rnd"),
                            ft.ElevatedButton(text="AC",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="AC"),
                            ft.ElevatedButton(text="=",bgcolor=ft.colors.WHITE24,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="equal"),
                            ft.ElevatedButton(text="MR",bgcolor=ft.colors.CYAN,color=ft.colors.WHITE,expand=1,on_click=self.button_clicked,data="mr"),
                        ]
                    )
                ],
            ),
        )
    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("xy","y_root_x"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value),self.operator
            )
        elif data in ("sin", "cos", "tan" ,"sin1","cos1","tan1"):
            if data =="sin":
                self.result.value = m.sin(self.result.value)
            elif data =="cos":
                self.result.value = m.cos(self.result.value)
            elif data == "tan" :
                self.result.value = m.tan(self.result.value)
            elif data =="sin1":
                self.result.value = m.asin(self.result.value)
            elif data =="cos1":
                self.result.value = m.acos(self.result.value)
            elif data =="tan1":
                self.result.value = m.atan(self.result.value)
                
        elif data in ("pie"):
             self.result.value = float(self.result.value) * 3.14

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        elif data =="e":
            self.result.value = (m.e) * self.result.value

        elif data == "root_x":
            self.result.value =  m.sqrt(float(self.result.value))

        elif data == "log":
            self.result.value =  m.log10(float(self.result.value))

        elif data == "n!":
             self.result.value = m.factorial(int(self.result.value))

        elif data == "ln":
            self.result.value =  m.log(float(self.result.value))
        
        elif data =="rad":
           self.result.value =  m.radians(float(self.result.value))
        elif data == "deg":
            self.result.value = m.degrees(float(self.result.value))
        
        elif data == "1/x":
            if(self.result.value == "0"):
                return 0
            else:
                return (1/float(self.result.value))

        elif data =="ex":
            self.result.value = (m.e) ** self.result.value

        elif data =="x3":
            self.result.value = self.result.value * self.result.value * self.result.value

        elif data =="x2":
            self.result.value = self.result.value ** self.result.value

        elif data =="three_root_x":
            if self.result.value < 0:
                self.result.value = m.abs(self.result.value)
                self.result.value = self.result.value ** (1/3) * (-1) 
            else:
                   self.result.value = self.result.value ** (1/3)
        elif data =="10x":
            self.result.value = 10 ** self.result.value
        
        self.update()



    def format_number(self,num):
        if num % 1 ==0:
            return int(num)
        else:
            return num
    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)
        elif operator =="xy":
            return operand1 ** operand2

        elif operator == "y_root_x":
            return operand2 ** (1/operand1)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True



ft.app(target=main)
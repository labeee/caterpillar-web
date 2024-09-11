import customtkinter as ctk
from turtle import RawTurtle, Canvas, TurtleScreen
import math
from pkg_resources import resource_filename
my_icon = resource_filename(__name__, 'icon_default.ico')

title_font = ('calibri', 35)
text_font = ('calibri', 25)
credit_font = ('calibri', 15)
help_font = ('calibri', 15)
elements_font = ('calibri', 10)
general_pady = 10
entry_width = 250
txt_color = '#C5F9C7'
txt_color_alt = 'black'
front = '#FF00E6'
back = '#00FFE0'
ground = '#FF0000'
roof = '#00FF0A'
wall = '#FAFF00'
foreground = '#2B2B2B'
background = 'black'
entry_bg = background
iniciar_button = txt_color
desenhar_color = '#FF4DD8'
calcular_color = '#00FF0A'


class Caterpillar:
    def __init__(self, jan):
        self.jan = jan
        self.jan.iconbitmap(my_icon)
        open_room_size = 120
        open_room_pos_init = (-50, -210)

        def start_program():
            iniciar_app.destroy()
            drawn_open()
            make_house(largura=300, altura=120, comprimento=200, x=150, y=100, z=60)
            mainscreen()

        def mainscreen():

            c_ambiente = ctk.CTkFrame(frame, fg_color='transparent')
            c_ambiente.pack()

            ambiente_titulo = ctk.CTkLabel(c_ambiente, text='Medidas do Ambiente', font=text_font, text_color=txt_color)
            ambiente_titulo.pack(pady=general_pady)

            largura_ambiente = ctk.CTkEntry(c_ambiente, placeholder_text='Largura (m)', font=credit_font, width=250, text_color=txt_color, fg_color=entry_bg)
            largura_ambiente.pack(pady=general_pady)
            comprimento_ambiente = ctk.CTkEntry(c_ambiente, placeholder_text='Comprimento (m)', font=credit_font, width=250, text_color=txt_color, fg_color=entry_bg)
            comprimento_ambiente.pack(pady=general_pady)
            altura_ambiente = ctk.CTkEntry(c_ambiente, placeholder_text='Altura (m)', font=credit_font, width=250, text_color=txt_color, fg_color=entry_bg)
            altura_ambiente.pack(pady=general_pady)

            c_posicao = ctk.CTkFrame(frame, fg_color='transparent')
            c_posicao.pack()

            posicao_titulo = ctk.CTkLabel(c_posicao, text='Posição do Plano', font=text_font, text_color=txt_color)
            posicao_titulo.pack(pady=general_pady)

            x_coord = ctk.CTkEntry(c_posicao, placeholder_text='X (m)', font=credit_font, width=250, text_color=txt_color, fg_color=entry_bg)
            x_coord.pack(pady=general_pady)
            y_coord = ctk.CTkEntry(c_posicao, placeholder_text='Y (m)', font=credit_font, width=250, text_color=txt_color, fg_color=entry_bg)
            y_coord.pack(pady=general_pady)
            z_coord = ctk.CTkEntry(c_posicao, placeholder_text='Z (m)', font=credit_font, width=250, text_color=txt_color, fg_color=entry_bg)
            z_coord.pack(pady=general_pady)

            def verify_room():
                largura_num = largura_ambiente.get().replace(',', '.')
                altura_num = altura_ambiente.get().replace(',', '.')
                comprimento_num = comprimento_ambiente.get().replace(',', '.')
                x_num = x_coord.get().replace(',', '.')
                y_num = y_coord.get().replace(',', '.')
                z_num  = z_coord.get().replace(',', '.')
                try:
                    try_float = [float(item) for item in [largura_num, altura_num, comprimento_num, x_num, y_num, z_num]]
                    verificacao = True
                except:
                    verificacao = False
                if verificacao:
                    turtle.clear()
                    drawn_open()
                    make_house(largura=float(largura_num)*100, altura=float(altura_num)*100, comprimento=float(comprimento_num)*100, x=float(x_num)*100, y=float(y_num)*100, z=float(z_num)*100)
                else:
                    turtle.clear()
                    turtle.up()
                    turtle.home()
                    turtle.color('red')
                    turtle.write('\tATENÇÃO\nInsira todas as medidas\ndo ambiente e coordenadas\nadequadamente para desenhar', False, 'center', text_font)

            desenhar = ctk.CTkButton(frame, text='Desenhar', font=text_font, text_color=txt_color_alt, fg_color=desenhar_color, command=verify_room)
            desenhar.pack(pady=general_pady, padx=30)

            c_temp = ctk.CTkFrame(frame, fg_color='transparent')
            c_temp.pack()

            temp_titulo = ctk.CTkLabel(c_temp, text='Temperaturas', font=text_font, text_color=txt_color)
            temp_titulo.grid(row=0, column=0, columnspan=2,pady=general_pady)

            temp_frontal = ctk.CTkEntry(c_temp, placeholder_text='Frontal (°C)', font=credit_font, width=160, text_color=txt_color, fg_color=entry_bg)
            temp_frontal.grid(row=1, column=0, pady=general_pady, padx=general_pady)
            temp_lat_esq = ctk.CTkEntry(c_temp, placeholder_text='Lateral Esquerda (°C)', font=credit_font, width=160, text_color=txt_color, fg_color=entry_bg)
            temp_lat_esq.grid(row=2, column=0, pady=general_pady, padx=general_pady)
            temp_piso = ctk.CTkEntry(c_temp, placeholder_text='Piso (°C)', font=credit_font, width=160, text_color=txt_color, fg_color=entry_bg)
            temp_piso.grid(row=3, column=0, pady=general_pady, padx=general_pady)
            temp_posterior = ctk.CTkEntry(c_temp, placeholder_text='Posterior (°C)', font=credit_font, width=160, text_color=txt_color, fg_color=entry_bg)
            temp_posterior.grid(row=1, column=1, pady=general_pady, padx=general_pady)
            temp_lat_dir = ctk.CTkEntry(c_temp, placeholder_text='Lateral Direita (°C)', font=credit_font, width=160, text_color=txt_color, fg_color=entry_bg)
            temp_lat_dir.grid(row=2, column=1, pady=general_pady, padx=general_pady)
            temp_teto = ctk.CTkEntry(c_temp, placeholder_text='Teto (°C)', font=credit_font, width=160, text_color=txt_color, fg_color=entry_bg)
            temp_teto.grid(row=3, column=1, pady=general_pady, padx=general_pady)

            def calculate():
                largura_num = largura_ambiente.get().replace(',', '.')
                altura_num = altura_ambiente.get().replace(',', '.')
                comprimento_num = comprimento_ambiente.get().replace(',', '.')
                x_num = x_coord.get().replace(',', '.')
                y_num = y_coord.get().replace(',', '.')
                z_num  = z_coord.get().replace(',', '.')
                temp_frontal_num = temp_frontal.get().replace(',', '.')
                temp_lat_esq_num = temp_lat_esq.get().replace(',', '.')
                temp_piso_num = temp_piso.get().replace(',', '.')
                temp_posterior_num = temp_posterior.get().replace(',', '.')
                temp_lat_dir_num = temp_lat_dir.get().replace(',', '.')
                temp_teto_num = temp_teto.get().replace(',', '.')
                if '0' in [largura_num, altura_num, comprimento_num, x_num, y_num, z_num, temp_frontal_num, temp_lat_esq_num, temp_piso_num, temp_posterior_num, temp_lat_dir_num, temp_teto_num]:
                    turtle.clear()
                    turtle.up()
                    turtle.home()
                    turtle.color('red')
                    turtle.write('\tERRO\nZero não pode ser uma das medidas', False, 'center', text_font)
                else:
                    try:
                        try_float = [float(item) for item in [largura_num, altura_num, comprimento_num, x_num, y_num, z_num, temp_frontal_num, temp_lat_esq_num, temp_piso_num, temp_posterior_num, temp_lat_dir_num, temp_teto_num]]
                        verificacao = True
                    except:
                        verificacao = False
                    if verificacao:
                        self.open_calculate_window(largura=float(largura_num), altura=float(altura_num), comprimento=float(comprimento_num), x=float(x_num), y=float(y_num), z=float(z_num), temp_frontal=float(temp_frontal_num), temp_lat_esq=float(temp_lat_esq_num), temp_piso=float(temp_piso_num), temp_posterior=float(temp_posterior_num), temp_lat_dir=float(temp_lat_dir_num), temp_teto=float(temp_teto_num))
                    else:
                        turtle.clear()
                        turtle.up()
                        turtle.home()
                        turtle.color('red')
                        turtle.write('\tATENÇÃO\nInsira todas as medidas\ndo ambiente, coordenadas e temperaturas\nadequadamente para desenhar', False, 'center', text_font)

            calcular = ctk.CTkButton(frame, text='Calcular', font=text_font, text_color=txt_color_alt, fg_color=calcular_color, command=calculate)
            calcular.pack(pady=general_pady, padx=30)

        def rectangle(x, y):
            turtle.setheading(0)
            for _ in range(2):
                turtle.forward(x)
                turtle.left(90)
                turtle.forward(y)
                turtle.left(90)

        def paralelepipedo(x, y):
            turtle.setheading(0)
            turtle.color(ground)
            turtle.left(45)
            turtle.forward(x)
            turtle.left(45)
            turtle.color(back)
            turtle.forward(y)
            turtle.setheading(225)
            turtle.color(roof)
            turtle.forward(x)
            turtle.setheading(270)
            turtle.color(front)
            turtle.forward(y)

        def make_house(largura:float, altura:float, comprimento:float, x:float, y:float, z:float):
            cube_size = 20
            size_of_pen = 3
            if (largura >= 400) or (altura >= 400) or (comprimento >= 400):
                if (largura >= 1000) or (altura >= 1000) or (comprimento >= 1000):
                    size_of_pen = 2
                greater = max([largura, altura, comprimento])
                largura = largura/(2*(greater/400))
                comprimento = comprimento/(2*(greater/400))
                altura = altura/(2*(greater/400))
                x = x/(2*(greater/400))
                y = y/(2*(greater/400))
                z = z/(2*(greater/400))
                cube_size = cube_size/(2*(greater/400))
            if (largura <= 100) or (altura <= 100) or (comprimento <= 100):
                largura = largura*1.5
                comprimento = comprimento*1.5
                altura = altura*1.5
                x = x*1.5
                y = y*1.5
                z = z*1.5
                cube_size = cube_size*1.5
            turtle.pensize(size_of_pen)

            turtle.up()
            if largura <= 200:
                if comprimento <= 200:
                    turtle.setx(-largura/2)
                else:
                    turtle.setx(-comprimento/1.6)
            elif comprimento <= 200:
                turtle.setx(-largura/1.6)
            else:
                turtle.setx(-(largura+comprimento)/2)
            if comprimento >= 200:
                if altura >= 300:
                    turtle.sety(-altura/3)
            turtle.down()

            initial = turtle.pos()

            turtle.up()
            turtle.setpos(initial)
            turtle.down()
            turtle.color(ground)
            turtle.setheading(45)
            turtle.forward(comprimento)
            turtle.setheading(0)
            turtle.forward(largura)
            turtle.setheading(225)
            turtle.forward(comprimento)
            turtle.setheading(180)
            turtle.forward(largura)
            
            paralelepipedo(comprimento, altura)

            turtle.setheading(45)
            turtle.up()
            turtle.forward(comprimento)
            turtle.color(back)
            turtle.down()
            rectangle(largura, altura)

            turtle.up()
            turtle.setpos(initial)
            turtle.setheading(0)
            turtle.forward(x)
            turtle.setheading(45)
            turtle.forward(y)
            turtle.setheading(90)
            turtle.forward(z)
            ambiente_center = turtle.pos()
            turtle.color('white')
            turtle.setheading(270)
            turtle.forward(cube_size/2)
            turtle.setheading(180)
            turtle.forward(cube_size/2)
            turtle.setheading(225)
            turtle.forward(cube_size/2)
            turtle.down()
            rectangle(cube_size, cube_size)
            turtle.setheading(45)
            turtle.forward(cube_size)
            rectangle(cube_size, cube_size)
            turtle.setheading(90)
            turtle.forward(cube_size)
            turtle.setheading(225)
            turtle.forward(cube_size)
            turtle.back(cube_size)
            turtle.setheading(0)
            turtle.forward(cube_size)
            turtle.setheading(225)
            turtle.forward(cube_size)
            turtle.setheading(270)
            turtle.forward(cube_size)
            turtle.setheading(45)
            turtle.forward(cube_size)
            turtle.up()
            turtle.setpos(ambiente_center)
            turtle.pensize(size_of_pen/3)
            turtle.down()
            turtle.setheading(225)
            turtle.forward(y)
            turtle.stamp()
            turtle.back(comprimento)
            turtle.up()
            turtle.setpos(ambiente_center)
            turtle.down()
            turtle.setheading(180)
            turtle.forward(x)
            turtle.back(largura)
            turtle.up()
            turtle.setpos(ambiente_center)
            turtle.down()
            turtle.setheading(270)
            turtle.forward(z)
            turtle.back(altura)
            turtle.pensize(size_of_pen)

            turtle.up()
            turtle.setpos(initial)
            turtle.setheading(0)
            turtle.forward(largura)
            turtle.down()
            paralelepipedo(comprimento, altura)

            turtle.up()
            turtle.setpos(initial)
            turtle.down()
            turtle.color(front)
            rectangle(largura, altura)

            turtle.pensize(2)

        def drawn_open():
            turtle.up()
            turtle.setpos(open_room_pos_init)
            turtle.down()
            turtle.color(roof)
            Caterpillar.square(turtle, open_room_size)
            turtle.forward(open_room_size)
            turtle.color(front)
            Caterpillar.square(turtle, open_room_size)
            turtle.forward(open_room_size)
            turtle.left(90)
            turtle.color(wall)
            Caterpillar.square(turtle, open_room_size)
            turtle.setheading(270)
            turtle.up()
            turtle.forward(open_room_size)
            turtle.down()
            turtle.setheading(0)
            Caterpillar.square(turtle, open_room_size)
            turtle.color(ground)
            turtle.forward(open_room_size)
            turtle.back(open_room_size)
            turtle.up()
            turtle.setheading(90)
            turtle.forward(open_room_size)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(open_room_size)
            turtle.color(back)
            Caterpillar.square(turtle, open_room_size)
            turtle.up()
            turtle.setpos(open_room_pos_init)
            turtle.color('white')
            turtle.forward(open_room_size/2)
            turtle.setheading(270)
            turtle.forward(open_room_size/2 + 20)
            turtle.setheading(0)
            turtle.write('Teto', False, 'center', credit_font)
            turtle.forward(open_room_size)
            turtle.write('Parede\nFrontal', False, 'center', credit_font)
            turtle.forward(open_room_size)
            turtle.write('Piso', False, 'center', credit_font)
            turtle.setheading(90)
            turtle.forward(open_room_size)
            turtle.write('Lateral\nDireita', False, 'center', credit_font)
            turtle.back(open_room_size*2)
            turtle.write('Lateral\nEsquerda', False, 'center', credit_font)
            turtle.forward(open_room_size)
            turtle.setheading(0)
            turtle.forward(open_room_size)
            turtle.write('Parede\nPosterior', False, 'center', credit_font)

            turtle.up()
            turtle.home()
            turtle.setx(-400)
            turtle.sety(-320)
            turtle.color('white')
            turtle.down()
            turtle.setheading(0)
            turtle.forward(130)
            turtle.stamp()
            turtle.write('Largura (X)', False, 'center', credit_font)
            turtle.back(130)
            turtle.setheading(90)
            turtle.forward(140)
            turtle.write('Altura (Z)', False, 'center', credit_font)
            turtle.stamp()
            turtle.back(140)
            turtle.setheading(45)
            turtle.forward(130)
            turtle.write('Comprimento (Y)', False, 'center', credit_font)
            turtle.stamp()

            turtle.up()
            turtle.home()
            turtle.down()


        self.jan.title("Caterpillar(CATeRP)")
        self.jan.geometry('1440x960')
        self.jan.configure(fg_color=background)
        window = ctk.CTkFrame(self.jan, fg_color=background)
        window.pack()
        self.toplevel_window = None
        
        label = ctk.CTkLabel(window, text='Caterpillar (CATeRP)', text_color=txt_color, font=title_font)
        label.grid(row=0, column=0, pady=20)

        help_button = ctk.CTkButton(window, text='?', text_color=txt_color_alt, font=title_font, width=25, fg_color=txt_color, corner_radius=90, command=self.open_help)
        help_button.place(x=430,y=17)

        frame = ctk.CTkFrame(window, fg_color=foreground, width=370, height=800)
        frame.grid(row=1, column=0, padx=60)
        frame.pack_propagate(False)
        frame.grid_propagate(False)

        credit = ctk.CTkLabel(window, text='Zac Milioli, LabEEE 2024', text_color=txt_color, font=credit_font)
        credit.grid(row=2, column=0, pady=20)

        canvas = Canvas(window, width=980, height=960, highlightbackground=foreground)
        canvas.grid(row=0, rowspan=3, column=1)
        screen = TurtleScreen(canvas)
        screen.bgcolor(foreground)
        turtle = RawTurtle(screen)
        turtle.hideturtle()
        turtle.speed(0)

        iniciar_app = ctk.CTkButton(frame, text='Iniciar', fg_color=iniciar_button, font=title_font, text_color=txt_color_alt, width=50, height=150, corner_radius=90, command=start_program)
        iniciar_app.pack(pady=300)
    
    def square(turtle, size):
        for _ in range(0,4):
            turtle.forward(size)
            turtle.right(90)
    
    def open_calculate_window(self, largura, altura, comprimento, x, y, z, temp_frontal, temp_lat_esq, temp_piso, temp_posterior, temp_lat_dir, temp_teto):
        calculation_window = ctk.CTkToplevel()
        calculation_window.attributes("-topmost", True)
        calculation_window.title('Resultados - Caterpillar')
        calculation_window.geometry('600x960')
        calculation_window.configure(fg_color=background)

        titulo_results = ctk.CTkLabel(calculation_window, text='Resultados - Caterpillar', font=title_font, text_color=txt_color)
        titulo_results.pack(pady=20)

        topframe = ctk.CTkScrollableFrame(calculation_window, fg_color=foreground, height=850, width=480)
        topframe.pack(padx=60)

        temps = {
        'temp_frontal': temp_frontal,
        'temp_posterior': temp_posterior,
        'temp_teto': temp_teto,
        'temp_piso': temp_piso,
        'temp_lat_direita': temp_lat_dir,
        'temp_lat_esquerda': temp_lat_esq
        }

        for key in temps:
            temps[key] += 273.15

        room = {
            'largura': largura,
            'comprimento': comprimento,
            'altura': altura,
            'pos_x': x,
            'pos_y': y,
            'pos_z': z
        }

        coordinates = {
            'dist_frontal': room['pos_y'],
            'dist_posterior': room['comprimento'] - room['pos_y'],
            'dist_piso': room['pos_z'],
            'dist_teto': room['altura'] - room['pos_z'],
            'dist_lat_direita': room['pos_x'],
            'dist_lat_esquerda': room['largura'] - room['pos_x'],
        }

        def ort_ff(a: float, b: float, c: float) -> float:
            """
            Calculates the orthogonal form factor.

            Args:
                a (float): The perpendicular measurement from c.
                b (float): The rest.
                c (float): The distance from the center of the plain to the reference point.

            Returns:
                form_factor (float): The orthogonal form factor.
            """

            x = a / b
            y = c / b

            form_factor = (1 / (2 * math.pi)) * (math.atan(1 / y) - (y / math.sqrt(x**2 + y**2)) * math.atan(1 / math.sqrt(x**2 + y**2)))
            return round(form_factor, 14)

        def par_ff(a: float, b: float, c: float) -> float:
            """
            Calculates the paralel form factor.

            Args:
                a (float): The perpendicular measurement from c.
                b (float): The rest.
                c (float): The distance from the center of the plain to the reference point.

            Returns:
                form_factor (float): The paralel form factor.
            """
            x = a / c
            y = b / c

            form_factor = (1 / (2 * math.pi)) * ((x / math.sqrt(1 + x**2)) * math.atan(y / math.sqrt(1 + x**2)) + (y / math.sqrt(1 + y**2)) * math.atan(x / math.sqrt(1 + y**2)))
            return round(form_factor, 14)

## CÁLCULO FRONTAL E POSTERIOR
        ort_ff_frontal_dict = {
            'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
            'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
            'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
            'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
            'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
            'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
            'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
        }

        ort_ff_posterior_dict = {
            'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
            'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
            'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
            'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
            'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
            'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
        }

        par_ff_dict = {
            'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
            'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
        }

        conferencia = {
            'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
            'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14)
        }

        ajuste_frontal = 0
        ajuste_posterior = 0

        if conferencia['sum_ff_frontal'] != 1:
            ajuste_frontal = conferencia['sum_ff_frontal']
            ajuste_frontal = 1 - ajuste_frontal
            ajuste_frontal = ajuste_frontal / 4
        
        if conferencia['sum_ff_posterior'] != 1:
            ajuste_posterior = conferencia['sum_ff_posterior']
            ajuste_posterior = 1 - ajuste_posterior
            ajuste_posterior = ajuste_posterior / 4

        result_data = {
            'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
            'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14),
            'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 14),
            'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 14),
            'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 14),
            'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 14),
            'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 14),
            'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 14),
            'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 14),
            'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 14)
        }

        radiant_temperatures = {
            'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 14),
            'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 14)
        }

        radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 14)
        radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 14)
        radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 14)

        resultados_frontal = f"""- - - - - - - - - - - - - - - - - - - - - - - - - -
    FRONTAL E POSTERIOR

    TEMPERATURAS RADIANTES
Frontal: {round(radiant_temperatures['frontal_celsius'], 2)}°C
Posterior: {round(radiant_temperatures['posterior_celsius'], 2)}°C
Assimetria: {round(radiant_temperatures['assimetry'], 2)}°C

    FATORES DE FORMA FRONTAIS
Parede frontal: {result_data['ff_frontal_total']}
Lateral direita: {result_data['ff_frontal_lat_dir_total']}
Lateral esquerda: {result_data['ff_frontal_lat_esq_total']}
Teto: {result_data['ff_frontal_teto_total']}
Piso: {result_data['ff_frontal_piso_total']}

    FATORES DE FORMA POSTERIORES
Parede posterior: {result_data['ff_posterior_total']}
Lateral direita: {result_data['ff_posterior_lat_dir_total']}
Lateral esquerda: {result_data['ff_posterior_lat_esq_total']}
Teto: {result_data['ff_posterior_teto_total']}
Piso: {result_data['ff_posterior_piso_total']}"""

## CÁLCULO ESQUERDA E DIREITA
        temps = {
        'temp_frontal': temp_lat_esq,
        'temp_posterior': temp_lat_dir,
        'temp_teto': temp_teto,
        'temp_piso': temp_piso,
        'temp_lat_direita': temp_frontal,
        'temp_lat_esquerda': temp_posterior
        }

        for key in temps:
            temps[key] += 273.15

        coordinates = {
            'dist_frontal': room['largura'] - room['pos_x'],
            'dist_posterior': room['pos_x'],
            'dist_piso': room['pos_z'],
            'dist_teto': room['altura'] - room['pos_z'],
            'dist_lat_direita': room['pos_y'],
            'dist_lat_esquerda': room['comprimento'] - room['pos_y'],
        }

        ort_ff_frontal_dict = {
            'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
            'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
            'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
            'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
            'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
            'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
            'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
        }

        ort_ff_posterior_dict = {
            'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
            'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
            'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
            'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
            'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
            'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
        }

        par_ff_dict = {
            'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
            'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
        }

        conferencia = {
            'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
            'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14)
        }

        ajuste_frontal = 0
        ajuste_posterior = 0

        if conferencia['sum_ff_frontal'] != 1:
            ajuste_frontal = conferencia['sum_ff_frontal']
            ajuste_frontal = 1 - ajuste_frontal
            ajuste_frontal = ajuste_frontal / 4
        
        if conferencia['sum_ff_posterior'] != 1:
            ajuste_posterior = conferencia['sum_ff_posterior']
            ajuste_posterior = 1 - ajuste_posterior
            ajuste_posterior = ajuste_posterior / 4

        result_data = {
            'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
            'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14),
            'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 14),
            'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 14),
            'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 14),
            'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 14),
            'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 14),
            'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 14),
            'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 14),
            'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 14)
        }

        radiant_temperatures = {
            'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 14),
            'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 14)
        }

        radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 14)
        radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 14)
        radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 14)

        resultados_direita = f"""
- - - - - - - - - - - - - - - - - - - - - - - - - -
    ESQUERDA E DIREITA

    TEMPERATURAS RADIANTES
Esquerda: {round(radiant_temperatures['frontal_celsius'], 2)}°C
Direita: {round(radiant_temperatures['posterior_celsius'], 2)}°C
Assimetria: {round(radiant_temperatures['assimetry'], 2)}°C

    FATORES DE FORMA ESQUERDOS
Lateral esquerda: {result_data['ff_frontal_total']}
Parede frontal: {result_data['ff_frontal_lat_dir_total']}
Parede posterior: {result_data['ff_frontal_lat_esq_total']}
Teto: {result_data['ff_frontal_teto_total']}
Piso: {result_data['ff_frontal_piso_total']}

    FATORES DE FORMA DIREITOS
Lateral direita: {result_data['ff_posterior_total']}
Parede frontal: {result_data['ff_posterior_lat_dir_total']}
Parede posterior: {result_data['ff_posterior_lat_esq_total']}
Teto: {result_data['ff_posterior_teto_total']}
Piso: {result_data['ff_posterior_piso_total']}"""

## CÁLCULO TETO E PISO
        temps = {
        'temp_frontal': temp_teto,
        'temp_posterior': temp_piso,
        'temp_teto': temp_posterior,
        'temp_piso': temp_frontal,
        'temp_lat_direita': temp_lat_dir,
        'temp_lat_esquerda': temp_lat_esq
        }

        for key in temps:
            temps[key] += 273.15

        coordinates = {
            'dist_frontal': room['altura'] - room['pos_z'],
            'dist_posterior': room['pos_z'],
            'dist_piso': room['pos_y'],
            'dist_teto': room['comprimento'] - room['pos_y'],
            'dist_lat_direita': room['pos_x'],
            'dist_lat_esquerda': room['largura'] - room['pos_x'],
        }

        ort_ff_frontal_dict = {
            'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
            'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
            'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
            'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
            'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
            'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
            'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
        }

        ort_ff_posterior_dict = {
            'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
            'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
            'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
            'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
            'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
            'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
            'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
        }

        par_ff_dict = {
            'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
            'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
            'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
            'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
        }

        conferencia = {
            'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
            'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14)
        }

        ajuste_frontal = 0
        ajuste_posterior = 0

        if conferencia['sum_ff_frontal'] != 1:
            ajuste_frontal = conferencia['sum_ff_frontal']
            ajuste_frontal = 1 - ajuste_frontal
            ajuste_frontal = ajuste_frontal / 4
        
        if conferencia['sum_ff_posterior'] != 1:
            ajuste_posterior = conferencia['sum_ff_posterior']
            ajuste_posterior = 1 - ajuste_posterior
            ajuste_posterior = ajuste_posterior / 4

        result_data = {
            'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
            'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14),
            'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 14),
            'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 14),
            'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 14),
            'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 14),
            'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 14),
            'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 14),
            'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 14),
            'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 14)
        }

        radiant_temperatures = {
            'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 14),
            'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 14)
        }

        radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 14)
        radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 14)
        radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 14)

        resultados_teto = f"""
- - - - - - - - - - - - - - - - - - - - - - - - - -
    TETO E PISO

    TEMPERATURAS RADIANTES
Teto: {round(radiant_temperatures['frontal_celsius'], 2)}°C
Piso: {round(radiant_temperatures['posterior_celsius'], 2)}°C
Assimetria: {round(radiant_temperatures['assimetry'], 2)}°C

    FATORES DE FORMA TETO
Teto: {result_data['ff_frontal_total']}
Lateral direita: {result_data['ff_frontal_lat_dir_total']}
Lateral esquerda: {result_data['ff_frontal_lat_esq_total']}
Parede posterior: {result_data['ff_frontal_teto_total']}
Parede frontal: {result_data['ff_frontal_piso_total']}

    FATORES DE FORMA PISO
Piso: {result_data['ff_posterior_total']}
Lateral direita: {result_data['ff_posterior_lat_dir_total']}
Lateral esquerda: {result_data['ff_posterior_lat_esq_total']}
Parede posterior: {result_data['ff_posterior_teto_total']}
Parede frontal: {result_data['ff_posterior_piso_total']}
- - - - - - - - - - - - - - - - - - - - - - - - - -"""

        resultados = resultados_frontal + resultados_direita + resultados_teto
        resultados_label = ctk.CTkLabel(topframe, text=resultados, font=text_font, text_color=txt_color, justify='center')
        resultados_label.pack()

        def save_results():
            open('RESULTADOS.txt', 'w', encoding='utf-8').write(resultados)

        create_text_button = ctk.CTkButton(calculation_window, text='+', text_color=txt_color_alt, font=title_font, width=25, fg_color=txt_color, corner_radius=90, command=save_results)
        create_text_button.place(relx=0.85,y=17)

    def open_help(self):
        help_window = ctk.CTkToplevel()
        help_window.attributes("-topmost", True)
        help_window.title('Ajuda - Caterpillar')
        help_window.geometry('600x960')
        help_window.configure(fg_color=background)

        titulo_help = ctk.CTkLabel(help_window, text='Ajuda - Caterpillar', font=title_font, text_color=txt_color)
        titulo_help.pack(pady=20)

        topframe = ctk.CTkScrollableFrame(help_window, fg_color=foreground, height=850, width=480)
        topframe.pack(padx=60)

        primeiro_paragrafo = """
Esta é a nova versão de uma antiga ferramenta desenvolvida 
no LabEEE, uma Calculadora de Assimetria de Temperatura 
Radiante Plana (de acordo com a ISO 7726 de 1998). 

Seu uso é simples, primeiramente insira
as medidas relativas ao ambiente e, em seguida,
as medidas relativas à coordenada onde se encontra
o centro do plano no ambiente.
Feito isso, pressione o botão"""

        p_1 = ctk.CTkLabel(topframe, font=help_font, text_color=txt_color, text=primeiro_paragrafo, justify='left')
        p_1.pack(padx=5, pady=5)
        
        desenhar_help = ctk.CTkButton(topframe, text='Desenhar', font=text_font, text_color=txt_color_alt, fg_color=desenhar_color)
        desenhar_help.pack(pady=general_pady, padx=30)

        segundo_paragrafo = """Você verá o desenho do ambiente sendo feito 
no canvas à direita. Não se preocupe com medidas 
grandes, a ferramenta foi implementada com cálculos 
de ajuste de posição e proporção de desenho no fundo, 
a depender das medidas poderá ser observado que apenas 
o cubo central reduzirá para representar a proporção do 
desenho. A proporção também não afetará os cálculos
da Assimetria da Temperatura Radiante Plana.

Caso o desenho esteja de acordo com o esperado, 
basta inserir as temperaturas radiantes de cada
face do ambiente, em graus celsius, na ordem 
da representação do canvas, e clicar no botão"""

        p_2 = ctk.CTkLabel(topframe, font=help_font, text_color=txt_color, text=segundo_paragrafo, justify='left')
        p_2.pack(padx=5, pady=5) 

        calcular_help = ctk.CTkButton(topframe, text='Calcular', font=text_font, text_color=txt_color_alt, fg_color=calcular_color)
        calcular_help.pack(pady=general_pady, padx=30)
    
        terceiro_paragrafo = """Assim que os cálculos forem feitos, será aberta uma 
nova janela igual a esta contendo os resultados dos 
cálculos. Não é necessário pressionar no botão "desenho" 
para os cálculos funcionarem, esta função serve apenas 
para conferência e orientação do usuário.

Na janela de resultados, há um botão"""

        p_3 = ctk.CTkLabel(topframe, font=help_font, text_color=txt_color, text=terceiro_paragrafo, justify='left')
        p_3.pack(padx=5, pady=5) 

        create_text_button_help = ctk.CTkButton(topframe, text='+', text_color=txt_color_alt, font=title_font, width=25, fg_color=txt_color, corner_radius=90)
        create_text_button_help.pack(pady=general_pady, padx=30)

        quarto_paragrafo = """Clicar nele fará com que um arquivo de texto de 
nome "RESULTADOS" seja criado contendo os resultados
calculados."""

        p_4 = ctk.CTkLabel(topframe, font=help_font, text_color=txt_color, text=quarto_paragrafo, justify='left')
        p_4.pack(padx=5, pady=5) 

        creditos = """
Feito por Zac Milioli, LabEEE 2024
zacmilioli@gmail.com
https://www.linkedin.com/in/zac-milioli/
https://github.com/Zac-Milioli"""

        cred = ctk.CTkLabel(topframe, font=help_font, text_color=txt_color, text=creditos)
        cred.pack(padx=5, pady=20) 


if __name__ == '__main__':
    root = ctk.CTk()
    caterpillar = Caterpillar(root)
    root.mainloop()


import friendly
friendly.install(lang="ru")
from pathlib import Path
from mars import create_field, Rover
field = create_field(Path.cwd() / "05turtle" / "mars" / "mars-path-5.png")


"""
Марсоходу необходимо объехать особенно большой кратер по-кругу. Используя информацию на карте,
напишите программу движения марсохода по указанной траектории. После каждого поворота на экран
выводится текущее направление марсохода в следующем формате:

Текущий курс марсохода: 30.0 град.
Текущий курс марсохода: 60.0 град.
Текущий курс марсохода: 90.0 град.

"""

rover = Rover(-40, -160) # ровер высадился в начальных координатах

# TODO: реализуйте алгоритм движения ниже



# добавьте код решения до этого комментария
field.mainloop()
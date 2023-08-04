import friendly
friendly.install(lang="ru")
from pathlib import Path
from mars import create_field, Rover
field = create_field(Path.cwd() / "05turtle" / "mars" / "mars-path-4.png")


"""
Исследуя поверхность Марса, марсоход обнаружил три кратера. Напишите программу с помощью которой
марсоход посетит все три кратера по заданному маршруту. Для написания программы используйте
информацию на карте.
"""

rover = Rover(-160, -135) # ровер высадился в начальных координатах

# TODO: реализуйте алгоритм движения ниже



# добавьте код решения до этого комментария
field.mainloop()
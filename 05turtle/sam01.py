import friendly
friendly.install(lang="ru")
from pathlib import Path
from mars import create_field, Rover
field = create_field(Path.cwd() / "05turtle" / "mars" / "mars-path-1.png")


"""
Марсоход находится на площадке размером 400x400 метров. Ваша задача проехать исследуемую
площадку по периметру. Путь следования марсохода изображен белым цветом.
"""

rover = Rover(-165, -165) # ровер высадился в начальных координатах

# TODO: реализуйте алгоритм движения ниже



# добавьте код решения до этого комментария
field.mainloop()

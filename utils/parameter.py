from os import path
from utils.type import Size, Color
from utils.constants import WHITE, BLACK, GREY


class Parameter:
    default_size: Size = Size(490, 490)
    bg_color: Color = WHITE

    # Grid settings
    grid_rows: int = 49
    grid_cols: int = 49
    grid_color: Color = GREY

    # Tile settings
    tile_size: int = 10
    tile_dead_color: Color = WHITE
    tile_alive_color: Color = BLACK

    # Font settings
    font_size: int = 24
    font_name: str = "Arial"
    font_color: Color = BLACK

    # Rules
    rules = "1:2-3,0:3"

    @staticmethod
    def save_to_file(filename: str) -> None:
        # Open the file and write the parameters
        with open(filename, "w") as f:
            f.write(f"default_size= {str(Parameter.default_size)}\n")
            f.write(f"bg_color= {str(Parameter.bg_color)}\n")

            f.write(f"grid_rows= {Parameter.grid_rows}\n")
            f.write(f"grid_cols= {Parameter.grid_cols}\n")
            f.write(f"grid_color= {str(Parameter.grid_color)}\n")

            f.write(f"tile_size= {Parameter.tile_size}\n")
            f.write(f"tile_dead_color= {str(Parameter.tile_dead_color)}\n")
            f.write(f"tile_alive_color= {str(Parameter.tile_alive_color)}\n")

            f.write(f"font_size= {Parameter.font_size}\n")
            f.write(f"font_name= {Parameter.font_name}\n")
            f.write(f"font_color= {str(Parameter.font_color)}\n")

            f.write(f"rules= {Parameter.rules}")

    @staticmethod
    def load_from_file(filename: str) -> None:
        # Check if the tile exist
        if not path.exists(filename):
            return

        # Open the and read the parameters
        with open(filename, "r") as f:
            for line in f:
                # Split the line into key and value
                key, value = line.split("=")
                # Strip whitespace and convert the value to the appropriate type
                key = key.strip()

                if key == "default_size":
                    Parameter.default_size = Size(*map(int, value.split(",")))
                elif key == "bg_color":
                    Parameter.bg_color = Color(*map(int, value.split(",")))

                elif key == "grid_rows":
                    Parameter.grid_rows = int(value)
                elif key == "grid_cols":
                    Parameter.grid_cols = int(value)
                elif key == "grid_color":
                    Parameter.grid_color = Color(*map(int, value.split(",")))

                elif key == "tile_size":
                    Parameter.tile_size = int(value)
                elif key == "tile_dead_color":
                    Parameter.tile_dead_color = Color(*map(int, value.split(",")))
                elif key == "tile_alive_color":
                    Parameter.tile_alive_color = Color(*map(int, value.split(",")))

                elif key == "font_name":
                    Parameter.font_name = value.strip()
                elif key == "font_size":
                    Parameter.font_size = int(value)
                elif key == "font_color":
                    Parameter.font_color = Color(*map(int, value.split(",")))

                elif key == "rules":
                    Parameter.rules = str(value.strip())

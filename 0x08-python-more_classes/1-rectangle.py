
#!/usr/bin/python3
"""This module provides a class for representing rectangles."""


class Rectangle:
    """A class to represent rectangles"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance\
        with the specified width and height.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

        @property
        def height(self):
            """
            Getter method for height attribute.

            Returns:
                int: The height of the rectangle.
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter method for height attribute.

            Args:
                value (int): The height of the rectangle.
            Raises:
                TypeError: If height is not an integer.
                ValueError: If height is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

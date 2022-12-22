Feature: Testing lab 3

    Scenario Outline: Testing properties of rectangle
        Given rectangle with sides of "<first>" and "<second>", color is "<color>"
        When we try to get properties
        Then we get square of "<square>", color is "<color>"

        Examples: Rectangle
            | first | second | color | square |
            | 9     | 4      | blue  | 45     |
            | 5     | 1      | red   | 5      |
            | 99    | 98     | yellow| 9702   |

    Scenario Outline: Testing properties of circle
        Given circle with radius of "<radius>", color is "<color>"
        When we try to get properties
        Then we get square of "<square>", color is "<color>"

        Examples: Circle
            | radius | color | square             |
            | 1      | cyan  | 3.141592653589793  |
            | 12     | gray  | 37.69911184307752  |
            | 200    | black | 348.71678454846705 |

    Scenario Outline: Testing properties of circle
        Given square with side of "<side>", color is "<color>"
        When we try to get properties
        Then we get square of "<square>", color is "<color>"

        Examples: Square
            | side | color | square |
            | 1    | lime  | 1      |
            | 12   | pink  | 144    |
            | 200  | white | 40000  |

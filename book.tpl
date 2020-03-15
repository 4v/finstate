<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
        <style>
            body {{
                line-height: 1em;
                letter-spacing: 0;
                font-size: 0.6rem;
                background: black;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <center><h2>{{ title }}<h2></center>
%for f in books:
    <img src=" {{ f }} "><br>
%end
    </body>
</html>